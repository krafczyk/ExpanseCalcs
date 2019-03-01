import unyt as u
import math as m

# Globals
g = 9.807*(u.m/u.second**2)

# Characteristics of ceres
# From: https://en.wikipedia.org/wiki/Ceres_(dwarf_planet)
m_ceres = 9.393e20*u.kg
R_ceres = 473000*u.m
T_ceres = 0.3781*u.day

rho_ceres = m_ceres/((4./3.)*m.pi*R_ceres**3)

surf_grav = 0.32*g
v_sh = (surf_grav*R_ceres+(u.G*m_ceres/R_ceres))**0.5

T = (2*m.pi*R_ceres/v_sh)

print("Rotational Period: ", T.to('min'))
print("Spin needs to be ", (T_ceres/T.to('day')).value, " times faster")

# Gravity will fall linearly until you hit the pole
# This assumes you're on the equatorial axis 
