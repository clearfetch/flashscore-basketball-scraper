#!/usr/bin/env bash
# Fetch today's basketball games and print the raw JSON.
curl -X POST "https://api.apify.com/v2/acts/clearfetch~flashscore-basketball-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"mode": "matches", "days": ["0"], "status": ["finished"]}'
