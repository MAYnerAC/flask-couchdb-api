def create_movie_data(title, year, genre, director, rating, duration, status="active"):
    return {
        'title': title,
        'year': year,
        'genre': genre,
        'director': director,
        'rating': rating,
        'duration': duration,
        'status': status
    }
