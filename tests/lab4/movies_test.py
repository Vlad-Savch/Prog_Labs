import unittest
from src.lab4.movies import RecommendationSystem


class TestRecommendationSystem(unittest.TestCase):
    def setUp(self):
        self.movies_file = 'test_movies.csv'
        self.history_file = 'test_history.csv'

        with open(self.movies_file, 'w', encoding='utf-8') as file:
            file.write("1,Мстители: Финал\n2,Хатико\n3,Дюна\n4,Унесенные призраками")

        with open(self.history_file, 'w', encoding='utf-8') as file:
            file.write("2,1,3\n1,4,3\n2,2,2,2,2,3")

        self.system = RecommendationSystem(self.movies_file, self.history_file)

    def test_recommendation(self):
        user_watched_movies = [2, 4]
        recommendation = self.system.recommend(user_watched_movies)
        self.assertEqual(recommendation, "Дюна")

    def test_no_recommendation(self):
        user_watched_movies = [1, 2, 3, 4]
        recommendation = self.system.recommend(user_watched_movies)
        self.assertIsNone(recommendation)


if __name__ == "__main__":
    unittest.main()
