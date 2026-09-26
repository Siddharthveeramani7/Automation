import logging
import argparse

logging.basicConfig( 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
    )

def count_pattern_occurence(log_path, pattern):
    count = 0
    try:
        with open(log_path, 'r') as log_file:
            for line in log_file:
                if pattern in line:
                    count += 1
    except FileNotFoundError:
        logging.error(f"Log file {log_path} not found.")
        return None
    except PermissionError:
        logging.error(f"Permission denied when trying to read {log_path}. Try running via sudo")
        return None
    return count

def main():
    parser = argparse.ArgumentParser(
        description="Monitor a log file for a pattern and alert if a threshold exceeds"
    )
    parser.add_argument(
        "log_path",
        help="Path to the log file to monitor"
    )
    parser.add_argument(
        "pattern",
        help="Pattern to search for in the log file"
    )
    parser.add_argument(
        "--threshold",
        type=int,
        default=3,
        help="Threshold for the number of occurrences of the pattern"
    )
    args = parser.parse_args()

    count = count_pattern_occurence(args.log_path, args.pattern)
    if count is None:
        logging.error("Could not complete log check")
    elif count > args.threshold:
        logging.warning(f"ALERT: '{args.pattern}' occurred {count} times, which exceeds the threshold of {args.threshold}.")   
    else:
        logging.info(f"Pattern '{args.pattern}' occurred {count} times, which is within the threshold of {args.threshold}.")

if __name__ == "__main__":
    main() 
