#!/usr/bin/python3
from math import sin, cos, pi, sqrt





# Variables
temp_celsius =     15.0
temp_kelvin  =    273.15 + temp_celsius
area_wing    =      0.525
#area_wing    =      2.1
#area_wing    =      8.4
c_A_cruise   =      0.12
c_A_toff     =      0.30
c_D_cruise   =      0.02
c_D_toff     =      0.03
velo_toff    =     18.05 
velo_ekin    =     80.0 / 3.6
velo_cruise  =     55.0
sfc          =      1.17 # kg / h / daN

mass_ac      =      3.00 # kg



# Constants
rho_0      = 1.225
rho_7000   = 0.498
kmh_to_mps = 1/3.6
mps_to_kmh = 3.6


def lift(c_A, rho_0, velo, area_wing):
    lift = c_A * rho_0 / 2 * velo**2 * area_wing
    lift = lift * 2 / 3 # Wegen elliptischer Auftriebsverteilung
    return lift


def drag(c_D, rho_0, velo, area_wing):
    drag = c_D * rho_0 / 2 * velo**2 * area_wing
    return drag

def fuel_consumption(sfc, drag, velo_mps):
    # drag in Newton
    # speed in km / h
    # 0.117 kg / h / N
    # sfc = kg / daN / h
    fuel_per_hundred_km = sfc / 3600 # kg fuel per second per Newton
    fuel_per_hundred_km = fuel_per_hundred_km * drag # kg fuel per second
    fuel_per_hundred_km = fuel_per_hundred_km / velo_mps # kg fuel per meter 
    fuel_per_hundred_km = fuel_per_hundred_km * 100000 # kg fuel per 100 km 
    return fuel_per_hundred_km

def energy_kin(velo, mass):
    e_kin = 0.5 * mass * velo**2
    return e_kin


def energy_pot(height, mass, g=9.81):
    e_pot = mass * g * height
    return e_pot

E_kin_80_pot_20 = (energy_kin(velo_ekin, mass_ac) + energy_pot(20.0, mass_ac)) / 3600 # from Joule to Watt-hours
    

print('Energy:      {:>5s} Wh'.format(str(round(E_kin_80_pot_20, 1))))

lift_toff     = lift(c_A_toff,    rho_0,    velo_toff,   area_wing)
lift_cruise   = lift(c_A_cruise,  rho_7000, velo_cruise, area_wing)
drag_toff     = drag(c_D_toff,    rho_0,    velo_toff,   area_wing)
drag_cruise   = drag(c_D_cruise,  rho_7000, velo_cruise, area_wing)

fuel_consumption_toff     = fuel_consumption(sfc, drag_toff,   velo_toff )
fuel_consumption_cruise   = fuel_consumption(sfc, drag_cruise, velo_cruise)


print()
print('Constants:') 
print('Wing area: {:>5s} m**2'.format(str(area_wing)))
print('Temp:      {:>5s} ° C'.format(str(round(temp_celsius, 1))))


print()
print('Takeoff conditions:') 
print('Lift:      {:>5s} N'.format(str(round(lift_toff, 1))))
print('Velocity:  {:>5s} m/s'.format(str(round(velo_toff, 1))))
print('Velocity:  {:>5s} km/h'.format(str(round(velo_toff*3.6, 1))))
print('Height:        0 m')


print()
print('Cruise conditions:') 
print('Lift:      {:>5s} N'.format(str(round(lift_cruise, 1))))
print('Velocity:  {:>5s} m/s'.format(str(round(velo_cruise, 1))))
print('Velocity:  {:>5s} km/h'.format(str(velo_cruise*3.6)))
print('Height:   {:<6s} m'.format(str(round(7000.0, 1))))
print('Drag:      {:>5s} N'.format(str(round(lift_cruise, 1))))
print('Fuel:      {:>5s} kg/100 km'.format(str(round(fuel_consumption_cruise, 1))))



print()
print('Energy in 20 m height at 80 km/h:') 
print('Energy:      {:>5s} Wh'.format(str(round(E_kin_80_pot_20, 1))))
print('Mass:        {:>5s} kg'.format(str(round(mass_ac, 1))))

