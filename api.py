import requests
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
    )

def check_api_health(url):
    try:
        response = requests.get(url,timeout=5)
        if response.status_code == 200:
            logging.info(f"API is healthy. Status Code: {response.status_code}")
            return True
        else:
            logging.warning(f"API returned non-200 status code: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        logging.error(f"Failed to connect to API at {url}. Connection error.")
    except requests.exceptions.Timeout:
        logging.error(f"Request to API at {url} timed out.")
    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred while checking API health: {e}")

check_api_health("https://api.github.com/")


