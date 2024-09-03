# Twitter Scraper with Twikit

## Description
This Python script is designed to scrape tweets based on a specific search query using the Twikit library. The script logs into a Twitter account using provided credentials and retrieves a specified number of tweets that match the query. The results are saved in a CSV file, including the username, tweet content, and user location.

## Features
- **Query-based Tweet Scraping**: Retrieves tweets based on a specified query in Spanish.
- **CSV Output**: Saves the tweets, along with user information, into a CSV file.
- **Rate Limit Handling**: Automatically handles Twitter's rate limits by waiting and resuming scraping.
- **Credential Management**: Uses a configuration file (`config.ini`) for storing Twitter login details and session management via cookies.

## Prerequisites
Ensure you have Python 3.7 or later installed on your system.

## Installation

To install the required dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Danielnvrrt/dataScrapingX.git
   cd dataScrapingX
   ```


