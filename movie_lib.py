import csv


all_movies = {}
all_users = {}


#--------



class User:
    def __init__(self, user_id):
        self.id = user_id
        all_users[self.id] = self
        self.ratings = {}


    def add_ratings(self, rating):
        self.ratings[rating.movie_id] = rating

    def get_ratings(self):
        return self.ratings.values()



    def __str__(self):
        return 'Rating(user_id={}, movie_id={}, stars={})'.format(self.user_id, self.movie_id, self.stars)

    def __repr__(self):
        return self.__str__()

class Movie:
    def __init__(self, movie_id, title):
        self.id = int(movie_id)
        self.title = title
        all_movies[self.id] = self #when we create a movie object it will go in the all_movies dictionary
        self.ratings = {} # key: user_id, value: Rating object

    def add_ratings(self, rating):
        self.ratings[rating.user_id] = rating.stars

    def get_ratings(self):
        return self.ratings.values() #will give us a dict of just the ratings for each movie while striping the user id



    def ave_rating(self):
        return sum(self.ratings.values()) / len(self.ratings.values())

    def get_movie_title(self):
        return all_movies[self.id].title


    def __str__(self):
        return 'Movie(movie_id={}, title={})'.format(self.id, repr(self.title))

    def __repr__(self):
        return self.__str__()


class Rating:
    def __init__(self, user_id, movie_id, stars):
        self.user_id = user_id
        self.movie_id = movie_id
        self.stars = stars

        all_movies[self.movie_id].add_ratings(self)

        all_users[self.user_id].add_ratings(self)



    def __str__(self):
        return 'Rating(user_id={}, movie_id={}, stars={})'.format(self.user_id, self.movie_id, self.stars)

    def __repr__(self):
        return self.__str__()

# ---------

def data():
    with open('u.data') as f:
        reader = csv.DictReader(f, fieldnames=['user_id', 'movie_id', 'stars'], delimiter='\t')
        for row in reader:
            Rating(int(row['user_id']), int(row['movie_id']), int(row['stars']))

def items():
    with open('u.item', encoding='latin_1') as f:
        reader = csv.DictReader(f, fieldnames=['movie_id', 'movie_title'], delimiter='|')
        for row in reader:
            Movie(int(row['movie_id']), row['movie_title'])

def users():
    with open('u.user') as f:
        reader = csv.DictReader(f, fieldnames=['user_id'], delimiter='|')
        for row in reader:
            User(int(row['user_id']))

#-------------



def top_rated(x=3,all_movies=all_movies):
    top_rated_movies = {}
    listed = int(input("Enter the number of movies to be listed:  "))
    for x in all_movies:
        if len(all_movies[x].get_ratings()) > 10:
            top_movies[x] = all_movies[x].ave_rating()
    top_rated_movies = sorted(top_rated_movies.items(), key=lambda c: c[1], reverse=True)
    # print('here')
    for item in top_movies[:listed]:
        print((all_movies[item[0]].title))
    return main()



#------------

def not_yet_rated(user, all_movies=all_movies, all_users=all_users):
    safe_dict = all_movies.copy()
    for key in all_users[user].ratings:
        del safe_dict[key]
    movie_suggested = top_rated(5, safe_dict)



#---------
def main():

    items()
    users()
    data()

    start = input("Please enter one of the following options. \n For a list of the top rated movies, enter 1. \n For a list of the top rated movies you have not yet rated, enter 2. \n to quit enter q. \n Enter 1, 2 or q here: ")
    if start == '1':
        top_rated()
    elif start == '2':
        user = input("Please enter reviewer id: ")
        user = int(user)
        not_yet_rated(user)
    elif start == 'q':
        quit()
    else:
        print("Not a valid entry.")
        return main()


if __name__ == '__main__':
    main()
