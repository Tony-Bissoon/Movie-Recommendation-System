# FILL IN ALL THE FUNCTIONS IN THIS TEMPLATE
# MAKE SURE YOU TEST YOUR FUNCTIONS WITH MULTIPLE TEST CASES
# ASIDE FROM THE SAMPLE FILES PROVIDED TO YOU, TEST ON YOUR OWN FILES

# WHEN DONE, SUBMIT THIS FILE TO AUTOLAB

from collections import defaultdict
from collections import Counter

# YOU MAY NOT CODE ANY OTHER IMPORTS

# ------ TASK 1: READING DATA  --------

# 1.1
def read_ratings_data(f):
    # parameter f: movie ratings file name f (e.g. "movieRatingSample.txt")
    # return: dictionary that maps movie to ratings
    # WRITE YOUR CODE BELOW
    movie_ratings_dict = {}
    with open(f, "r", encoding = 'utf-8') as file:
        for line in file: 
            parts = line.strip().split('|')
            if len(parts) == 3:
                movie, rating, _ = parts 
                rating = float(rating)

                if movie not in movie_ratings_dict:
                    movie_ratings_dict[movie] = []
                movie_ratings_dict[movie].append(rating)
    print(movie_ratings_dict)
    return movie_ratings_dict
                    
    #pass
    

# 1.2
def read_movie_genre(f):
    # parameter f: movies genre file name f (e.g. "genreMovieSample.txt")
    # return: dictionary that maps movie to genre
    # WRITE YOUR CODE BELOW

    movie_genre_dict = {}
    with open(f, "r", encoding = 'utf-8') as file:
        for line in file: 
            parts = line.strip().split('|')
            if len(parts) == 3:
                genre, _ , movie = parts 
                

                movie_genre_dict[movie] =genre
    print(movie_genre_dict)
    return movie_genre_dict 

    #pass


# ------ TASK 2: PROCESSING DATA --------

# 2.1
def create_genre_dict(d):
    # parameter d: dictionary that maps movie to genre
    # return: dictionary that maps genre to movies
    # WRITE YOUR CODE BELOW

    genre_dict = {}
    for movie, genre in d.items():
        if genre not in genre_dict:
            genre_dict[genre] = []
        genre_dict[genre].append(movie)
    
    return genre_dict

    # pass
    
# 2.2
def calculate_average_rating(d):
    # parameter d: dictionary that maps movie to ratings
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    average_ratings = {}
    for movie, ratings in d.items():
        if ratings: 
            average_ratings[movie] = round(sum(ratings) / len(ratings), 2)
    return average_ratings
    #pass
    
# ------ TASK 3: RECOMMENDATION --------

# 3.1
def get_popular_movies(d, n=10):
    # parameter d: dictionary that maps movie to average rating
    # parameter n: integer (for top n), default value 10
    # return: dictionary that maps movie to average rating, 
    #         in ranked order from highest to lowest average rating
    # WRITE YOUR CODE BELOW
    sorted_movies = sorted(d.items(), key = lambda x: x[1], reverse= True)
    top_n_movies= dict(sorted_movies[:n])
    return top_n_movies
    #pass
    
# 3.2
def filter_movies(d, thres_rating=3):
    # parameter d: dictionary that maps movie to average rating
    # parameter thres_rating: threshold rating, default value 3
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    # pass
    filtered_movies = {}
    for movie, rating in d.items():
        if rating >= thres_rating:
            filtered_movies[movie] = rating
    return filtered_movies
    
# 3.3
def get_popular_in_genre(genre, genre_to_movies, movie_to_average_rating, n=5):
    # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    # pass
    movies_in_genre = genre_to_movies.get(genre, [])
    rated_movies = {}
    for movie in movies_in_genre:
        if movie in movie_to_average_rating:
            rated_movies[movie] = movie_to_average_rating[movie]

    sorted_movies = sorted(rated_movies.items(), key=lambda x: x[1], reverse=True)
    top_n_movies = dict(sorted_movies[:n])
    return top_n_movies        
    
# 3.4
def get_genre_rating(genre, genre_to_movies, movie_to_average_rating):
   
    # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # return: average rating of movies in genre
    # WRITE YOUR CODE BELOW
    movies_in_genre = genre_to_movies.get(genre, [])
    total_rating = 0
    count = 0
    for movie in movies_in_genre:
        if movie in movie_to_average_rating:
            total_rating += movie_to_average_rating[movie]
            count += 1
    return round(total_rating / count, 2) if count > 0 else None
    pass

    
# 3.5
def genre_popularity(genre_to_movies, movie_to_average_rating, n=5):
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps genre to average rating
    # WRITE YOUR CODE BELOW
    genre_rating = {}
    for genre in genre_to_movies:
        avg_rating = get_genre_rating(genre, genre_to_movies, movie_to_average_rating)
        if avg_rating is not None:
            genre_rating[genre] = avg_rating
    sorted_genre = sorted(genre_rating.items(), key=lambda x: x[1], reverse=True)
    top_n_genre = dict(sorted_genre[:n])
    return top_n_genre
    pass


# ------ TASK 4: USER FOCUSED  --------

# 4.1
def read_user_ratings(f):
    # parameter f: movie ratings file name (e.g. "movieRatingSample.txt")
    # return: dictionary that maps user to list of (movie,rating)
    # WRITE YOUR CODE BELOW
    user_ratings_dict = {}
    with open(f, "r", encoding = 'utf-8') as file:
        for line in file: 
            parts = line.strip().split('|')
            if len(parts) == 3:
                movie, rating, user_id = parts 
                rating = float(rating)
                user_id = int(user_id)


                if user_id not in user_ratings_dict:
                    user_ratings_dict[user_id] = []
                user_ratings_dict[user_id].append((movie, rating))
    sorted_user_ratings = dict(sorted(user_ratings_dict.items()))
    return sorted_user_ratings
   
    pass
    
# 4.2
def get_user_genre(user_id, user_to_movies, movie_to_genre):
    # parameter user_id: user id
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # return: top genre that user likes
    # WRITE YOUR CODE BELOW
    if user_id not in user_to_movies:
        return None
    
    genre_ratings = {}
    genre_count = {}

    for movie, rating in user_to_movies[user_id]:
        if movie in movie_to_genre:
            genre = movie_to_genre[movie]
            if genre not in genre_ratings:
                genre_ratings[genre] = 0
                genre_count[genre] = 0
            genre_ratings[genre] += rating
            genre_count[genre] += 1
        
    genre_avg = {genre: genre_ratings[genre] / genre_count[genre] for genre in genre_ratings}
    top_genre = max(genre_avg, key=genre_avg.get, default=None)
    return top_genre
    pass
    
# 4.3    
def recommend_movies(user_id, user_to_movies, movie_to_genre, movie_to_average_rating):
    # parameter user_id: user id
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # parameter movie_to_average_rating: dictionary that maps movie to average rating
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    top_genre = get_user_genre(user_id, user_to_movies, movie_to_genre)
    if not top_genre:
        return {}
    
    movies_in_genre = [movie for movie, genre in movie_to_genre.items() if genre == top_genre]

    user_rated_movies = {movie for movie, _ in user_to_movies.get(user_id, [])}
    unrated_movies = {movie: rating for movie, rating in movie_to_average_rating.items() if movie in movies_in_genre and movie not in user_rated_movies}
    sorted_recommendations = sorted(unrated_movies.items(), key=lambda x: x[1], reverse=True)
    recommend_movies = dict(sorted_recommendations)
    return recommend_movies
    pass

# -------- main function for your testing -----
def main():
    # write all your test code here
    # this function will be ignored by us when grading
    #pass
    print("Question 1: ")
    print("1.1: ")
    movie_ratings = read_ratings_data("movieRatingSample.txt")
    print("1.2: ")
    movie_genre = read_movie_genre("genreMovieSample.txt")

    print("Question 2: ")
    print("2.1: ")
    genre_dict = create_genre_dict(movie_genre)
    print(genre_dict)
    print("2.2: ")
    avg_ratings = calculate_average_rating(movie_ratings)
    print(avg_ratings)

    print("Question 3: ")
    print("Question 3.1: ")
    top_movies = get_popular_movies(avg_ratings, 10)
    print(top_movies)
    print("Question 3.2: ")
    filtered_movies = filter_movies(avg_ratings, 4)
    print(filtered_movies)
    print("Question 3.3: ")
    top_genre_movies = get_popular_in_genre("Comedy", genre_dict, avg_ratings, 5)
    print(top_genre_movies)
    print("Question 3.4: ")
    genre_rating = get_genre_rating("Comedy", genre_dict, avg_ratings)
    print(genre_rating)
    print("Question 3.5: ")
    top_genre = genre_popularity(genre_dict, avg_ratings, 5)
    print(top_genre)    

    print("Question 4: ")
    print("Question 4.1: ")
    user_ratings = read_user_ratings("movieRatingSample.txt")
    print(user_ratings)
    print("Question 4.2: ")
    user_genre = get_user_genre(1, user_ratings, movie_genre)
    print(user_genre)
    print("Question 4.3: ")
    recommended_movies = recommend_movies(1, user_ratings, movie_genre, avg_ratings)
    print(recommended_movies)



    
    
    
# DO NOT write ANY CODE (including variable names) outside of any of the above functions
# In other words, ALL code your write (including variable names) MUST be inside one of
# the above functions
    
# program will start at the following main() function call
# when you execute hw1.py
main()

    