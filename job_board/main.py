# from playwright.sync_api import sync_playwright
# import time
#
# def fetch_jobs(position="Lawyer", region="NCR", start=0, length=10):
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)  # use False to debug
#         page = browser.new_page()
#
#         # Step 1: Load main career page to pass Cloudflare
#         page.goto("https://csc.gov.ph/career/index.php")
#         time.sleep(5)  # wait for CF challenge to complete and cookies set
#
#         # Step 2: Now request JSON endpoint with same session
#         url = f"https://csc.gov.ph/career/inc/server_processing.php?draw=1&start={start}&length={length}&position={position}&region={region}"
#         response = page.goto(url)
#
#         if response.ok:
#             try:
#                 data = response.json()
#                 return data.get("data", [])
#             except:
#                 print("Not JSON, got:", response.status, response.text()[:200])
#         else:
#             print("Request failed:", response.status)
#         browser.close()
#
# # Example usage
# jobs = fetch_jobs()
# for job in jobs:
#     print(job)

import requests

url = 'https://csc.gov.ph/career/index.php'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)

print(response.text)

