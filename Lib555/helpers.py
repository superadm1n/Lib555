'''
Helper functions for quick conversion between resistor and capacitor values
'''


def microferad_to_ferad(microferad):
    return (microferad / 1000) / 1000


def kohm_to_ohm(kohm):
    return kohm * 1000


def mohm_to_ohm(mohm):
    mohm * 1000000
