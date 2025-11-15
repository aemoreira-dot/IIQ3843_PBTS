"""
Data for Escoria Cobre (Copper Slag) - Sample ES-N.
rho = 300 (density)
k = 1.5 (thermal conductivity)
cp = 900 (specific heat capacity at constant pressure)
"""
_RHO = 3000
_K = 1.5
_CP = 900.0

def h(T:float) -> float:
    return 900 * T

def T(h:float, p:float=None) -> float:
    return 1.0 / 900 * h

def rho(h:float, p:float=None) -> float:
    return 3000* h**0

def k(h:float, p:float=None) -> float:
    return 1.5 * h**0

def cp(h:float, p:float=None) -> float:
    return 900 * h**0