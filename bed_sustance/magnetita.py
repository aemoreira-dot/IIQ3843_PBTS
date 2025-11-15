"""
Data for Magnetita (Mineral).
rho = 4962 (density)
k = 3.1 (thermal conductivity)
cp = 850 (specific heat capacity at constant pressure)
"""
_RHO = 4962.0
_K = 3.1
_CP = 850.0

def h(T:float) -> float:
    return 850 * T

def T(h:float, p:float=None) -> float:
    return 1.0 / 850 * h

def rho(h:float, p:float=None) -> float:
    return 4962 * h**0

def k(h:float, p:float=None) -> float:
    return 3.1 * h**0

def cp(h:float, p:float=None) -> float:
    return 850 * h**0