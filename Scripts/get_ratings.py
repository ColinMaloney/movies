def get_ratings(dataframe):
    '''
    This calls an api from omdbapi.com and returns a dictionary of values for the specified movies
    that were in the yearly gross profits from get_data_frames
    '''
    movie_rating_list = []
    for api_req,year in zip(dataframe.clean_movie, dataframe.year):
        movie_name = f"http://www.omdbapi.com/?t={api_req}&y={year}&apikey=b213361e"
        try:
            movie_ratings = requests.get(movie_name).json()
            movie_rating_list.append(movie_ratings)
        except ValueError:
            print('Name did not work')
    return pd.DataFrame(movie_rating_list)

ratings_df = get_ratings(overall_df)
