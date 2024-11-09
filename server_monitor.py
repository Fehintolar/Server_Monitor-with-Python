import psutil
import logging
import os
import time

# Set up logging to save to server_health.log in the same directory as this script
current_dir = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(current_dir, "server_health.log")

logging.basicConfig(
    filename="server_health.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Log a message to indicate the start of monitoring
logging.info("Starting server health check.")

try:
    while True:
        # Get CPU, memory, and disk usage
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        disk_usage = psutil.disk_usage('/')

        # Log the metrics
        logging.info(f"CPU Usage: {cpu_usage}%")
        logging.info(f"Memory Usage: {memory_info.percent}%")
        logging.info(f"Disk Usage: {disk_usage.percent}%")

        # Wait for 5 seconds before the next check
        time.sleep(5)

except KeyboardInterrupt:
    logging.info("Server health check stopped by user.")
