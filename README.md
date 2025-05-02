# Bitcoin Price Checker

This Python script, `bitcoin.py`, fetches the current price of Bitcoin from the CoinCap API and calculates the cost of a user-specified number of Bitcoins in USD.

## Features

*   Accepts the number of Bitcoins to calculate the cost for as a command-line argument.
*   Handles invalid command-line arguments (missing or non-numeric).
*   Queries the CoinCap API (v3) for the latest Bitcoin price.
*   Handles potential API request errors and invalid API responses.
*   Outputs the total cost in USD, formatted to four decimal places with a comma as the thousands separator.

## Prerequisites

1.  **Python 3:** Ensure you have Python 3 installed.
2.  **`requests` library:** You need to install the `requests` library.
    ```bash
    pip install requests
    ```
3.  **CoinCap API Key:** You need an API key from CoinCap. Sign up or log in at [coincap.io](https://coincap.io/) to get your key from the dashboard.

## Setup

1.  Clone or download the `bitcoin.py` script.
2.  **Important:** Open `bitcoin.py` in a text editor and replace the placeholder `"YourApiKey"` in the `requests.get` call with your actual CoinCap API key.
    ```python
    # Inside the main function's try block:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=YOUR_ACTUAL_API_KEY_HERE")
    ```

## How to Run

Navigate to the directory containing `bitcoin.py` in your terminal and run the script using the following command structure:

```bash
python bitcoin.py <number_of_bitcoins>
```

**Example:**

To find the cost of 2.5 Bitcoins:

```bash
python bitcoin.py 2.5
```

**Output Example:**

The script will output the calculated cost in USD, formatted like this:

```
$244,612.5609
```
*(Note: The actual price will vary based on the current market rate.)*

## Error Handling

*   If no command-line argument is provided, it will exit with the message: `Missing command-line argument`
*   If the command-line argument is not a valid number, it will exit with the message: `Command-line argument is not a number`
*   If there's an issue contacting the CoinCap API, it will exit with: `API request failed`
*   If the API response format is unexpected, it will exit with: `Invalid API response` 
