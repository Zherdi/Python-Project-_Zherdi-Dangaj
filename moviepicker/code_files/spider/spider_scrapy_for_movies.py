#! C:\Users\dazherdw\Desktop\Python\py files\files\venv\Scripts\python.exe
import pandas as pd
import re
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

print("Please change your directory to the location of the python files(main_part.py) to mitigate any potential errors with the spider crawling")
class IMDBMoviesSpider(scrapy.Spider):
    name = "imdb_movies"
    #Here are all the pages that the spider will crawl
    start_urls = {
        "Action": "https://www.imdb.com/search/title/?genres=Action&explore=genres&title_type=movie&ref_=ft_movie_0",
        "Adventure": "https://www.imdb.com/search/title/?genres=Adventure&explore=genres&title_type=movie&ref_=ft_movie_1",
        "Horror": "https://www.imdb.com/search/title/?genres=Horror&explore=genres&title_type=movie&ref_=ft_movie_12"
    }
    
    def start_requests(self):
        genre = getattr(self, 'genre', 'Action')
        url = self.start_urls.get(genre)
        if url:
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        genre_match = re.search(r'genres=([^&]+)', response.url)
        # I used regular expressions to get the genre from the url for demostration purposes and for training, I could use "genres" variable as well of course. 
        if genre_match:
            unique_id = genre_match.group(1)
        else:
            unique_id = "unknown"

        movies = response.css(".lister-item-content") # using this to select the desired  elements 

        movie_data = []
        for movie in movies:
            title = movie.css("h3 a::text").get()
            year = movie.css(".lister-item-year::text").get()
            rating = movie.css(".ratings-imdb-rating strong::text").get()
            runtime = movie.css(".runtime::text").get()
            # I decided that getting some extra info makes sense for my recommentation. So I will scrape the year,rating and runtime as well. 
            movie_data.append({
                "Title": title,
                "Year": year,
                "IMDb Rating": rating,
                "Runtime": runtime,
            })

        output_filename = f"top_{unique_id}_movie_suggestions_.csv"
        df = pd.DataFrame(movie_data) # here I am saving all the data the spider scraped 
        df.to_csv(output_filename, index=False)
        self.log(f"Saved data to {output_filename}")
