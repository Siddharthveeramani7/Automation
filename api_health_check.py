import requests
import argparse
import logging
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def check_api_health(url, retries=3, delay=3, timeout=5):
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, timeout=timeout)
            if response.status_code == 200:
                logging.info(f"{url} is healthy (200 OK) on attempt {attempt}.")
                return True
            else:
                logging.warning(f"{url} returned status {response.status_code} on attempt {attempt}.")
        except requests.exceptions.ConnectionError:
            logging.warning(f"Attempt {attempt}: could not connect to {url}.")
        except requests.exceptions.Timeout:
            logging.warning(f"Attempt {attempt}: request to {url} timed out.")

        if attempt < retries:
            time.sleep(delay)

    logging.error(f"{url} failed health check after {retries} attempts.")
    return False

def main():
    parser = argparse.ArgumentParser(
        description="Check API/endpoint health with retry logic."
    )
    parser.add_argument("url", help="URL to check, e.g. https://api.github.com")
    parser.add_argument("--retries", type=int, default=3, help="Number of retry attempts (default: 3)")
    parser.add_argument("--delay", type=int, default=3, help="Seconds to wait between retries (default: 3)")
    args = parser.parse_args()

    check_api_health(args.url, retries=args.retries, delay=args.delay)

if __name__ == "__main__":
    main()