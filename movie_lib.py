

class Rating:

    def __init__(self, movie_id, user_id):
        self.movie_id = movie_id
        self.user_id = user_id



    def all_movie_rating(self, movie_id, movie_rating_dict):
        return movie_ratings_dict[movie_id]


    def ave_rating(self, movie_id, movie_rating_dict):
        rating_av = (sum(movie_ratings_dict[movie_id]))/(len(movie_ratings_dict[movie_id]))
        return rating_av



class Movie:

    def __init__(self, movie_id):
        self.movie_id = movie_id

    def id_for_title(self, movie_id, movie_id_dict):
        movie_name = movie_id_dict[movie_id]
        return movie_name



class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def get_user_ratings(self, user_id, user_rating_dict):
        value = user_rating_dict[user_id]
        return value


def main():
    pass



if __name__ == '__main__':
    main()
