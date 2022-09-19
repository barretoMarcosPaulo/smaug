import csv

class CsvReader:
    def __init__(self, filepath, delimiter=";"):
        self.filepath = filepath
        self.delimiter = delimiter
        self.dataframe = self.read()

    def read(self):
        try:
            with open(self.filepath, newline='') as csvfile:
                buffer_data = csv.reader(csvfile, delimiter=self.delimiter)
                return buffer_data
        except Exception:
            return False

    def export(self, data):
        return "not implemented"

    def filter_by_column(self, column_index, value):
        with open(self.filepath, newline='') as csvfile:
            buffer_data = csv.reader(csvfile, delimiter=self.delimiter)
            filtered_data = []
            for row in buffer_data:
                if row[column_index] == value:
                    filtered_data.append(row)
            return filtered_data
        
        