import os

# Import the Parse function from your code file
from Parseur2 import Parse


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class TestParse:

    def __init__(self):
        self.expected_test_cases = [
            "./test_integration/load_store/load_store.bin",
            "./test_integration/shift_add_sub_mov/1-4_instructions.bin",
            "./test_integration/shift_add_sub_mov/5-8_instructions.bin",
            "./test_integration/data_processing/1-4_instructions.bin",
            "./test_integration/data_processing/5-10_instructions.bin",
            "./test_integration/data_processing/11-12_instructions.bin",
            "./test_integration/data_processing/13-16_instructions.bin",
            "./test_integration/miscellaneous/sp.bin",
            "./test_integration/conditional/branch.bin",
            "../code_c/calckeyb.bin",
            "../code_c/calculator.bin",
            "../code_c/simple_add.bin",
            "../code_c/tty.bin",
            "../code_c/testfp.bin"
            
        ]
        self.output_test_cases = [
            "./test_integration/load_store/load_store.s",
            "./test_integration/shift_add_sub_mov/1-4_instructions.s",
            "./test_integration/shift_add_sub_mov/5-8_instructions.s",
            "./test_integration/data_processing/1-4_instructions.s",
            "./test_integration/data_processing/5-10_instructions.s",
            "./test_integration/data_processing/11-12_instructions.s",
            "./test_integration/data_processing/13-16_instructions.s",
            "./test_integration/miscellaneous/sp.s",
            "./test_integration/conditional/branch.s",
            "../code_c/calckeyb.s",
            "../code_c/calculator.s",
            "../code_c/simple_add.s",
            "../code_c/tty.s",
            "../code_c/testfp.s"
        ]

    def test_output_files(self):
        total_tests_correct = 0
        for k in range(len(self.output_test_cases)):
            expected = self.get_expected_bin(self.expected_test_cases[k])
            output_file_path = Parse(self.output_test_cases[k], "./test/" + str(k))
            actual = self.get_expected_bin(output_file_path)

            print(self.expected_test_cases[k], self.output_test_cases[k])
            print(expected, actual)
            correct_count = 0
            for i in range(len(expected)):
                try:
                    if expected[i] != actual[i]:
                        # print the characters that change in red
                        print("Expected/Actual: ")
                        for j in range(len(expected[i])):
                            if expected[i][j] != actual[i][j]:
                                print(bcolors.FAIL + expected[i][j] + bcolors.ENDC, end="")
                            else:
                                print(bcolors.OKGREEN + expected[i][j] + bcolors.ENDC, end="")
                        print(f"/{actual[i]} [KO]\n")
                    else:
                        correct_count += 1
                        print(f"Expected/Actual: {bcolors.OKGREEN + expected[i] + bcolors.ENDC}/{actual[i]} [OK]\n")
                except IndexError:
                    if i > len(expected):
                        print(f"Expected/Actual: None/{bcolors.FAIL + actual[i] + bcolors.ENDC} [KO]\n")
                        continue
                    elif i > len(actual):
                        print(f"Expected/Actual: {bcolors.FAIL + expected[i] + bcolors.ENDC}/None [KO]\n")
                        continue
            
            percentage_correct = (correct_count / len(expected)) * 100
            if percentage_correct == 100:
                total_tests_correct +=1
            #print(f"Percentage of Correctness: {percentage_correct:.2f}%")
        print(f"Total number of tests correct {total_tests_correct}/{len(self.output_test_cases)}")

    def get_expected_bin(self, file_name):
        with open(file_name, "r") as file:
            for line in file.readlines():
                # skip the first line
                if line == "v2.0 raw\n":
                    continue
                return line.split()


if __name__ == '__main__':
    testParse = TestParse()
    testParse.test_output_files()