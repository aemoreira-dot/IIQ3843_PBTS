"""
Data for Gabro (Igneous Rock).
rho = 2950 (density, average)
k = 2.6(thermal conductivity, average)
cp = 600 (specific heat capacity, assumed average)
"""
_RHO = 2950.0
_K = 2.6
_CP = 600

def h(T:float) -> float:
    return 600 * T

def T(h:float, p:float=None) -> float:
    return 1.0 / 600 * h

def rho(h:float, p:float=None) -> float:
    return 2950 * h**0

def k(h:float, p:float=None) -> float:
    return 2.6 * h**0

def cp(h:float, p:float=None) -> float:
    return 600 * h**0