from huggingface_hub import InferenceClient
from src.config import HF_TOKEN, MODEL_ID, CLOUD_THRESHOLD

class AnalystAgent:
    """
    Evaluates satellite imagery quality using Large Language Models.
    """

    def __init__(self):
        """Initializes the Hugging Face inference client."""
        self.client = InferenceClient(token=HF_TOKEN)

    def analyse_image_data(self, date, clouds, url):
        """
        Evaluates imagery metadata against cloud cover thresholds.

        Args:
            date (str): Capture date.
            clouds (float): Cloud cover percentage.
            url (str): Asset URL.

        Returns:
            str: Agent reasoning and decision.
        """
        prompt = (
            f"Role: Satellite Data Analyst\n"
            f"Objective: Evaluate image suitability for rainforest monitoring.\n"
            f"Criterion: Reject if cloud cover exceeds {CLOUD_THRESHOLD}%.\n\n"
            f"Data:\n"
            f"- Date: {date}\n"
            f"- Cloud Cover: {clouds}%\n"
            f"- URL: {url}\n\n"
            f"Instructions: Provide a brief justification for your decision. "
            f"Your final line must contain exactly one of these tags: [ACCEPT] or [REJECT]."
        )

        try:
            response = self.client.chat_completion(
                model=MODEL_ID,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=300,
                temperature=0.1
            )
            return response.choices[0].message.content
        except Exception as error:
            return f"Error: Analysis could not be completed. {error}"