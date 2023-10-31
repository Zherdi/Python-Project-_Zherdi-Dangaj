import scrapy
import pandas as pd
import re

class IMDBMoviesSpider(scrapy.Spider):
    name = "imdb_movies"

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
        if genre_match:
            unique_id = genre_match.group(1)
        else:
            unique_id = "unknown"

        movies = response.css(".lister-item-content")

        movie_data = []
        for movie in movies:
            title = movie.css("h3 a::text").get()
            year = movie.css(".lister-item-year::text").get()
            rating = movie.css(".ratings-imdb-rating strong::text").get()
            runtime = movie.css(".runtime::text").get()

            movie_data.append({
                "Title": title,
                "Year": year,
                "IMDb Rating": rating,
                "Runtime": runtime,
            })

        output_filename = f"top_{unique_id}_movie_suggestions_.csv"
        df = pd.DataFrame(movie_data)
        df.to_csv(output_filename, index=False)

        self.log(f"Saved data to {output_filename}")

if __name__ == "__main__":
    genre = input("Enter genre: ")
    process = CrawlerProcess()
    process.crawl('imdb_movies', genre=genre)
    process.start()
