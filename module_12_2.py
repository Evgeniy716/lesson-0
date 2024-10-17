from unittest import TestCase
from runner_and_tournament import Runner, Tournament


class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.first = Runner("Усейн",10)
        self.second = Runner("Андрей",9)
        self.third = Runner("Ник",3)

    def test_first_tournament(self):
        tournament = Tournament(90,self.first, self.third)
        result = tournament.start()
        self.all_results['1'] = result
        self.assertTrue(result[2] == "Ник")


    def test_second_tournament(self):
        tournament = Tournament(90,self.second,self.third)
        result = tournament.start()
        self.all_results["2"] = result
        self.assertTrue(result[2] == "Ник")

    def test_third_tournament(self):
        tournament = Tournament(90, self.first, self.second, self.third)
        result = tournament.start()
        self.all_results["3"] = result
        self.assertTrue(result[3] == "Ник")

    @classmethod
    def tearDownClass(cls):
        for k, v in cls.all_results.items():
            print(f"{k}: {v}")
