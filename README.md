# Flashscore Basketball Scraper - Live Scores, Quarters & Stats

Get basketball data from Flashscore as clean JSON: fixtures for the days you choose, live scores, final results,
and the score in every quarter and overtime period. Per game you can also pull the full statistics sheet, from
field-goal percentages to rebounds, assists and turnovers. NBA, EuroLeague, NCAA and every domestic league
Flashscore covers. No login, no API key and no proxy.

## What data you get

**Games mode** returns one row per game:

- **Quarter-by-quarter scores** that add up to the final score, plus any overtime periods as their own entries.
- **Status resolved from Flashscore's own stage codes**, not guessed: scheduled, live, finished, postponed,
  cancelled or interrupted, plus `stageDetail` naming the exact stage (`FIRST_QUARTER`, `THIRD_QUARTER`,
  `EXTRA_TIME`, `AWARDED`).
- **Competition**: name, country, phase such as Play Offs, plus IDs and the Flashscore URL.
- **Teams**: name, Flashscore team ID and slug, three-letter code and logo.
- **`raw`**: all 43 original feed fields for the game, so nothing is lost if you need something we did not map.

**Game details mode** takes match IDs and returns, per game:

- **Period scores** straight from the source.
- **Full statistics** split by period and group: field goals attempted, made and percentage, three pointers,
  free throws, offensive and defensive rebounds, assists, turnovers, steals and blocks. 100 rows for the
  example below.
- **Head to head**: recent form for both teams and their previous meetings.

## How to use

1. Choose **Games** mode and set **Days** (0 is today, -1 yesterday, 1 tomorrow; add several for a range).
2. Optionally narrow by status, by country, or with a regular expression on the competition name such as `nba`.
3. Run it, then export as JSON, CSV or Excel, or read it from the API. For a deeper look at one game, run the
   Actor again in **Game details** mode with the `matchId` values you got back.

## Input

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `mode` | string | `matches` | `matches` for fixtures, live scores and results; `matchDetails` for period scores, statistics and head to head. |
| `days` | array | `["0"]` | Day offsets from today, from -7 to 7. Several entries are fetched in one run and deduplicated. |
| `status` | array | all | Keep only `scheduled`, `live`, `finished`, `postponed`, `cancelled` or `interrupted`. |
| `countries` | array | all | Keep only these countries or regions, for example USA, Spain, Europe. |
| `tournamentFilter` | string | — | Case-insensitive regular expression on the full competition name, e.g. `euroleague|eurocup`. |
| `matchIds` | array | — | Details mode: match IDs such as `nm66nX6U`, or full `flashscore.com/match/...` URLs. |
| `details` | array | all three | Details mode: `summary`, `statistics`, `h2h`. |
| `maxItems` | integer | `0` | Stop after this many rows; 0 means no limit. |
| `maxConcurrency` | integer | `5` | Parallel requests in details mode. |
| `timeoutSecs` | integer | `30` | Per-request timeout. |
| `token` | string | — | Advanced. Overrides the feed signature, which the Actor otherwise discovers by itself. |
| `proxyConfiguration` | object | off | Optional. Not needed in normal use. |

## Output example

One game from a **games** run (the `raw` object with all 43 feed fields is omitted here for readability):

```json
{
  "matchId": "nm66nX6U",
  "url": "https://www.flashscore.com/match/nm66nX6U/",
  "sport": "basketball",
  "status": "finished",
  "stage": "finished",
  "stageDetail": "FINISHED",
  "stageCode": 3,
  "stageDetailCode": 3,
  "startTime": "2026-09-04T23:30:00.000Z",
  "lastUpdate": "2026-09-05T00:57:35.000Z",
  "note": null,
  "tournament": {
    "name": "LNB",
    "fullName": "PARAGUAY: LNB - Clausura",
    "country": "Paraguay",
    "phase": "Clausura",
    "id": "dddz4h2L",
    "stageId": "SK32QUiJ",
    "path": "/basketball/paraguay/lnb/",
    "url": "https://www.flashscore.com/basketball/paraguay/lnb/"
  },
  "home": {
    "name": "Capiata Bulls",
    "fullName": "Capiata Bulls",
    "id": "OSTxMXDD",
    "slug": "capiata-bulls",
    "url": "https://www.flashscore.com/team/capiata-bulls/OSTxMXDD/",
    "code": "CAP",
    "image": null
  },
  "away": {
    "name": "San Alfonzo",
    "fullName": "San Alfonzo",
    "id": "jZLOqy6K",
    "slug": "san-alfonzo",
    "url": "https://www.flashscore.com/team/san-alfonzo/jZLOqy6K/",
    "code": "SAN",
    "image": "https://static.flashscore.com/res/image/data/Mw8KczVH-dINMEfSG.png"
  },
  "score": {
    "home": 89,
    "away": 126,
    "quarters": [
      {
        "period": "Q1",
        "home": 20,
        "away": 23
      },
      {
        "period": "Q2",
        "home": 27,
        "away": 33
      },
      {
        "period": "Q3",
        "home": 21,
        "away": 44
      },
      {
        "period": "Q4",
        "home": 21,
        "away": 26
      }
    ],
    "overtime": null
  },
  "winner": "away",
  "inPlay": false,
  "ok": true,
  "dayOffset": 0,
  "scrapedAt": "2026-09-05T14:39:09.824Z"
}
```

A **game details** item, trimmed to the first statistics rows:

```json
{
  "matchId": "nm66nX6U",
  "url": "https://www.flashscore.com/match/nm66nX6U/",
  "sport": "basketball",
  "ok": true,
  "summary": {
    "periods": [
      {
        "period": "1st Quarter",
        "home": 20,
        "away": 23
      },
      {
        "period": "2nd Quarter",
        "home": 27,
        "away": 33
      },
      {
        "period": "3rd Quarter",
        "home": 21,
        "away": 44
      },
      {
        "period": "4th Quarter",
        "home": 21,
        "away": 26
      }
    ]
  },
  "statistics": [
    {
      "period": "Match",
      "group": "Scoring",
      "name": "Field goals attempts",
      "home": "77",
      "away": "86"
    },
    {
      "period": "Match",
      "group": "Scoring",
      "name": "Field goals made",
      "home": "32",
      "away": "51"
    },
    {
      "period": "Match",
      "group": "Scoring",
      "name": "Field goals %",
      "home": "41.56%",
      "away": "59.3%"
    },
    {
      "period": "Match",
      "group": "Scoring",
      "name": "2-point field goals attempts",
      "home": "43",
      "away": "62"
    }
  ],
  "scrapedAt": "2026-09-05T14:39:23.412Z"
}
```

A game that cannot be found, or has no data yet, produces `{ "matchId": "...", "ok": false, "error": "..." }`
and is not charged.

## Pricing

- **$0.001 per game** in games mode. A normal day is a few hundred games worldwide, so well under a dollar for
  everything, or a few cents once you filter by country or competition.
- **$0.01 per game** in details mode, whatever number of sections you request. Period scores, the whole
  statistics sheet and both teams' recent form count as one charge.
- Games that fail or have no data are free. Runs on the Apify free plan.

Paid Apify plans pay less: 10% off on Bronze, 20% on Silver and 30% on Gold and higher tiers.

Apify also charges a run-start fee of $0.00005 per started GB of allocated memory (minimum one event), including runs that produce no chargeable results.

## Use cases

- **Betting and trading models**: build a history of quarter splits, shooting percentages and pace, then keep it
  current with a scheduled daily run.
- **Live scoreboards and bots**: poll games mode for in-play scores and push updates to a site, app or Discord.
- **Fantasy basketball**: pull box-score style statistics per game.
- **Media and newsletters**: generate daily results digests with the quarter breakdown.
- **Research and machine learning**: label datasets across leagues, including overtime games and abandoned ones.
- **AI agents**: give an assistant a tool that answers "what was the score by quarter in last night's games".

## Integrations

```bash
curl -X POST "https://api.apify.com/v2/acts/clearfetch~flashscore-basketball-scraper/run-sync-get-dataset-items?token=YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"days": ["0"], "status": ["finished"]}'
```

```python
from apify_client import ApifyClient
client = ApifyClient("YOUR_TOKEN")
run = client.actor("clearfetch/flashscore-basketball-scraper").call(
    run_input={"days": ["0"], "status": ["finished"]}
)
for game in client.dataset(run["defaultDatasetId"]).iterate_items():
    quarters = " ".join(f"{q['home']}-{q['away']}" for q in game["score"]["quarters"] or [])
    print(game["home"]["name"], game["score"]["home"], "-", game["score"]["away"], game["away"]["name"], quarters)
```

Works with the Apify integrations for n8n, Make, Zapier, Google Sheets, Slack and webhooks, with scheduled runs,
and with AI agents through the Apify MCP server.

## FAQ

**Do I need a proxy?** No. The feed answers ordinary datacenter requests. A proxy input exists if you want one.

**Do I need a Flashscore account?** No. Nothing here requires a login or a cookie.

**Do the quarter scores always add up?** Yes, and the Actor's tests assert it on every finished game in the
fixture set. Overtime periods are returned separately so you can tell regulation from what followed.

**How fresh is the data?** Each run reads the feed live, so games in progress carry their current score.
Schedule a run every few minutes if you need a running scoreboard.

**What if Flashscore changes its feed signature?** The Actor discovers the current signature from the site on
every run and falls back to a known value, so a rotation does not break it. The `token` input is a last resort.

**Which sports does this cover?** Basketball. The same feed carries other sports; ask if you want one added.

**Is this legal?** It reads the same public endpoints a browser reads, with no login and no personal data.
Scores and results are facts. You are responsible for how you use the data, including any redistribution.

## More tools from clearfetch

- [Flashscore Football Scraper](https://apify.com/clearfetch/flashscore-football-scraper): fixtures, live scores and results from every league
- [Flashscore Tennis Scraper](https://apify.com/clearfetch/flashscore-tennis-scraper): ATP, WTA and Challenger matches with point by point
- [Flashscore Baseball Scraper](https://apify.com/clearfetch/flashscore-baseball-scraper): MLB, NPB and KBO with inning-by-inning line scores
- [Flashscore Hockey Scraper](https://apify.com/clearfetch/flashscore-hockey-scraper): NHL, KHL and every league, by period

## Changelog

- **1.0.1** (2026-09) — match links copied from the browser work in details mode. Flashscore's current links
  carry the match ID in `?mid=`, after team names that were being read as the ID; a link with no ID in it is now
  skipped with a message saying where to find one.
- **1.0.0** (2026-09) — first release: games mode with day ranges and status, country and competition filters;
  details mode with period scores, statistics and head to head; status resolved from Flashscore's own stage
  codes; automatic feed-signature discovery.
