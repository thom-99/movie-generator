# movie-generator
contains a python script that will generate movies based on various parameters chosen by the user and according to a modified rating system that enhances the relevance of lesser known movies.

the program is based on the IMDB public database which is of couse updated every now and then, therefore if you want to visualize movies up to date you must 
download yourself the up-to-date versions of the datasetes and run the program on those!!
download the datasets [here](https://datasets.imdbws.com/)
you'll need only two files: **title.basics.tsv.gz**  and  **title.ratings.tsv.gz**
# how it works
you can generate movies using a function called: generate_movies(Lenght,Genres,Date,Top,n) 
as you can see it has 5 argumens:

**Lenght** = can be either 'short' or 'movie' (short of course is for short-movie)

**Genres** = takes in a LIST of genres written as strings (write each genre as shown in the list of allowed genres)

**Date** = simplu input the a year (ex.1990) and only movies from that year up to now will be selected (1990-This year)

**Top** = how good do you want your movies to be? top 1%? top 20%? Just input the number as an integer (ex. Top=25)

**n**= how many movies will be generated, it is set by default at 10 and I suggest to keeping it like this for optimal visualization

you can print the result of the function and visualize the movies that have been randomly selected with your parameters, then you just have to grab some pop-corns
