
# IIQ3843: Benchmark de Materiales Nacionales para Almacenamiento Térmico (PBTS)

## Propósito del Proyecto

Este proyecto consiste en la modificación y expansión de un código de simulación de calor sensible (*open-source* basado en OpenTerrace) para evaluar el rendimiento de 10 materiales granulares, priorizando alternativas chilenas de bajo costo y alto impacto (ej. Escoria de Cobre, Basalto).

El objetivo es generar un Benchmark Comparativo que permita la toma de decisiones informada para el diseño de sistemas de Almacenamiento Térmico en Lecho Empacado (PBTS), contribuyendo a la cadena de valor local y a la descarbonización industrial en Chile.

En Chile, la mayoría de medios para TES son **importados** (p. ej., alúmina). Este proyecto crea una **metodología reproducible** para comparar **materiales locales** (granito, basalto, escoria de cobre, etc.)

## Modelo Matemático Implementado

El sistema PBTS se modela mediante el Modelo 1-D (Axial) No Estacionario de Dos Fases, que considera un balance de energía separado para el fluido (HTF) y el material sólido.

### 1. Ecuaciones del Balance de Energía

El modelo resuelve la transferencia de calor a lo largo de la dimensión axial ($z$) y el tiempo ($t$), acoplando ambas fases mediante el término convectivo $h_v(T_s - T_f)$.

Balance de Energía en el Fluido ($T_f$):

$$\varepsilon \rho_f C_{p,f} \frac{\partial T_f}{\partial t} + \rho_f C_{p,f} u_f \frac{\partial T_f}{\partial z} = h_v (T_s - T_f)$$

Balance de Energía en el Sólido ($T_s$):

$$(1 - \varepsilon) \rho_s C_{p,s} \frac{\partial T_s}{\partial t} = h_v (T_f - T_s)$$

Donde:
* $\varepsilon$: Porosidad del lecho.
* $\rho, C_p$: Densidad y calor específico.
* $u_f$: Velocidad del fluido.
* $h_v$: Coeficiente de transferencia de calor volumétrico (el término de acoplamiento).
#### 📐 3. Ecuaciones de Balance de Energía

Este proyecto simula el comportamiento térmico de un tanque TES de **lecho empacado** mediante la solución acoplada de las ecuaciones de energía del **fluido** y del **sólido**, usando *OpenTerrace*.  
La **alúmina** se utiliza como **material de referencia**, y cada material se compara bajo condiciones idénticas.

---

### 🔥 3.1. Balance de energía del fluido (dirección axial *z*)

El fluido (agua) intercambia calor con las partículas, fluye por convección y presenta difusión/dispersion axial.  

\[
\varepsilon \,\rho_f c_{p,f}\,\frac{\partial T_f}{\partial t}
+\varepsilon \,\rho_f c_{p,f}\,u\,\frac{\partial T_f}{\partial z}
=
\frac{\partial}{\partial z}\left( k_{\mathrm{ax}} \frac{\partial T_f}{\partial z} \right)
- a_s\, h \left(T_f - T_s^{\mathrm{surf}}\right)
\]

**Donde:**

- \(\varepsilon\): porosidad del lecho.  
- \(u\): velocidad superficial del fluido.  
- \(k_{\mathrm{ax}}\): conductividad/dispersion axial efectiva.  
- \(a_s\): área específica sólido–fluido por volumen.  
- \(h\): coeficiente convectivo fluido–sólido.  
- \(T_s^{\mathrm{surf}}\): temperatura de la superficie de la partícula sólida.

**Condiciones de borde:**

\[
T_f(0,t)=80^\circ\mathrm{C}, \qquad 
\frac{\partial T_f}{\partial z}(H,t)=0
\]

**Condición inicial:**

\[
T_f(z,0)=20^\circ\mathrm{C}
\]

---

### 🪨 3.2. Balance de energía del sólido (partícula esférica hueca)

El sólido se modela con conducción radial transitoria:

\[
\rho_s c_{p,s}\,\frac{\partial T_s}{\partial t}
=
\frac{1}{r^2}
\frac{\partial}{\partial r}
\left( k_s r^2 \frac{\partial T_s}{\partial r} \right)
\]

**Condiciones de borde:**

- **Radio interno (aislado):**  
  \[
  \left.\frac{\partial T_s}{\partial r}\right|_{r=R_{\mathrm{in}}}=0
  \]

- **Superficie externa (interfaz fluido–sólido):**  
  \[
  -k_s 
  \left.\frac{\partial T_s}{\partial r}\right|_{r=R_{\mathrm{out}}}
  =
  h \left(T_s(R_{\mathrm{out}},t) - T_f(z,t)\right)
  \]

**Condición inicial:**  
\[
T_s(r,0)=20^\circ\mathrm{C}
\]

---

### 🔗 3.3. Acoplamiento fluido–sólido

El intercambio de calor en la interfaz está dado por:

\[
q'' = h\,(T_f - T_s^{\mathrm{surf}})
\]

Este flujo se resta en la ecuación del fluido (pierde calor) y se suma en la del sólido (gana calor).

---

### 🧮 3.4. Métodos numéricos utilizados

Los esquemas definidos en el código son:

- **Convección (fluido):** upwind 1D  
- **Difusión (fluido y sólido):** diferencia central 1D  
- **Avance temporal:** integración explícita con paso  
  \[
  \Delta t = 0.05\ \mathrm{s}
  \]

OpenTerrace gestiona la malla espacial y el ensamblaje de los sistemas para ambas fases, asegurando estabilidad mediante restricciones tipo CFL/Fourier.

---


### 2. Puntos Clave del código

1.  **Corrección 1D Axial:** Se corrigió el error dimensional forzando las fases Fluidas y Sólidas a tener **consistencia de nodos** (`n_other=1`) para simular el eje Z (axial) únicamente.
2.  **Acoplamiento:** Se utilizó `ot.select_coupling()` para implementar el término $h_v$.
3.  **Benchmark Automatizado:** Se implementó un bucle que itera la simulación a través de las propiedades termofísicas de los **10 materiales** y recopila los datos (`T_xt`) para la comparación gráfica.

---

##  Instrucciones de Uso

Para replicar la simulación y el benchmark:

1.  **Clonar el Repositorio:** `git clone https://docs.github.com/es/repositories/creating-and-managing-repositories/quickstart-for-repositories`
2.  **Crear Entorno Virtual:** `python -m venv .venv`
3.  **Activar Entorno:** `.\.venv\Scripts\activate`
4.  **Instalar Dependencias:** `pip install -r requirements.txt`
5.  **Ejecutar Simulaciones:** Ejecutar los 10 scripts de simulación individuales (ej. `python simular_alumina.py`). Esto generará los archivos `.pkl` en la carpeta `resultados/`.
6.  **Generar Benchmark:** `python benchmark_desde_pkls.py`

---

'''
hola
'''

##  Resultados Clave (Benchmark)

La simulación demuestra que la **Escoria de Cobre** y la **Magnetita** poseen el mejor rendimiento de almacenamiento volumétrico, superando a las rocas geológicas más comunes (Basalto, Granito), validando una **alternativa de alto impacto** para la industria nacional.
