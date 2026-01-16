import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timedelta

# ---------- USER SETTINGS ----------
STATION = "IBOGOR129"
START_DATE = "2025-08-14"
END_DATE = "2025-12-31"

# Function to generate dates for the entire year 2025
def generate_dates(start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    delta = timedelta(days=1)
    dates = []
    while start <= end:
        dates.append(start.strftime("%Y-%m-%d"))
        start += delta
    return dates

# ---------- SETUP SELENIUM ---------
chrome_options = Options()
chrome_options.add_argument("--headless")  # remove if you want to see the browser
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Set up WebDriver with an extended timeout
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=chrome_options
)

driver.set_page_load_timeout(180)  # Increased page load timeout to 180 seconds

# Generate list of all dates in 2025
dates = generate_dates(START_DATE, END_DATE)

# Loop through all dates and scrape data
for date in dates:
    print(f"Scraping data for {date}...")
    
    # Construct the URL for the current date
    URL = f"https://www.wunderground.com/dashboard/pws/{STATION}/table/{date}/{date}/daily"
    
    try:
        # ---------- LOAD PAGE ----------
        driver.get(URL)
        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//table")))  # Wait until the table is loaded

        # ---------- SCROLL TO BOTTOM (forces load) ----------
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        
        # ---------- EXTRACT HTML ----------
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        
        # ---------- FIND MAIN TABLE (SKIP THE FIRST TABLE) ----------
        tables = soup.find_all("table")
        
        # Skip the first table and select the second one (index 1)
        main_table = tables[3]  # Skip the first table by selecting the second table
        
        if main_table is None:
            print(f"Main data table not found for {date}. Skipping...")
            continue
        
        # ---------- EXTRACT ROWS INCLUDING <th> IN <tbody> ----------
        rows = []
        for tr in main_table.find_all("tr"):
            cells = tr.find_all(["td", "th"])  # include both td and th
            if cells:
                row = [c.get_text(strip=True) for c in cells]
                rows.append(row)
        
        # ---------- HANDLE INCOMPLETE DATA ----------
        headers = [th.get_text(strip=True) for th in main_table.find_all("th")]
        expected_columns = len(headers)  # Keep the full header count
        
        for row in rows:
            while len(row) < expected_columns:
                row.append("")  # Fill missing columns with empty values
        
        # ---------- CONVERT TO DATAFRAME ----------
        df = pd.DataFrame(rows, columns=headers)
        
        # ---------- SAVE TO CSV ----------
        csv_filename = f"{STATION}_{date}_daily.csv"
        df.to_csv(csv_filename, index=False)
        print(f"Saved data for {date} to {csv_filename}")
    
    except Exception as e:
        print(f"Error scraping data for {date}: {e}")

# Close the driver after the loop
driver.quit()
