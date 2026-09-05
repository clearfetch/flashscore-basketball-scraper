"""Fetch today's basketball games with the Apify client."""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("clearfetch/flashscore-basketball-scraper").call(run_input={"mode": "matches", "days": ["0"], "status": ["finished"]})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["startTime"], item["status"], item["home"]["name"], "vs", item["away"]["name"])
