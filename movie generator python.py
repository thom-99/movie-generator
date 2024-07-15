import numpy as np
import pandas as pd 

ratings = pd.read_csv('title.ratings.tsv.gz',delimiter='\t')
basics = pd.read_csv('title.basics.tsv.gz',delimiter='\t')
basics = basics.loc[basics['titleType']!='tvEpisode']

ratings['logNumVotes']=np.log(ratings['numVotes'])
ratings['logNumVotes']/=ratings['logNumVotes'].max()
ratings['averageRating']/=ratings['averageRating'].max()
ratings['newrating']=ratings['averageRating']*ratings['logNumVotes']

def filter1(lenght='movie',genres='All',date=0):
    
    #cleaning the basics dataframe out of the movies that have no 'startDate' registered
    date_presence=basics['startYear']!=r'\N'
    Basics=basics[date_presence]
    
    #setting the startdate as the minimum of all by default
    Basics['startYear'] = Basics['startYear'].astype(int)   
    if date==0:
        date=Basics['startYear'].min()
    
    #filtering now to reduce runtime
    filtered_movies=Basics.loc[(Basics['startYear']>=date) & (Basics['titleType']==lenght)]
    if genres=='All':
        return filtered_movies
    else:
        if len(genres)>3:
            return 'Error, maximum allowed: 3 genres'
        else:
            #select the rows containing the genres specified
            genre_filter = filtered_movies['genres'].apply(lambda x: all(genre in x.split(',') for genre in genres))
            filtered_movies=filtered_movies[genre_filter]
            assert filtered_movies.shape[0]!=0 
            return filtered_movies

def merge_dataframes(filtered_movies,ratings):
    rated_movies=filtered_movies.merge(ratings, how='inner',on='tconst')
    return rated_movies

def quality_filter(top_percentile, rated_movies):
    assert top_percentile<=100
    quant=1-(top_percentile/100)
    quality_filter=rated_movies['newrating'].quantile(quant)
    final_movies=rated_movies[rated_movies['newrating']>=quality_filter]
    return final_movies

def generate_movies(Lenght='movie',Genres='All',Date=0,Top=1,n=10):
    filtered_movies=filter1(Lenght,Genres,Date)
    rated_movies=merge_dataframes(filtered_movies,ratings)
    final_movies=quality_filter(Top,rated_movies)
    suggestions=final_movies.sample(n)
    relevant_info=['primaryTitle','originalTitle','startYear','runtimeMinutes','genres','newrating']
    return suggestions[relevant_info]