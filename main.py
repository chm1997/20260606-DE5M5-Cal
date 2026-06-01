# Imports and Data
import pandas as pd
import regex as re

library_system_customer_path = r"C:\Course Files\data\03_Library SystemCustomers.csv"
library_system_book_path = r"C:\Course Files\data\03_Library Systembook.csv"
library_system_customer_output_path = r"C:\Course Files\data\03_Library SystemCustomers Output.csv"
library_system_book_output_path = r"C:\Course Files\data\03_Library Systembook Output.csv"

# Exceptions
class DuplicateIDException(Exception):
    """
    Raised when an ID field is duplicated in the input dataframes
    """

class WeirdDaysAllowedToBorrowException(Exception):
    """
    Raised when days allowed to borrow column produces multiple sets of numbers
    """

# Functions
def days_allowed_to_borrow_converter(x):
    multiplyer = 1
    if 'weeks' in x.lower():
        multiplyer = 7
    numbers = re.findall(r'\d+', x)
    if len(numbers) != 1:
        raise WeirdDaysAllowedToBorrowException(f"Following days allowed to borrow column produces multiple numbers: {x}")
    else:
        return int(int(numbers[0]) * multiplyer)

def basic_dataframe_cleaning(df, id_column_name):
    df = df.dropna()
    df = df.drop_duplicates()
    df[id_column_name] = df[id_column_name].apply(lambda x: int(x))
    if True in df.duplicated(subset=[id_column_name]):
        raise DuplicateIDException(f"duplicate in {id_column_name} field")
    return df

def book_dataframe_cleaning(df):
    df['Book checkout'] = df['Book checkout'].apply(lambda x: x.strip('''"'''))
    df['Book checkout'] = pd.to_datetime(df['Book checkout'], format= '%d/%m/%Y', errors='coerce')
    df['Book Returned'] = pd.to_datetime(df['Book Returned'], format= '%d/%m/%Y', errors='coerce')
    df['Days allowed to borrow'] = df['Days allowed to borrow'].apply(lambda x: days_allowed_to_borrow_converter(x))
    df['Customer ID'] = df['Customer ID'].apply(lambda x: int(x))
    df = df.dropna()
    return df

def library_system_cross_reference_validator(books_df, customers_df):
    not_in_series = books_df['Customer ID'].isin(customers_df['Customer ID'])
    dropped_count = 0
    for index, row in not_in_series.items():
        if row == False:
            dropped_count += 1
            books_df = books_df.drop(index)
    return books_df, dropped_count


# Main Code
def main():
    library_system_customer_df = pd.read_csv(library_system_customer_path)
    library_system_book_df = pd.read_csv(library_system_book_path)

    library_system_customer_df = basic_dataframe_cleaning(library_system_customer_df, 'Customer ID')
    library_system_book_df = basic_dataframe_cleaning(library_system_book_df, 'Id')

    library_system_book_df = book_dataframe_cleaning(library_system_book_df)

    library_system_book_df, records_dropped = library_system_cross_reference_validator(library_system_book_df, library_system_customer_df)

    library_system_customer_df.to_csv(library_system_customer_output_path)
    library_system_book_df.to_csv(library_system_book_output_path)
    return records_dropped

print(main())

# print(library_system_customer_df.head(10))
# print(library_system_book_df.head(25))
# print(records_dropped)