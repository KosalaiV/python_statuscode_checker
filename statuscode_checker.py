import pandas as pd
import requests
from concurrent.futures import ThreadPoolExecutor

input_file = 'urls_list.xlsx'
output_file = 'failed_urls.xlsx'

# Load the Excel file containing URLs
df = pd.read_excel(input_file, header=None)

# Get the number of URLs
num_urls = len(df)
print(f"Total URLs: {num_urls}")

# Create a session for HTTP requests
session = requests.Session()

# Extract URLs from the Excel file
urls = df.iloc[:, 0].tolist()

# Lists to store failed and passed URLs
failed_urls = []
passed_urls = []

# Process each URL and handle exceptions
def process_url(url):
    try:
        # Send HEAD request and check response status
        response = session.head(url, timeout=5)
        response.raise_for_status()
        if response.status_code == 404 or response.status_code == 500:
            print(f"FAIL: {url} - {response.status_code}")
            failed_urls.append(url)
        else:
            print(f"PASS: {response.status_code}")
            passed_urls.append(url)
    except requests.exceptions.RequestException as e:
        print(f"ERROR: {url} - {e}")
        failed_urls.append(url)

# Set the number of concurrent threads
num_threads = 50

# Create a thread pool executor
with ThreadPoolExecutor(max_workers=num_threads) as executor:
    # Process URLs using the thread pool
    executor.map(process_url, urls)

# Create a DataFrame with failed URLs and save to Excel
df_failed_urls = pd.DataFrame(failed_urls)
df_failed_urls.to_excel(output_file, index=False, header=False)

# Count the number of failed URLs and passed URLs
num_failed_urls = len(failed_urls)
num_passed_urls = len(passed_urls)
print(f"Failed URLs: {num_failed_urls}")
print(f"Passed URLs: {num_passed_urls}")