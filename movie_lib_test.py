from movie_lib import *


user1 = User(5)
user2 = User(12)
movie1 = Movie(3, 'Toy Story')
movie2 = Movie(9, 'Pretty Woman')

print(all_movies)
print(all_movies[3])




rating1 = Rating(user1.id, movie1.id, 4)
rating2 = Rating(user2.id, movie2.id, 1)
rating3 = Rating(user1.id, movie2.id, 3)
rating4 = Rating(user2.id, movie1.id, 1)



def test_user_creation():
    assert user1.id == 5
    assert user2.id == 12

def test_movie_creation():
    assert movie1.id == 3
    assert movie1.title == 'Toy Story'
    assert movie2.id == 9
    assert movie2.title == 'Pretty Woman'

def test_rating_creation():
    assert rating1.user_id == rating3.user_id == user1.id
    assert rating2.user_id == rating4.user_id == user2.id
    assert rating1.movie_id == rating4.user_id == movie1.id
    assert rating2.movie_id == rating3.user_id == movie2.id
    assert rating1.stars == 4
    assert rating2.stars == 1
    assert rating3.stars == 3
    assert rating4.stars == 1



def test_find_ratings_for_movie():
    # toy_story_ratings = get_ratings_for_movie(movie1.id)

    # should return a list of rating objects
    toy_story_ratings = all_movies[movie1.id].get_ratings()

    assert len(toy_story_ratings) == 2
