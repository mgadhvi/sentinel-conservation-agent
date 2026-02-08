# Sentinel Conservation Agent

An autonomous geospatial intelligence agent designed to streamline rainforest monitoring. This tool integrates high-resolution satellite data with Large Language Models (LLMs) to automate the validation of imagery for conservation efforts.

## Objective
Manual verification of satellite imagery is a bottleneck for conservationists monitoring remote regions. The **Sentinel Conservation Agent** acts as a first-responder system, autonomously fetching, analysing, and filtering imagery to ensure field researchers only spend time on high-quality, relevant data.


## Key Features
* **Automated STAC Discovery:** Interfaces with the Microsoft Planetary Computer to fetch real-time Sentinel-2 imagery.
* **LLM-Driven Analysis:** Utilises Llama-3.2 (via Hugging Face Inference API) to interpret metadata and provide logical justifications for image selection.
* **Defensive API Architecture:** Implements robust error handling and fallback logic to manage "API drift" and inference provider fluctuations.
* **Geospatial Visualisation:** Generates interactive Leaflet-based maps (Folium) to provide immediate spatial context for analysed targets.

## Tech Stack
* **Language:** Python 3.10+
* **Geospatial:** PySTAC, Planetary Computer, Folium
* **AI/Inference:** Hugging Face Hub (InferenceClient), Llama-3.2-3B
* **Testing:** Unittest (Mock-based architecture)

## Installation

This project is optimised for Guix SD but is compatible with any Linux environment utilising a Python virtual environment.

1. **Clone the repository:**
```bash
  git clone [https://github.com/mgadhvi/sentinel-conservation-agent.git](https://github.com/mgadhvi/sentinel-conservation-agent.git)
   cd sentinel-conservation-agent
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

