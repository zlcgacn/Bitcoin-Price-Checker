import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    
    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    
    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey")
        data = response.json()
        price = float(data["data"]["priceUsd"])
        cost = bitcoins * price
        print(f"${cost:,.4f}")
    except requests.RequestException:
        sys.exit("API request failed")
    except (KeyError, ValueError):
        sys.exit("Invalid API response")

if __name__ == "__main__":
    main() 
