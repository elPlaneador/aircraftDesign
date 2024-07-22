class Aircraft:
    def __init__(self, span):
        self.span = float(span)

        if float(span) == 7.0: 
            length_chord_center = 1.60
            length_chord_tip    = 0.80
        elif float(span) == 3.5: 
            length_chord_center = 0.80
            length_chord_tip    = 0.40
        elif float(span) == 1.75: 
            length_chord_center = 0.40
            length_chord_tip    = 0.20

        length_mac               = (length_chord_center + length_chord_tip) * 0.5
        area_wing                = (length_chord_center + length_chord_tip) * 0.5 * span

        self.length_chord_center = length_chord_center
        self.length_chord_tip    = length_chord_tip
        self.length_mac          = length_mac
        self.area_wing           = round(area_wing, 3)

        self.c_L_cruise   =      0.12
        self.c_L_toff     =      0.70
        self.c_L_max      =      self.c_L_toff
        self.c_D_cruise   =      0.02
        self.c_D_toff     =      0.03

    def set_weight(self, weight):
        self.weigth = weight

    def set_thrust_zero(self, thrust):
        self.thrust_zero = thrust

    def get_thrust_zero(self):
        #if 'thrust_zero' in locals():
        if hasattr(self, 'thrust_zero'):
            return self.thrust_zero
        else:
            thrust_zero = float(input('Zero thrust:'))
            self.set_thrust_zero(thrust_zero)
        return self.thrust_zero


        

