from unittest import TestCase
from runner import Runner


class RunnerTest(TestCase):
    def test_walk(self):
        r1 = Runner("Вася")
        for i in range(10):
            r1.walk()
        self.assertEqual(r1.distance,50,f"{r1.name} прошел {r1.distance} а должен был 50")
    def test_run(self):
        r2 = Runner("Коля")
        for i in range(10):
            r2.run()
        self.assertEqual(r2.distance, 100, f"{r2.name} прошел {r2.distance} а должен был 100")

    def test_challenge(self):
        r1 = Runner("Вася")
        r2 = Runner("Коля")
        for i in range(10):
            r1.run()
            r2.walk()
        self.assertNotEqual(r1.distance,r2.distance)