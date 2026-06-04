import unittest
import os
import pandas as pd
from main import days_allowed_to_borrow_converter, basic_dataframe_cleaning, book_dataframe_cleaning, library_system_cross_reference_validator, library_system_book_checkout_matcher, DuplicateIDException

class TestOperations(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def test_basic_dataframe_cleaning(self):
        input_test_data_df = pd.read_csv(os.path.join(os.getcwd(), r"test/test_data/basic_dataframe_cleaning/input_test_data.csv"))
        output_test_data_df = pd.read_csv(os.path.join(os.getcwd(), r"test/test_data/basic_dataframe_cleaning//output_test_data.csv"))
        pd.testing.assert_frame_equal(basic_dataframe_cleaning(input_test_data_df, 'Id').reset_index(drop=True), output_test_data_df.reset_index(drop=True))

    def test_basic_dataframe_cleaning_exception(self):
        input_test_data_df = pd.read_csv(os.path.join(os.getcwd(), r"test/test_data/basic_dataframe_cleaning/exception_input_test_data.csv"))        
        with self.assertRaises(DuplicateIDException):
            basic_dataframe_cleaning(input_test_data_df, 'Id')

unittest.main()