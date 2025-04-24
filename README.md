# FIFA21 Player Data API

A simple, efficient Flask-based REST API for fetching detailed FIFA 21 player data using player IDs. Deployed on [Vercel](https://vercel.com), this API was built out of necessity during a data cleaning and preprocessing task, due to the lack of free, scalable APIs or FIFA data sources that could handle 18,000+ players.

## Why I Built This

While working on a data science project involving the FIFA21 dataset, I needed a reliable way to fetch comprehensive player data for over 18,000 individuals. Existing sources were limited, paid, or incomplete — so I created my own API to serve clean and structured data for each player, one ID at a time.

## Features

- **ID-based lookup**: Get player data via a unique player ID.
- **78 player attributes**: Each response returns detailed information including stats, physical traits, and skill ratings.
- **Fast & Lightweight**: Optimized for performance and hosted on Vercel for instant global availability.
- **Open for use**: Great for personal projects, data science workflows, or analysis pipelines.

## API Endpoint

GET https://fifa21api.vercel.app/player/{ID}

### Example Request

```bash
curl https://fifa21api.vercel.app/player/158023

Example Response

{
  "ID": 158023,
  "Name": "L. Messi",
  "Age": 33,
  "Nationality": "Argentina",
  "Overall": 93,
  ...
  "Strength": 68,
  "Aggression": 48
}

> Note: The response includes a total of 78 variables per player.



Tech Stack

Backend: Python, Flask

Deployment: Vercel

Data Source: Custom-parsed from FIFA21 dataset


Use Cases

Machine Learning preprocessing

Data cleaning and feature engineering

Sports analytics

Football player stat lookups


Future Improvements

Bulk ID requests

Pagination & filtering

Player name-based search

Swagger/OpenAPI documentation


