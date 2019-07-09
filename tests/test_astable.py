from unittest import TestCase
from Lib555 import AStable555

class TestCalculations(TestCase):

    def setUp(self) -> None:
        self.obj = AStable555(capacitor_in_ferad=0.0000022, resistor_1_ohms=2200, resistor_2_ohms=2200)

    def test_frequency_calculation(self):
        self.assertEqual(99.17355371900827, self.obj.frequency)

    def test_period_calculation(self):
        # time in seconds
        self.assertEqual(self.obj.period, 0.010083333333333333)
        # conversion to ms
        self.assertEqual(self.obj.period * 1000, 10.083333333333332)

    def test_duty_cycle_calculation(self):
        pass

    def test_time_high_calculation(self):
        # time in seconds
        self.assertEqual(self.obj.high_time, 0.0067179200000000005)
        # convert to ms
        self.assertEqual(self.obj.high_time * 1000, 6.71792)

    def test_time_low_calculation(self):
        # time in seconds
        self.assertEqual(self.obj.low_time, 0.0033589600000000002)
        # convert to ms
        self.assertEqual(self.obj.low_time * 1000, 3.35896)
