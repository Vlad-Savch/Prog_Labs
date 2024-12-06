import csv


class Movie:
    def __init__(self, movie_id, title):
        self.movie_id = int(movie_id)
        self.title = title


class UserHistory:
    def __init__(self, watched_movies):
        self.watched_movies = list(map(int, watched_movies))


class RecommendationSystem:
    def __init__(self, movies_file, history_file):
        self.movies = self.load_movies(movies_file)
        self.history = self.load_history(history_file)

    def load_movies(self, filepath):
        movies = {}
        with open(filepath, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                movie_id, title = row
                movies[int(movie_id)] = Movie(movie_id, title)
        return movies

    def load_history(self, filepath):
        history = []
        with open(filepath, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                history.append(UserHistory(row))
        return history

    def recommend(self, user_watched_movies):
        user_history = set(user_watched_movies)
        recommendations = {}

        for other_history in self.history:
            other_watched = set(other_history.watched_movies)
            common_movies = user_history.intersection(other_watched)

            if len(common_movies) >= len(user_history) / 2:
                for movie in other_watched - user_history:
                    if movie in recommendations:
                        recommendations[movie] += 1
                    else:
                        recommendations[movie] = 1

        if not recommendations:
            return None

        recommended_movie_id = max(recommendations, key=recommendations.get)
        return self.movies[recommended_movie_id].title


if __name__ == "__main__":
    system = RecommendationSystem('movies.csv', 'history.csv')
    user_input = input("Введите просмотренные фильмы через запятую: ").split(',')
    user_watched_movies = list(map(int, user_input))

    recommendation = system.recommend(user_watched_movies)
    if recommendation:
        print("Рекомендуемый фильм:", recommendation)
    else:
        print("Нет рекомендаций")
