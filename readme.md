# Sentinel Conservation Agent

An autonomous geospatial monitoring tool designed to identify high-quality satellite imagery for rainforest preservation. This project integrates the SpatioTemporal Asset Catalog (STAC) with Large Language Models (LLMs) to automate the filtering of cloud-obscured satellite data.

## Problem Statement

Tropical deforestation monitoring is frequently hindered by heavy cloud cover, which renders a high percentage of optical imagery unusable. Manual screening of these datasets is time-intensive and delays response times for conservation teams. 

The Sentinel Conservation Agent acts as a high-speed filter, using AI-driven metadata analysis to identify clear-sky imagery. This ensures that only actionable data is passed to researchers, accelerating the detection of illegal logging and land-use changes.

## Technical Architecture

The application is built using a modular, class-based architecture to ensure maintainability and testability.

* **SentinelClient (src/sentinel_client.py):** Handles spatial and temporal queries against the Microsoft Planetary Computer STAC API. It utilizes guard clauses to handle empty result sets and ensures metadata integrity.
* **AnalystAgent (src/analyst_agent.py):** Interfaces with the Hugging Face Inference API. It utilizes prompt engineering and structured output constraints to convert unstructured model reasoning into deterministic signals.
* **Notifications (src/notifications.py):** An OS-level bridge for real-time alerting on Linux systems.
* **Orchestrator (main.py):** Manages the application lifecycle, error handling, and professional logging.

## Core Technologies

* **Python 3.11:** Primary development language.
* **STAC API (pystac-client):** Standardized geospatial data retrieval.
* **Hugging Face Inference API:** Cloud-based LLM inference (Zephyr-7B).
* **Unittest & Mock:** Automated verification of AI logic without API costs.
* **Logging:** Centralized observability for production monitoring.

## Installation

This project is optimized for Guix SD but is compatible with any Linux environment utilizing a Python virtual environment.

1. **Clone the repository:**
```bash
   git clone <repository-url>
   cd sentinel_agent
```
2. Configure Environment: Create a .env file in the root directory:
```
HUGGINGFACEHUB_API_TOKEN=your_token_here
```
3. Install Dependencies:
```
pip install -r requirements.txt
```
## Usage
Execute the main entry point to initiate a scan:
```
python main.py
```

To run the test suite:
```
python -m unittest discover tests
```

## Project Structure
```
├── src/
│   ├── config.py           # Configuration management and constants
│   ├── sentinel_client.py  # Geospatial API client
│   ├── analyst_agent.py    # AI reasoning logic
│   └── notifications.py    # System notification bridge
├── tests/                  # Unit tests and mocks
├── main.py                 # Application entry point
├── .env                    # Local secrets (excluded via .gitignore)
├── .gitignore              # Version control exclusions
└── requirements.txt        # Pinned project dependencies
```

