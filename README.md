
# IIQ3843: Benchmark de Materiales Nacionales para Almacenamiento Térmico (PBTS)

## Propósito del Proyecto
El almacenamiento térmico sensible (TES) en lechos empacados es una tecnología ampliamente usada en aplicaciones solares e industriales, este sistema consiste en un fluido caliente (como aire o agua ) que circula a través de un tanque cílindrico relleno de particulas sólidas transfiriendo calor por convección externa e interna por conducción dentro del sólido que almacenan energía térmica por cambio de temperatura.

Este proyecto consiste en la modificación y expansión de un código de simulación de calor sensible (*open-source* basado en OpenTerrace) para evaluar el rendimiento de 10 materiales granulares, priorizando alternativas chilenas de bajo costo y alto impacto, despues de un exhaustiva revision realizada por [Georgousis, (2025)](https://www.sciencedirect.com/science/article/pii/S2352152X25012290), escogiendo finalmente los 10 mejores materiales sólidos y con mayor impacto en Chile: Escoria de Cobre, Basalto, Diorita, Residuos de Demolición, Gabro, Granito, Magnetita, Basalto y la Caliza.

El objetivo es generar un Benchmark Comparativo que permita la toma de decisiones informada para el diseño de sistemas de Almacenamiento Térmico en Lecho Empacado (PBTS), contribuyendo a la cadena de valor local y a la descarbonización industrial en Chile.El principal problema que se esta enfrentando en Chile la mayoría de medios para TES son importados, siendo la principal la Alúmina.

## Importancia de buscar alternativas a la alúmina como medio de almacenamiento térmico

El norte de Chile posee uno de los niveles mas altos de irradiancia solar (2800-300kWh/m^2*año) [World Bank Group & ESMAP. (2023)](https://globalsolaratlas.info/map?c=-21.542511,-69.620361,8&s=-20.463043,-69.422607&m=site), lo cual hace esta tecnologías de almacenamiento térmico fundamentales para la estabilidad,
Actualmente para estos sistemas, la alúmina (Al₂O₃) sigue siendo uno de los materiales más utilizados en sistemas de almacenamiento térmico sensible (TES), presentando problemas críticos a nivel internacional y especialmente para Chile que no produce alúmina, Chile importa entre 30.000 y 40.000 toneladas anuales [Importación alumina](https://comtradeplus.un.org/) 

Esto significa que proyectos en Chile dependen completamente de **importar cientos de toneladas** de material.

---

## Modelo Matemático Implementado

El sistema PBTS se modela mediante el Modelo 1-D (Axial) No Estacionario de Dos Fases, que considera un balance de energía separado para el fluido (HTF) y el material sólido.
La alúmina se utiliza como material de referencia, y cada material se compara bajo condiciones idénticas.

### 1. Ecuaciones del Balance de Energía

El modelo resuelve la transferencia de calor a lo largo de la dimensión axial ($z$) y el tiempo ($t$), acoplando ambas fases mediante el término convectivo $h_v(T_s - T_f)$.

Balance de Energía en el Fluido ($T_f$):
El fluido (HTF) fluye por convección e intercambia calor con las partículas sólidas.Utilizando la ecuación en donde se ignora la conducción axial  

$$\varepsilon \rho_f C_{p,f} \frac{\partial T_f}{\partial t} + \rho_f C_{p,f} u_f \frac{\partial T_f}{\partial z} = h_v (T_s - T_f)$$

Balance de Energía en el Sólido ($T_s$):
El sólido se modela con conducción radial transitoria Esta ecuación representa el Modelo Lumped (Agrupado), donde se desprecia la variación de temperatura dentro de la partícula, siendo consistente con la configuración del benchmark (`n_other=1`).:

$$(1 - \varepsilon) \rho_s C_{p,s} \frac{\partial T_s}{\partial t} = h_v (T_f - T_s)$$

Donde:
* $\varepsilon$: Porosidad del lecho.
* $\rho, C_p$: Densidad y calor específico.
* $u_f$: Velocidad del fluido.
* $h_v$: Coeficiente de transferencia de calor volumétrico (el término de acoplamiento).
  
## Geometría del tanque 
Basado en las dimensiones de [Zanganeh](https://www.sciencedirect.com/science/article/pii/S0038092X12002812), a escala de planta piloto:
* Altura : 3m 
* Diametro del tanque : 0.03m
* Porosidad: 0.4 kg/s
* Diametro particula: 0.05m


### 2. Puntos Clave del código

1.  **Corrección 1D Axial:** Se corrigió el error dimensional forzando las fases Fluidas y Sólidas a tener consistencia de nodos (`n_other=1`) para simular el eje Z (axial) únicamente.
2.  **Acoplamiento:** Se utilizó `ot.select_coupling()` para implementar el término $h_v$.
3.  **Benchmark Automatizado:** Se implementó un bucle que itera la simulación a través de las propiedades termofísicas de los 10 materiales y recopila los datos (`T_xt`) para la comparación gráfica.
---

##  Instrucciones de Uso

Para replicar la simulación y el benchmark:

1.  **Clonar el Repositorio:** `git clone https://docs.github.com/es/repositories/creating-and-managing-repositories/quickstart-for-repositories`
2.  **Crear Entorno Virtual:** `python -m venv .venv`
3.  **Activar Entorno:** `.\.venv\Scripts\activate`
4.  **Instalar Dependencias:** `pip install  openterrace.txt`, `pip install  matplotlib.pyplot.txt`, `pip install  numpy.txt`,`pip install  os.txt`,`pip install  pickle.txt`,`pip install  pathlib.txt`.
5.  **Ejecutar Simulaciones:** Ejecutar los 10 scripts de simulación individuales (ej. `python simular_alumina.py`). Esto generará los archivos `.pkl` en la carpeta `resultados/`. 
6.  **Generar Benchmark:** `python benchmark_desde_pkls.py`

---



##  Resultados Clave (Benchmark)
### Figura 1: Perfil axial vs Tiempo 

<img width="614" height="461" alt="image" src="https://github.com/user-attachments/assets/a8af19ed-9cb0-4da3-ada6-0456fb1474e4" />

**Fuente:** Elaboración Propia a partir de la simulación del Modelo 1-D (Axial) implementado en OpenTerrace.

### Figura 2: Curva de Salida (Benchmark T de Salida vs Tiempo)

<img width="614" height="461" alt="image" src="https://github.com/user-attachments/assets/c0d45929-80fc-4745-ae3d-6bd8cd816efb" />

**Fuente:** Elaboración Propia a partir de la simulación del Modelo 1-D (Axial) implementado en OpenTerrace.


La simulación demuestra que la Escoria de Cobre y la Magnetita poseen el mejor rendimiento de almacenamiento volumétrico, superando a las rocas geológicas más comunes (Basalto, Granito), validando una alternativa de alto impacto para la industria nacional.
