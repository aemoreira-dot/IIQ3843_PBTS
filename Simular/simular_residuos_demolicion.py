import openterrace
import matplotlib.pyplot as plt
import os, pickle
from pathlib import Path

SOLID_NAME = "residuos_demolicion"
OUTPUT_DIR = Path("resultados")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_FILENAME = OUTPUT_DIR / f"resultados_{SOLID_NAME}.pkl"

def main():
    ot = openterrace.Simulate(t_end=100*60, dt=0.05)

    fluid = ot.create_phase(n=100, type='fluid')
    fluid.select_substance(substance='water')
    fluid.select_domain_shape(domain='cylinder_1d', D=0.3, H=3)
    fluid.select_porosity(phi=0.4)
    fluid.select_schemes(diff='central_difference_1d', conv='upwind_1d')
    fluid.select_initial_conditions(T=273.15+20)
    fluid.select_massflow(mdot=0.04) #ks/s
    fluid.select_bc(bc_type='fixed_value',
                    parameter='T',
                    position=(slice(None, None, None), 0),
                    value=273.15+80)
    fluid.select_bc(bc_type='zero_gradient',
                    parameter='T',
                    position=(slice(None, None, None), -1))
    fluid.select_output(times=[0, 30, 60, 90, 120, 150, 180, 210,
                        240, 270, 300, 600, 900,
                        1800, 3600, 5400, 6000])

    bed = ot.create_phase(n=20, n_other=100, type='bed')
    bed.select_substance('residuos_demolicion')
    bed.select_domain_shape(domain='hollow_sphere_1d', Rinner=0.005, Router=0.025)
    bed.select_schemes(diff='central_difference_1d')
    bed.select_initial_conditions(T=273.15+20)
    bed.select_bc(bc_type='zero_gradient',
                parameter='T',
                position=(slice(None, None, None), 0))
    bed.select_bc(bc_type='zero_gradient',
                parameter='T',
                position=(slice(None, None, None), -1))
    bed.select_output(times=range(0,600+300,300))

    ot.select_coupling(fluid_phase=0, bed_phase=1, h_exp='constant', h_value=200)
    ot.run_simulation()

    plt.plot(fluid.node_pos,fluid.data.T[:,0,:].T-273.15, label=fluid.data.time/60)
    plt.legend(title='Simulation time (min)')
    plt.xlabel(u'Cylinder position (m)')
    plt.ylabel(u'Temperature (℃)')
    plt.grid()
    plt.grid(which='major', color='#DDDDDD', linewidth=1)
    plt.grid(which='minor', color='#EEEEEE', linestyle=':', linewidth=0.8)
    plt.minorticks_on()
    plt.savefig('imagenes/residuos_demolicion.svg')

    #guardar resultados como pkl
    try:
        
        T_xt = fluid.data.T[:, 0, :]          
    except Exception:
       
        import numpy as np
        T_raw = getattr(fluid.data, "T")
        T_arr = np.asarray(T_raw)
        if T_arr.ndim == 3:
            T_xt = T_arr[:, 0, :]
        elif T_arr.ndim == 2:
            T_xt = T_arr
        else:
            raise RuntimeError(f"Error: {T_arr.shape}")

    payload = {
        "solid_name": SOLID_NAME,
        "x": getattr(fluid, "node_pos"),   
        "t": getattr(fluid.data, "time"),  
        "T_xt": T_xt,                      
        "params": {
            "D": 0.3, "H": 3.0, "phi": 0.4, "mdot": 0.04,
            "h": 200, "Tin_C": 80.0, "T0_C": 20.0
        }
    }
    with open(OUTPUT_FILENAME, "wb") as f:
        pickle.dump(payload, f)
    print(f"[OK] Guardado PKL: {OUTPUT_FILENAME}")

if __name__ == "__main__":
    main()