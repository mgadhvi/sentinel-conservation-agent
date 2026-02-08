import unittest
from unittest.mock import patch, MagicMock
from src.analyst_agent import AnalystAgent

class TestAnalystAgent(unittest.TestCase):
    def setUp(self):
        self.agent = AnalystAgent()

    @patch('src.analyst_agent.InferenceClient.chat_completion')
    def test_analyse_image_data_accept(self, mock_chat):
        # Simulate a positive response from the LLM
        mock_response = MagicMock()
        mock_response.choices = [MagicMock(message=MagicMock(content="The image is clear. [ACCEPT]"))]
        mock_chat.return_value = mock_response

        report = self.agent.analyse_image_data("2026-01-01", 5.0, "http://test.url")
        
        self.assertIn("[ACCEPT]", report)
        self.assertNotIn("Error", report)

    @patch('src.analyst_agent.InferenceClient.chat_completion')
    def test_analyse_image_data_reject(self, mock_chat):
        # Simulate a negative response from the LLM
        mock_response = MagicMock()
        mock_response.choices = [MagicMock(message=MagicMock(content="Too many clouds. [REJECT]"))]
        mock_chat.return_value = mock_response

        report = self.agent.analyse_image_data("2026-01-01", 45.0, "http://test.url")
        
        self.assertIn("[REJECT]", report)

if __name__ == '__main__':
    unittest.main()