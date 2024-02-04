import unittest
import os

# Import the Parse function from your code file
from Parseur import Parse

class TestParse(unittest.TestCase):
    def test_output_files(self):
        test_cases = [
            #load_store test
            ("./test_integration/load_store/load_store.s", "./test_integration/load_store/load_store.bin"),
            #shift add sub mov test
            ("./test_integration/shift_add_sub_mov/1-4_instructions.s", "./test_integration/shift_add_sub_mov/1-4_instructions.bin"),
            ("./test_integration/shift_add_sub_mov/5-8_instructions.s", "./test_integration/shift_add_sub_mov/5-8_instructions.bin"),
            # data processing test
            ("./test_integration/data_processing/1-4_instructions.s", "./test_integration/data_processing/1-4_instructions.bin"),
            ("./test_integration/data_processing/5-10_instructions.s", "./test_integration/data_processing/5-10_instructions.bin"),
            ("./test_integration/data_processing/11-12_instructions.s", "./test_integration/data_processing/11-12_instructions.bin"),
            ("./test_integration/data_processing/13-16_instructions.s", "./test_integration/data_processing/13-16_instructions.bin"),
            #miscellaneous test
            ("./test_integration/miscellaneous/sp.s", "./test_integration/miscellaneous/sp.bin"),
            # Add more test cases as needed
        ]
        
        for input_file, expected_output_file in test_cases:
            with self.subTest(input_file=input_file):
                # Call the Parse function with input file
                output_file_name = Parse(input_file)
                
                # Read actual and expected output files
                with open(output_file_name, "r") as actual_output_file:
                    actual_output = actual_output_file.read().strip()
                with open(expected_output_file, "r") as expected_output_file:
                    expected_output = expected_output_file.read().strip()
                
                # Assert actual output matches expected output
                self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()