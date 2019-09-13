# Getting data from gross profits and movie ratings to find out if the ratings of the movies have any statistical affect on the movie's grossing profits. 

*To see how each site caculates their scores for the movies, check out the Wiki page in this repository.
#Background:
I have always been intrigued by how movie ratings could affect how a movie does in the Box Office.  You would think that a good movie is going to get a good rating score and this would make people want to see the movie.  I wanted to see if I could determine this correlation.  I first started by finding some sites on the Internet that had good data for me to use.  The first was www.the-numbers.com.  This allowed me to scrape the data from the tables of the yearly grossing top 100 for a given year. I then had to clean some of the movie names, especially the one's with and aphostrophe.  From here I was able to find and API with movie information from http://www.omdbapi.com/.  I then sent each movie in with the attached year to get back my ratings from Imdb, Rotten Tomatoes, and Meatcritic.  This data was extracted and put into one usable DataFrame using Pandas. 


