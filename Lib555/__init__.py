class AStable555:
    '''
    Class that represents a 555 timer configured in Astable mode
    '''

    def __init__(self, capacitor_in_ferad, resistor_1_ohms, resistor_2_ohms):
        self.capacitor_in_ferad = capacitor_in_ferad
        self.resistor_1_ohms = resistor_1_ohms
        self.resistor_2_ohms = resistor_2_ohms

    @property
    def frequency(self):
        '''Frequency in hertz'''
        res_val = self.resistor_1_ohms + (2 * self.resistor_2_ohms)
        denominator = res_val * self.capacitor_in_ferad
        return 1.44 / denominator

    @property
    def period(self):
        '''Returns period (T) in seconds, to get ms multiply this value by 1000'''
        return 1 / self.frequency

    @property
    def high_time(self):
        '''Returns high time in seconds to get ms multiply this value by 1000'''
        return 0.694 * (self.resistor_1_ohms + self.resistor_2_ohms) * self.capacitor_in_ferad

    @property
    def low_time(self):
        '''Returns low time in seconds to get ms multiply this value by 1000'''
        return 0.694 * self.resistor_2_ohms * self.capacitor_in_ferad

    @property
    def duty_cycle(self):
        return self.high_time / self.frequency * 100


class MonoStable555:
    '''
    Class that represents a 555 timer configured in monostable mode
    '''

    def __init__(self, capacitor_in_ferad, resistor_in_ohms):
        self.cap = capacitor_in_ferad
        self.resistor = resistor_in_ohms

    @property
    def output_pulse_width(self):
        '''
        Pulse width time in seconds of output pin after trigger is pulled low
        to get value in ms multiply output by 1000
        '''
        return 1.1 * self.resistor * self.cap

