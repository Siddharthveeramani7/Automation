import logging

logging.basicConfig( 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
    )

def count_failed_logins(log_path):
    failed_count = 0
    try:
        with open(log_path, 'r') as log_file:
            for line in log_file:
                if 'Failed' in line:
                    failed_count += 1
    except FileNotFoundError:
        logging.error(f"Log file {log_path} not found.")
        return None
    except PermissionError:
        logging.error(f"Permission denied when trying to read {log_path}. Try running via sudo")
        return None
    return failed_count

THRESHOLD = 3
failures = count_failed_logins("/var/log/auth.log")

if failures is None:
    logging.error("Could not check log file")
elif failures > THRESHOLD:
    logging.warning(f"High number of failed login attempts detected: {failures}")
else:
    logging.info(f"Number of failed login attempts: {failures} - within normal range")