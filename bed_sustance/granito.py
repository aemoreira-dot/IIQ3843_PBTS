"""
Data for Granito (Granite).
rho = 2600 (density)
k = 2.8 (thermal conductivity)
cp = 820 (specific heat capacity at constant pressure)
"""
_RHO = 2600.0
_K = 2.8
_CP = 820.0

def h(T:float) -> float:
    return 820 * T

def T(h:float, p:float=None) -> float:
    return 1.0 / 820 * h

def rho(h:float, p:float=None) -> float:
    return 2600 * h**0

def k(h:float, p:float=None) -> float:
    return 2.8 * h**0

def cp(h:float, p:float=None) -> float:
    return 820 * h**0