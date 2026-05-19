# Netflix Data Analysis

## Project Overview
This project analyzes the Netflix dataset using Python to uncover content trends across content type, countries, genres, and release years. The code reads the compressed dataset `netflix_titles.csv.zip`, creates visualizations, saves the combined plot as `Data.png`, and prints summary counts.

---

## Tools & Technologies
- Python 3
- pandas
- matplotlib

---

## Analysis Performed
- Movies vs TV Shows comparison
- Top 5 countries with the most content
- Top 10 genres by content count
- Release year distribution of Netflix titles
- Basic null-value handling by dropping missing values for relevant columns

---

## Output
- Displays a 4-panel figure with:
  - Movies vs TV Shows bar chart
  - Top 5 countries pie chart
  - Top 10 genres bar chart
  - Release year trend line chart
- Saves the visualization as `Data.png`
- Prints summary statistics to the console

---

## Dataset
- `netflix_titles.csv.zip` (Netflix titles dataset)
- Place the ZIP file in the project folder before running the script

---

## How to Run
1. Download `netflix_titles.csv.zip` and put it inside the project folder.
2. Open `Netflix.py`.
3. Run the script with Python:
   ```bash
   python Netflix.py
   ```

---

## Notes
- The script drops rows with missing values in `type`, `country`, `listed_in`, or `release_year` before analysis.
- The genre analysis expands comma-separated values from `listed_in` to count each genre individually.

---

## Project Link
[GitHub Repository](https://github.com/kvysingh9315-stack/Netflix_data_analysing)

---

## Learning Outcome
This project demonstrates:
- Data loading and cleaning with pandas
- Plotting multiple charts with matplotlib
- Extracting dataset insights from real-world CSV data

