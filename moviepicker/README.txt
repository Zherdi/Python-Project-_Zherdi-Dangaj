The modules I used were the following:
subprocess
os
pandas
random
scrapy
re

My IDE was VS.

								**Important**

Your terminal directory should be the same as the location of both python files (main_part.py and spider_scrapy_for_movies.py).
This will insure that everything runs smoothly. 

Please run the main_part.py as the spider_scrapy_for_movies.py operates as support for the main_part.py. 


- Scope of the project -
My goal was to create a program that asks the user to select a genre of his choice(I limited the choices to 3, but of course the choices can easily expand). 
Then based on that choice the user makes, use scrapy to extract data from the website IMDB(image movie database) for the top movies for the genre that was selected. 
Then store that data in a CSV file and finally present the user with 5 random movie recommendations based on the data that was extracted.

- Full description -
The project is split in to 2 python files. One called main_part.py, which is the one that should be run by the user and one called spider_scrapy_for_movies is where the spiders funtions are.
All other files are scrapy's settings files. 

The first thing the program does is ask the user to select a genre, each genre corresponds to a number starting from 1. 
So in our case 1= is for action, 2= is for adventure and 3= is for horror etc.
The user has to put a number to indicate his preferred genre to receive recommendations. If the user doesn't provide a number, or a number within the range of available options then exception
handling is used to steer them back and to prevent program errors.

As soon as the user makes a choice, the programs prints messages to reassure the user that everything is going well, so the user doesn’t despair while the spider is crawling IMDB.
Subprocess is used to connect the two python files and provide the spider with the neccessary arguments and of course the choice of genre of the user. 

Once the users choice has been inserted then it uses that key to scrap the corresponding url. As can be seen in the dictionary that I created for the "start_urls" variable.
So for example if the user choices "horror" then the "https://www.imdb.com/search/title/?genres=Horror&explore=genres&title_type=movie&ref_=ft_movie_12" url is selected for the spider to crawl.

The next part of the code can be broken in to three parts:

1. **start_requests():**
   - Attempts to retrieve a 'genre' attribute from the object

2. **parse(response):**
   - I used a regular expression to search for the genre within the URL. I used this mostly for training purposes and to expand my intergration of modules,
 even though the information is easily retrivable from the genre variable. 
   - Collected specific movie-related data such as title, year, IMDb rating, and runtime from the HTML elements.
   - Gathered this movie-related data into a list of dictionaries called 'movie_data'.

3. **Output:**
   - Created a filename based on the unique ID (parsed genre) and saves the scraped data into a CSV file with the collected movie details.
   - The log function was used to display a message indicating the successful saving of the data into the CSV file.

Once the CSV file is created with the 50 top movies of the users preferred genre, then with the use of pandas the program reads the CSV file and presents the user with 5 random choices from the 50 items.
The module random makes that possible.

The end. 


 
  
