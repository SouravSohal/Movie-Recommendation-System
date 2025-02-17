# Movie Recommendation System (IMDb Scraper)

## Overview
This Python script scrapes IMDb's **Top 250 Movies** list and provides personalized movie recommendations based on a user-input movie. If the movie exists in the Top 250 list, it fetches **top 4 recommended movies** based on the director's other works.

## Features
- Scrapes IMDb's **Top 250 Movies** list.
- Searches for a movie entered by the user.
- Retrieves **the director's other movies** as recommendations.
- Uses **requests** and **BeautifulSoup** for web scraping.

## Prerequisites
Before running the script, ensure you have the following installed:

- Python 3.x
- Required Python libraries:
  ```bash
  pip install requests beautifulsoup4
  ```

## How to Run the Script
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/movie-recommender.git
   cd movie-recommender
   ```
2. Run the script:
   ```bash
   python movie_recommender.py
   ```
3. Enter a movie name when prompted.
4. If the movie is found in IMDb's Top 250 list, the script will display **top 4 movie recommendations** based on the director's other works.

## Code Explanation
- Fetches IMDb's **Top 250 Movies** from [IMDb Top 250](https://www.imdb.com/chart/top/).
- Searches for the user-input movie in the list.
- Extracts the director’s IMDb page from the movie details.
- Scrapes the **top 4 movies** directed by the same director.
- Displays the recommended movies.

## Example Output
```
Enter the name of the Movie: The Shawshank Redemption
Your top 4 movies recommendation based on the entered movie The Shawshank Redemption are:
1. The Green Mile
2. Mystic River
3. Million Dollar Baby
4. Gone Baby Gone
```

## Limitations
- Only works with IMDb's **Top 250 Movies**.
- IMDb **may update its website structure**, causing changes in scraping logic.
- Works on **static HTML** (does not handle JavaScript-rendered content).

## License
This project is open-source under the MIT License.

## Contributing
Feel free to contribute by submitting a pull request or suggesting improvements!

## Author
[Your Name](https://github.com/SouravSohal)

