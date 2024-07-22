from mission import Mission
from aircraft import Aircraft


ac1 = Aircraft(3.5)
ac1.set_thrust_zero(91)

flight1 = Mission('flight1', ac1, 30, 300)


print('Fluggeschwindigkeit in m/s:  {}'.format(round(flight1.get_velo_lift_off(), 2)))
print('Fluggeschwindigkeit in km/h: {}'.format(round(flight1.get_velo_lift_off()*3.6, 2)))
print('Runway:                      {}'.format(flight1.get_runway_length()))