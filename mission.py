from scipy.constants import g
from math import sqrt
import aircraft

class Mission:
    def __init__(self, name, aircraft, tow, range):
        self.name = name
        self.aircraft = aircraft  
        self.tow      = tow       # Takeoff weight
        self.payload  = tow / 2   # TODO
        self.range    = range
        self.dens_air = 1.225
    
    def get_thrust_zero(self):
        return self.aircraft.get_thrust_zero()
    
    def set_velo_lift_off(self):
        lift          = g * self.tow
        tmp = 2.0 * lift / (self.dens_air * self.aircraft.c_L_toff * self.aircraft.area_wing )
        velo_lift_off = sqrt(tmp)
        self.velo_lift_off = velo_lift_off

    def get_runway_length(self):
        self.set_velo_lift_off()

        velo_lift_off = self.get_velo_lift_off()
        thrust_zero   = self.get_thrust_zero()

        velo_i = []
        i = 0
        while (i < velo_lift_off): 
            velo_i.append(i)
            i+=0.5
        else: 
            velo_i.append(velo_lift_off)
        print(velo_i)

        

        return 'Lift off at {} m/s.'.format(self.velo_lift_off)
    
    def get_velo_lift_off(self):
        self.set_velo_lift_off()
        return self.velo_lift_off



    
    


        
