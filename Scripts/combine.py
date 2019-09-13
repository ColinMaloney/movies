def get_tomato_score(row):
    try:
        tomato_val = [x.get('Value') for x in row if x.get('Source') == 'Rotten Tomatoes'][0]
        tomato_val = tomato_val.replace('%','')
        return int(tomato_val)
    except:
        return (None)

def imdb_clean(row):
    try:
        return float(row) * 10
    except:
        return(None)


def get_meta_score(row):
    try:
        return int(row)
    except:
        return(None)

ratings_df['Rotten_Score'] = ratings_df.Ratings.map(get_tomato_score)
ratings_df['Metacritic_Score'] = ratings_df.Metascore.map(get_meta_score)
ratings_df['Imdb_Score'] = ratings_df.imdbRating.map(imdb_clean)
joining_df = ratings_df[['Title','Rotten_Score','Metacritic_Score','
                            Imdb_Score']].set_index('Title')


def clean_movie_names(dataframe):
    '''
    The movie names were coming back with some no ascii characters so this function cleans up
    those characters and adds an apostrophe where those characters were located
    '''
    overall_df['clean_movie'] = overall_df.Movie.map(lambda x: x.replace("â", "'"))
    return overall_df

overall_df = clean_movie_names(overall_df)

joined_df = overall_df[['Worldwide Box Office','Domestic Box Office',
                        'International Box Office','DomesticShare','year',
                        'clean_movie']].set_index('clean_movie')

final_df = joined_df.join(joining_df,on='clean_movie',how='inner')
final_df = final_df.dropna()
