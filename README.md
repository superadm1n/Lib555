# Lib555
I created this python package to easily use the algorithms to calculate the timing
intervals of a 555 timer circuit configured in mono stable and astable mode.

### Installing
I have not put this on PyPi but you can still install it with pip via the following command
```commandline
pip install git+https://github.com/superadm1n/Lib555
```

### Usage
Monostable 555 Timer
```python
from Lib555 import MonoStable555

my_timer = MonoStable555(capacitor_in_ferad=2, resistor_in_ohms=22000)
print(my_timer.output_pulse_width)

```

Astable 555 Timer
```python
from Lib555 import AStable555

my_timer = AStable555(capacitor_in_ferad=2, resistor_1_ohms=22000, resistor_2_ohms=22000)
print(my_timer.high_time)
print(my_timer.low_time)
print(my_timer.frequency)
```

I also created some helper functions to convert various capacitor and resistor values
```python
from Lib555.helpers import microferad_to_ferad, kohm_to_ohm, mohm_to_ohm
print(microferad_to_ferad(2.2))
print(kohm_to_ohm(2.2))
print(mohm_to_ohm(1))
```