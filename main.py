import sys
import logging
from src.config import DEFAULT_LAT, DEFAULT_LON
from src.sentinel_client import SentinelClient
from src.analyst_agent import AnalystAgent
from src.notifications import notify_user
from src.visualiser import create_location_map

# Configure logging for professional observability
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run_conservation_agent():
    logging.info("Initializing Sentinel Conservation Agent...")
    
    eyes = SentinelClient()
    brain = AnalystAgent()
    
    logging.info(f"Scanning coordinates: {DEFAULT_LAT}, {DEFAULT_LON}")
    
    try:
        image_data = eyes.find_latest_image(DEFAULT_LAT, DEFAULT_LON)
    except Exception as e:
        logging.error(f"Failed to retrieve satellite data: {e}")
        return

    if not image_data:
        logging.warning("No suitable images found in the specified timeframe.")
        return

    logging.info(f"Image found: Captured on {image_data['date']} with {image_data['cloud_cover']}% cloud cover.")

    logging.info("Submitting metadata to the Analyst Agent...")
    report = brain.analyse_image_data(
        image_data['date'], 
        image_data['cloud_cover'], 
        image_data['url']
    )
    
    print(f"\n--- Agent Report ---\n{report}\n")

    # Structured parsing of the AI's decision
    if "[ACCEPT]" in report.upper():
        notify_user("Sentinel Agent", f"High-quality image identified for {image_data['date']}")
        logging.info("Action: Positive identification. Notification dispatched.")
        create_location_map(DEFAULT_LAT, DEFAULT_LON, image_data['date'])
        logging.info("Map generated: Open map.html to view the site.")
    else:
        logging.info("Action: Image rejected based on quality criteria.")

if __name__ == "__main__":
    try:
        run_conservation_agent()
    except KeyboardInterrupt:
        logging.info("Process interrupted by user.")
        sys.exit(0)
    except Exception as error:
        logging.critical(f"Critical System Failure: {error}")
        sys.exit(1)