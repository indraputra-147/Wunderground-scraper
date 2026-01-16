# Wunderground AWS Data Scraper

This project is designed to scrape weather data from Weather Underground for a specific weather station and date range. The script uses Selenium to automate the browser interaction, BeautifulSoup to parse the page, and Pandas to store and save the data as CSV files.

## Table of Contents
- [Project Description](#project-description)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [Script Explanation](#script-explanation)
- [License](#license)

## Project Description
This script scrapes daily weather data for a specific weather station from Weather Underground, specifically the data displayed on the station's dashboard in a table format. It supports scraping data for a range of dates and saves it in CSV format for further analysis.

### Key Features:
- **Scraping for a date range**: Data is scraped for every day between a specified start and end date.
- **Handles dynamic content**: Uses Selenium to handle JavaScript-rendered pages.
- **Flexible date range**: You can define the start and end dates of the data you want to scrape.
- **CSV export**: Saves scraped data as individual CSV files for each day.

## Requirements
Before you can use this script, make sure you have the following dependencies installed:

- Python 3.x
- Selenium
- BeautifulSoup4
- Pandas
- WebDriver Manager (for automatic installation of ChromeDriver)
- Chrome or Chromium (Selenium requires a browser to run)

You can install the required Python libraries by running:

```bash
pip install selenium beautifulsoup4 pandas webdriver-manager

Make sure that Google Chrome is installed on your machine, as the script uses ChromeDriver for automation.

## Setup

1. Clone the repository to your local machine:
2. Navigate to the project folder:
3. Install the required libraries using pip:
4. You can adjust the STATION, START_DATE, and END_DATE variables in the script to scrape data for your desired weather station and date range.

## Usage
1. Open the scrape_weather.py file.
2. Modify the STATION, START_DATE, and END_DATE variables to specify the weather station and the range of dates for which you want to scrape data.
Example:
3. Run the script:
4. The script will scrape the data for each date in the specified range and save each day's data to a separate CSV file in the format STATION_DATE_daily.csv.
Example:

## Script Explanation

1. Selenium Setup: The script uses Selenium to control a Chrome browser instance. It opens the weather station's dashboard for each date in the specified range.
2. Page Handling: It waits for the table to load and scrolls to the bottom of the page to ensure all data is loaded.
3. HTML Parsing: BeautifulSoup is used to parse the page source and extract the relevant table data.
4. Data Extraction: The script identifies and extracts the rows and columns from the table, ensuring that each row has the correct number of columns.
5. Data Saving: The extracted data is saved as a CSV file using Pandas.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
