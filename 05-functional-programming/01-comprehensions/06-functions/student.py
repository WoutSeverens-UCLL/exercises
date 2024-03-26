

def movie_count(movies, director):
    return len([movie.director for movie in movies if movie.director == director])

def longest_movie_runtime_with_actor(movies, actor):
    return max([movie.runtime for movie in movies if actor in movie.actors])

def has_director_made_genre(movies, director, genre):
    return any([movie.director for movie in movies if genre in movie.genres and director == movie.director])

def is_prime(n):
    return n > 1 and all(n % x != 0 for x in range(2, n))

def is_increasing(ns):
    return all(x <= y for x,y in zip(ns, ns[1:]))

def count_matching(xs, ys):
    return sum(1 for x, y in zip(xs, ys) if x == y)

def weighted_sum(ns, weight):
    return sum(x * y for x, y in zip(ns, weight))

def alternating_caps(string):
    return ''.join([char.upper() if index % 2 == 0 else char.lower() for index, char in enumerate(string)])

def find_repeated_words(sentence):
    import re 
    words = [word.lower() for word in re.findall('[a-zA-Z]+', sentence)]
    return {x for x, y in zip(words, words[1:]) if x == y }