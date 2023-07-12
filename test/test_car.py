import unittest
from datetime import datetime, timedelta


class Car:
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.needs_battery_service() or self.needs_engine_service()

    def needs_battery_service(self):
        return self.last_service_date < datetime.today() - timedelta(days=365 * 3)

    def needs_engine_service(self):
        return self.current_mileage - self.last_service_mileage > 


class TestCar(unittest.TestCase):
    def setUp(self):
        self.today = datetime.today().date()

    def test_needs_service_battery(self):
        car = Car(self.today - timedelta(days=365 * 3), 0, 0)
        self.assertTrue(car.needs_service())

    def test_does_not_need_service_battery(self):
        car = Car(self.today - timedelta(days=365), 0, 0)
        self.assertFalse(car.needs_service())

    def test_needs_service_engine(self):
        car = Car(self.today, 30001, 0)
        self.assertTrue(car.needs_service())

    def test_does_not_need_service_engine(self):
        car = Car(self.today, 30000, 0)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
