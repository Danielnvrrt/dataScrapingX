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
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

### Create a `config.ini` File
Create a `config.ini` file in the root directory of your project with the following content:

```ini
[X]
username = your_twitter_username
email = your_email_address
password = your_password
```
Replace `your_twitter_username`, `your_email_address`, and `your_password` with your actual Twitter credentials.

## Set the Query and CSV Filename
Edit the script if necessary to update the `MINIMUM_TWEETS`, `QUERY` and `CSV_NAME` variables according to your needs:
```python
MINIMUM_TWEETS = 1000
QUERY = 'query'
CSV_NAME = 'name.csv'
```

## Usage
### First-time Execution
The first time you run the script, it will log in using your credentials and save the session cookies in a file named `cookies.json`. This will help in subsequent logins without needing to re-enter credentials.

Run the script using the following command:
```bash
python main.py
```
### Subsequent Executions

For subsequent executions, the script will use the saved cookies for login, speeding up the process.

### Output

The script will generate a CSV file (e.g., `data.csv`) in the project directory, containing the scraped tweets.

## Handling Rate Limits

If Twitter's rate limit is reached, the script will pause and resume once the rate limit resets. This is handled automatically, so no additional intervention is required.

## Notes

- Ensure your credentials are stored securely and avoid hardcoding them directly in the script.
- If you encounter issues with logging in or scraping, double-check your `config.ini` file for accuracy.


