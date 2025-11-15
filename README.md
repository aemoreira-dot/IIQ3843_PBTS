
# IIQ3843: Benchmark de Materiales Nacionales para Almacenamiento Térmico (PBTS)

## Propósito del Proyecto

Este proyecto consiste en la Modificación y Expansión de un código de simulación de calor sensible (*open-source* basado en OpenTerrace) para evaluar el rendimiento de 10 materiales granulares, priorizando alternativas chilenas de bajo costo y alto impacto (ej. Escoria de Cobre, Basalto).

El objetivo es generar un Benchmark Comparativo que permita la toma de decisiones informada para el diseño de sistemas de Almacenamiento Térmico en Lecho Empacado (PBTS), contribuyendo a la cadena de valor local y a la descarbonización industrial en Chile.

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
