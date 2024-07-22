
from math import sin, cos, pi, sqrt


def propeller_thrust_at_velocity(thrust_stand, flight_velocity, flight_velocity_max):
    return thrust_stand * ( 1 - (flight_velocity / flight_velocity_max)**2 )

def propeller_flight_velocity_max():
    return 0