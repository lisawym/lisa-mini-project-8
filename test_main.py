import unittest

# from mylib.transform_load import load_and_split
from mylib.query import query
from mylib.extract import extract

# from unittest import mock

"""
class TestLoadAndSplit(unittest.TestCase):
    def test_load_and_split(self):
        # Create a mock sqlite3 connection
        conn_mock = mock.Mock()

        # Create a mock cursor
        cursor_mock = mock.Mock()
        conn_mock.cursor.return_value = cursor_mock

        # Create a mock CSV reader
        csv_reader_mock = mock.Mock()
        cursor_mock.fetchall.return_value = csv_reader_mock

        # Simulate loading the data from the CSV file
        # Create a list to represent the CSV reader data
        csv_reader_data = []
        for row in csv_reader_mock:
            csv_reader_data.append(row)

        # Randomly shuffle the list
        random.shuffle(csv_reader_data)

        # Simulate inserting the data into the database
        cursor_mock.executemany.return_value = None

        # Split the data into training and test sets
        split = int(len(csv_reader_data) * 0.8)
        train_data = csv_reader_data[:split]
        test_data = csv_reader_data[split:]

        # Simulate saving the training and test datasets to separate CSV files
        with open("train_data.csv", "w", newline="") as f:
            csv_writer = csv.writer(f)
            for row in train_data:
                csv_writer.writerow(row)

        with open("test_data.csv", "w", newline="") as f:
            csv_writer = csv.writer(f)
            for row in test_data:
                csv_writer.writerow(row)

        # Call the load_and_split function
        load_and_split(conn_mock)

        # Verify that the mocked functions were called correctly
        conn_mock.cursor.assert_called_once()
        csv_reader_mock.assert_called_once()
        cursor_mock.executemany.assert_called_once()
"""


class TestQuery(unittest.TestCase):
    def test_query(self):
        # Create a mock sqlite3 connection
        # conn_mock = mock.Mock()

        # Call the query function
        result = query("OfferDB.db")

        # Verify that the mocked functions were called correctly
        # conn_mock.cursor.assert_called_once()

        # Verify the return value
        self.assertEqual(result, "Success")


class TestExtract(unittest.TestCase):
    def test_extract(self):
        # Simulate downloading the CSV file from the URL
        with open("data/offer.csv", "rb") as f:
            file_content = f.read()

        # Call the extract function
        file_path = extract()

        # Verify that the file was downloaded to the correct location
        self.assertEqual(file_path, "data/offer.csv")

        # Verify that the file content is the same as the mocked content
        with open(file_path, "rb") as f:
            actual_file_content = f.read()

        self.assertEqual(actual_file_content, file_content)


if __name__ == "__main__":
    unittest.main()
