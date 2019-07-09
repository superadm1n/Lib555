from unittest import TestCase
from Lib555 import MonoStable555


class TestCalculations(TestCase):

    def setUp(self) -> None:
        self.obj = MonoStable555(capacitor_in_ferad=0.0000022, resistor_in_ohms=2200)

    def test_output_pulse_width_calculation(self):
        self.assertEqual(self.obj.output_pulse_width, 0.005324000000000001)
        # convert to ms
        self.assertEqual(self.obj.output_pulse_width * 1000, 5.324000000000001)
