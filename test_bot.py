import unittest
from unittest.mock import patch, MagicMock
import test

class TestPerplexityBot(unittest.TestCase):
    @patch('test.uc')
    @patch('test.WebDriverWait')
    @patch('test.time.sleep')
    def test_get_perplexity_answer_driver_init(self, mock_sleep, mock_wait, mock_uc):
        # Setup mocks
        mock_driver = MagicMock()
        mock_uc.Chrome.return_value = mock_driver
        mock_uc.ChromeOptions.return_value = MagicMock()

        # Mocking find_elements for the answers
        mock_element = MagicMock()
        mock_element.text = "Mocked answer"
        mock_driver.find_elements.return_value = [mock_element]

        # Execute
        answer = test.get_perplexity_answer("test prompt")

        # Verify: uc.Chrome should be called exactly once
        mock_uc.Chrome.assert_called_once()

        # Verify driver is quit
        mock_driver.quit.assert_called_once()

        self.assertEqual(answer, "Mocked answer")

if __name__ == '__main__':
    unittest.main()
