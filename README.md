# Movie Recommendation System

A simple desktop movie recommender built with Python and Tkinter. The app lets you enter a movie title and returns five similar movie recommendations using a precomputed similarity matrix.

## Features

- Tkinter-based graphical user interface
- Recommends movies based on title similarity
- Uses `movie_list.pkl` for movie metadata
- Uses `similarity.pkl` for precomputed similarity scores
- Automatically downloads `similarity.pkl` from Google Drive if it is missing
- Shows helpful messages for empty input or unknown movie titles

## Project Files

| File | Description |
| --- | --- |
| `APP.PY` | Main Tkinter application for running the recommender. |
| `mode1.ipynb` | Notebook used for data processing/model creation. |
| `movie_list.pkl` | Pickled movie list used by the app. |
| `similarity.pkl` | Pickled similarity matrix used to generate recommendations. |
| `tmdb_5000_movies.csv` | TMDB movie dataset. |
| `tmdb_5000_credits.csv` | TMDB credits dataset. |

## Requirements

Install Python 3, then install the required packages:

```bash
pip install gdown numpy pandas
```

`tkinter` is included with most standard Python installations. If it is missing, install a Python distribution that includes Tkinter.

## How to Run

From the project folder, run:

```bash
python APP.PY
```

Then enter a movie name in the app and click **Recommend**.

## How It Works

1. The app loads `movie_list.pkl` and `similarity.pkl`.
2. The entered movie title is normalized to lowercase and matched against the movie list.
3. The app finds the selected movie's similarity scores.
4. The top five most similar movies are displayed in the recommendation box.

## Notes

- Keep `movie_list.pkl` in the same folder as `APP.PY`.
- If `similarity.pkl` is not present, the app attempts to download it automatically using `gdown`.
- Movie names must exist in the dataset for recommendations to appear.

## Author

Himanshu Gautam
