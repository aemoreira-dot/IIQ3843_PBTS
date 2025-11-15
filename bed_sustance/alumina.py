"""
Data for Alumina (Ceramic).
rho = 3550 (density)
k = 30 (thermal conductivity)
cp = 920 (specific heat capacity at constant pressure)
"""
_RHO = 3550.0
_K = 30.0
_CP = 920.0

def h(T:float) -> float:
    """Mass specific enthalpy as function of temperature."""
    # h = cp * T
    return 920 * T

def T(h:float, p:float=None) -> float:
    """Temperature as function of mass specific enthalpy."""
    # T = h / cp
    return 1.0 / 920 * h

def rho(h:float, p:float=None) -> float:
    """Density as function of mass specific entahlpy (assumes constant density)."""
    return 3550 * h**0

def k(h:float, p:float=None) -> float:
    """Thermal conductivity as function of mass specific enthalpy (assumes constant k)."""
    return 3 * h**0

def cp(h:float, p:float=None) -> float:
    """Specific heat capacity as function of mass specific enthalpy (assumes constant cp)."""
    return 920 * h**0