# benchmark_desde_pkls.py
import pickle
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

RESULTS_DIR = Path("resultados")
IMG_DIR = Path("imagenes")
IMG_DIR.mkdir(parents=True, exist_ok=True)

def cargar_pkls():
    datasets = []
    if not RESULTS_DIR.exists():
        print(f"[ERROR] No existe la carpeta {RESULTS_DIR.resolve()}.")
        return datasets
    for p in sorted(RESULTS_DIR.glob("resultados_*.pkl")):
        try:
            with open(p, "rb") as f:
                d = pickle.load(f)
            # Validación mínima
            if all(k in d for k in ("solid_name", "x", "t", "T_xt")):
                datasets.append(d)
                print(f"[OK] Cargado: {p.name}")
            else:
                print(f"[WARN] PKL incompleto: {p.name}")
        except Exception as e:
            print(f"[WARN] No se pudo leer {p.name}: {e}")
    return datasets

def main():
    data = cargar_pkls()
    if not data:
        print("No se encontraron PKL válidos en 'resultados/'.")
        return

    
    plt.figure()
    for d in data:
        t_min = np.asarray(d["t"], dtype=float)/60
        T_out_C = np.asarray(d["T_xt"], dtype=float)[:, -1] - 273.15
        plt.plot(t_min, T_out_C, label=d["solid_name"])
    plt.xlabel("Tiempo (min)")
    plt.ylabel("T salida del fluido (°C)")
    plt.title("Benchmark: T de salida vs tiempo")
    plt.grid(True, which="both", alpha=0.35)
    plt.legend(title="Material", fontsize=8)
    plt.tight_layout()
    plt.xlim(20,100)
    plt.savefig(IMG_DIR / "benchmark_Tout_vs_t.png", dpi=300)
    plt.savefig(IMG_DIR / "benchmark_Tout_vs_t.svg")

    
    plt.figure()
    tiempos_finales_min = {}
    for d in data:
        x = np.asarray(d["x"], dtype=float)
        T_final_C = np.asarray(d["T_xt"], dtype=float)[-1, :] - 273.15
        plt.plot(x, T_final_C, label=d["solid_name"])
        tiempos_finales_min[d["solid_name"]] = float(d["t"][-1])/60
    iguales = len({round(v, 6) for v in tiempos_finales_min.values()}) == 1
    titulo = "Benchmark: perfil axial al tiempo final"
    if iguales:
        titulo += f" (t = {next(iter(tiempos_finales_min.values())):.0f} min)"
    plt.title(titulo)
    plt.xlabel("Posición axial en cilindro (m)")
    plt.ylabel("T fluido (°C)")
    plt.grid(True, which="both", alpha=0.35)
    plt.legend(title="Material", fontsize=8)
    plt.tight_layout()
    plt.savefig(IMG_DIR / "benchmark_perfil_axial_final.png", dpi=200)
    plt.savefig(IMG_DIR / "benchmark_perfil_axial_final.svg")

    print("Listo. Figuras guardadas en 'imagenes/'.")

if __name__ == "__main__":
    main()
