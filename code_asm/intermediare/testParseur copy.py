import unittest
import os
from Parseur import compilation

class TestCompilation(unittest.TestCase):
    def test_compilation(self):
        # Define test cases
        test_cases = [
            ("load_store.s", "load_store.bin"),
            
            # Add more test cases as needed
        ]
        
        # Loop through each test case
        for input_file, expected_output_file in test_cases:
            with self.subTest(input_file=input_file):
                # Call your compilation function with input file
                with open(input_file, 'r') as file:
                    input_content = file.read().strip()
                actual_output = compilation(input_content)
                
                # Read expected output from file
                with open(expected_output_file, 'r') as file:
                    expected_output = file.read().strip()
                
                # Assert actual output matches expected output
                self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()