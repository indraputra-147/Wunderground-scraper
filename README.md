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
