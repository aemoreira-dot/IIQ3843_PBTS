"""
Data for Diorita (Igneous Rock).
rho = 2800 (density, average)
k = 2.5 (thermal conductivity, average)
cp = 1000 (specific heat capacity)
"""
_RHO = 2800.0
_K = 2.5
_CP = 1000.0

def h(T:float) -> float:
    return 1000 * T

def T(h:float, p:float=None) -> float:
    return 1.0 / 1000 * h

def rho(h:float, p:float=None) -> float:
    return 2800 * h**0

def k(h:float, p:float=None) -> float:
    return 2.5* h**0

def cp(h:float, p:float=None) -> float:
    return 1000 * h**0
    