import sys
from src.config import DEFAULT_LAT, DEFAULT_LON
from src.sentinel_client import SentinelClient
from src.analyst_agent import AnalystAgent
from src.notifications import notify_user

def run_conservation_agent():
    """
    Coordinates the satellite search and AI analysis workflow.
    """
    print("Initializing Sentinel Conservation Agent...")
    
    # Initialize the core components.
    eyes = SentinelClient()
    brain = AnalystAgent()
    
    # 1. Search for the most recent satellite imagery.
    print(f"Scanning coordinates: {DEFAULT_LAT}, {DEFAULT_LON}")
    image_data = eyes.find_latest_image(DEFAULT_LAT, DEFAULT_LON)
    
    if not image_data:
        print("Status: No suitable images found in the specified timeframe.")
        return

    print(f"Image found: Captured on {image_data['date']} "
          f"with {image_data['cloud_cover']}% cloud cover.")

    # 2. Execute AI-driven metadata analysis.
    print("Submitting metadata to the Analyst Agent for evaluation...")
    report = brain.analyse_image_data(
        image_data['date'], 
        image_data['cloud_cover'], 
        image_data['url']
    )
    
    print(f"\n--- Agent Report ---\n{report}\n")

    # 3. Process the agent's decision.
    if "accept" in report.lower():
        notify_user("Sentinel Agent", f"High-quality image identified for {image_data['date']}")
        print("Action: Desktop notification dispatched.")
    else:
        print("Action: Image rejected based on quality criteria. Continuing monitoring.")

if __name__ == "__main__":
    try:
        run_conservation_agent()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
        sys.exit(0)
    except Exception as error:
        print(f"Critical System Error: {error}")
        sys.exit(1)