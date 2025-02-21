import unittest
from src.data_preprocessing import preprocess_data

class TestDataPreprocessing(unittest.TestCase):

    def test_preprocess_data(self):
        # Test with sample input
        raw_data = ["This is a sample sentence.", "Another sentence for testing."]
        expected_output = ["this is a sample sentence", "another sentence for testing"]
        
        processed_data = preprocess_data(raw_data)
        
        self.assertEqual(processed_data, expected_output)

    def test_empty_input(self):
        # Test with empty input
        raw_data = []
        expected_output = []
        
        processed_data = preprocess_data(raw_data)
        
        self.assertEqual(processed_data, expected_output)

    def test_invalid_input(self):
        # Test with invalid input
        raw_data = None
        
        with self.assertRaises(TypeError):
            preprocess_data(raw_data)

if __name__ == '__main__':
    unittest.main()