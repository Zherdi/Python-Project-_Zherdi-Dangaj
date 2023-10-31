import subprocess
import os
import pandas as pd
import random


def get_movie_recommendations():
    genres = ["Action", "Adventure", "Horror"]
    print("Available Genres:")
    for index, genre in enumerate(genres, start=1):
        print(f"{index}. {genre}")

    try:
        selected_index = int(input("Enter the number of the genre: "))
        if selected_index not in range(1, len(genres) + 1):
            print("Invalid selection. Please choose a number from the available genres.")
            return
        selected_genre = genres[selected_index - 1]
        print("")
        print("Please change your terminal directory to the location of the python files(main_part.py) to mitigate any potential errors with the spider crawling")
        print("")
        print("Please give the spider some time to crawl...")
        process = subprocess.Popen(['scrapy', 'crawl', 'imdb_movies', '-a', f'genre={selected_genre}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        out, err = process.communicate()
        print(out)  
        print(err)  
        print(f"Recommendations based on {selected_genre} genre have been saved.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    get_movie_recommendations()
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # This is here so the location is used to open the csv file
    all_files = os.listdir(current_directory)

    # This will look for the CSV file that has the scraped data
    csv_files = [file for file in all_files if file.endswith(".csv")]

    if csv_files:
        selected_file = random.choice(csv_files)
        
        # Giving the user 5 random choices from the top movies of that genre
        df = pd.read_csv(os.path.join(current_directory, selected_file))
        random_rows = df.sample(5)
        print(f"Here are your recommendations, more suggestions are stored in this file '{selected_file}':")
        print(random_rows)
    else:
        print("No CSV files found, please check if the website is experiencing issues")

    
