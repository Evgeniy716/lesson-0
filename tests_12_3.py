import unittest
from unittest import TestCase
from runner_and_tournament import Runner, Tournament

class RunnerTest(TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen,"Тесты в этом кейсе заморожены")
    def test_walk(self):
        r1 = Runner("Вася")
        for i in range(10):
            r1.walk()
        self.assertEqual(r1.distance,50,f"{r1.name} прошел {r1.distance} а должен был 50")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        r2 = Runner("Коля")
        for i in range(10):
            r2.run()
        self.assertEqual(r2.distance, 100, f"{r2.name} прошел {r2.distance} а должен был 100")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        r1 = Runner("Вася")
        r2 = Runner("Коля")
        for i in range(10):
            r1.run()
            r2.walk()
        self.assertNotEqual(r1.distance,r2.distance)

class TournamentTest(TestCase):
    is_frozen =True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def setUp(self):
        self.first = Runner("Усейн",10)
        self.second = Runner("Андрей",9)
        self.third = Runner("Ник",3)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_first_tournament(self):
        tournament = Tournament(90,self.first, self.third)
        result = tournament.start()
        self.all_results['1'] = result
        self.assertTrue(result[2] == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_second_tournament(self):
        tournament = Tournament(90,self.second,self.third)
        result = tournament.start()
        self.all_results["2"] = result
        self.assertTrue(result[2] == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_third_tournament(self):
        tournament = Tournament(90, self.first, self.second, self.third)
        result = tournament.start()
        self.all_results["3"] = result
        self.assertTrue(result[3] == "Ник")

    @classmethod
    def tearDownClass(cls):
        for k, v in cls.all_results.items():
            print(f"{k}: {v}")
