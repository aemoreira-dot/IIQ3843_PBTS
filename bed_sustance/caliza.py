"""
Data for Caliza (Sedimentary Rock).
rho = 2800(density, average)
k = 3 (thermal conductivity, average)
cp = 908 (specific heat capacity, average of 683-908 J/kgK)
"""
_RHO = 2800
_K = 3
_CP = 908

def h(T:float) -> float:
    return 908 * T

def T(h:float, p:float=None) -> float:
    return 1.0 / 908 * h

def rho(h:float, p:float=None) -> float:
    return 2800 * h**0

def k(h:float, p:float=None) -> float:
    return 3 * h**0

def cp(h:float, p:float=None) -> float:
    return 908 * h**0