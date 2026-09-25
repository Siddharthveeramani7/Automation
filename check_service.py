import subprocess
import logging
import argparse

SERVER_VERSION='2.0branch-a'

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def is_service_active(service_name):
    result = subprocess.run(
        ['systemctl','is-active',service_name],
        capture_output = True,
        text = True
    )
    status = result.stdout.strip()
    return status == "active"

def restart_service(service_name):
    result = subprocess.run(
        ['systemctl', 'restart', service_name],
        capture_output = True,  
        text = True
        )
    if result.returncode == 0:
        logging.info(f"{service_name} restarted successfully.")
    else:
        logging.error(f"Failed to restart {service_name}. Error: {result.stderr.strip()}")

parser = argparse.ArgumentParser(description='Check and restart a service if it is not running.')
parser.add_argument('service_name', type=str, help='Name of the service to check')
args = parser.parse_args()
service = args.service_name

if is_service_active(service):
    logging.info(f"{service} is running fine.")
else:
    logging.warning(f"{service} is NOT running — needs attention.")
    restart_service(service)


    
