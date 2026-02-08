import os
from huggingface_hub import InferenceClient
from src.config import HF_TOKEN, MODEL_ID, CLOUD_THRESHOLD

class AnalystAgent:
    """
    An AI-driven agent responsible for evaluating satellite imagery metadata 
    to determine suitability for conservation monitoring.
    """

    def __init__(self):
        # Initialize the Inference Client using the token from environment variables
        if not HF_TOKEN:
            raise ValueError("HF_TOKEN not found. Please check your .env file.")
        
        # We use the official InferenceClient which handles the HTTP handshake
        self.client = InferenceClient(model=MODEL_ID, token=HF_TOKEN)

    def analyse_image_data(self, date, clouds, url):
        """
        Submits metadata to the LLM and parses the result.
        Returns a string containing the justification and a [TAG].
        """
        
        # Construct a high-precision System Prompt
        prompt = (
            f"Role: Satellite Data Analyst\n"
            f"Objective: Evaluate image suitability for rainforest monitoring.\n"
            f"Constraint: Reject if cloud cover exceeds {CLOUD_THRESHOLD}%.\n\n"
            f"Data to Analyze:\n"
            f"- Capture Date: {date}\n"
            f"- Cloud Cover: {clouds}%\n"
            f"- Image URL: {url}\n\n"
            f"Instructions: Provide a one-sentence justification. "
            f"Your final line MUST contain exactly one of these tags: [ACCEPT] or [REJECT]."
        )

        try:
            # Perform the HTTP POST request via the 'chat' endpoint
            response = self.client.chat_completion(
                messages=[{"role": "user", "content": prompt}],
                max_tokens=150,
                temperature=0.1  # Low temperature for deterministic, logical output
            )
            
            # Extract the text content from the response object
            return response.choices[0].message.content

        except Exception as error:
            # Professional Error Handling: 
            # If the API fails, we return a string that the orchestrator can parse safely.
            error_msg = str(error)
            
            if "400" in error_msg:
                return f"Error: API Model mismatch or endpoint error. Details: {error_msg[:50]}... [REJECT]"
            
            if "503" in error_msg:
                return "Error: Hugging Face server is currently overloaded. [REJECT]"
                
            return "Error: Analysis failed due to network issue. [REJECT]"