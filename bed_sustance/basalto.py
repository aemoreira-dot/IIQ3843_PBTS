"""
Data for Basalto (Basalt).
rho = 2800 (density)
k = 2.1 (thermal conductivity)
cp = 755 (specific heat capacity at constant pressure)
"""
_RHO = 2800.0
_K = 2.1
_CP = 755.0
NAME = 'basalto'  


def h(T:float) -> float:
    return 755 * T

def T(h:float, p:float=None) -> float:
    return 1.0 / 755 * h

def rho(h:float, p:float=None) -> float:
    return 2800 * h**0

def k(h:float, p:float=None) -> float:
    return 2.1 * h**0

def cp(h:float, p:float=None) -> float:
    return 755 * h**0