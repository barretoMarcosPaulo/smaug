import contextlib
import os

import pytest
from utils.sort import SortValues
from utils.csv_reader import CsvReader
from utils.parliamentary_spending import ParliamentarySpending

BASEDIR = os.getcwd()
DATASET = f"{BASEDIR}/data/test.csv"


class TestSorting:

    def test_sort_array_5_elements(self):
        sorter = SortValues([90, 1, 4, 6, 11])
        sorter.sort_elements()
        assert sorter.values[0] == 1
        assert sorter.values[1] == 4
        assert sorter.values[2] == 6
        assert sorter.values[3] == 11
        assert sorter.values[4] == 90

    def test_sort_array_3_elements(self):
        sorter = SortValues([0, -1, -4])
        sorter.sort_elements()
        assert sorter.values[0] == -4
        assert sorter.values[1] == -1
        assert sorter.values[2] == 0

    def test_sort_array_10_elements(self):
        sorter = SortValues([1, 1921, 14, 26, 99, 44, 11, 89, 71, 56])
        sorter.sort_elements()

        assert sorter.values[0] == 1
        assert sorter.values[1] == 11
        assert sorter.values[2] == 14
        assert sorter.values[3] == 26
        assert sorter.values[4] == 44
        assert sorter.values[5] == 56
        assert sorter.values[6] == 71
        assert sorter.values[7] == 89
        assert sorter.values[8] == 99
        assert sorter.values[9] == 1921


class TestCsvReader:

    def test_load_csv_reader(self):
        reader = CsvReader(DATASET)
        assert reader.filepath == DATASET
        assert reader.delimiter == ";"
        assert reader.dataframe
        

    def test_read_csv_file(self):
        reader = CsvReader(DATASET)
        response = reader.read()
        assert response

    def test_read_wrong_filepath(self):
        reader = CsvReader("wrong.csv")
        response = reader.read()
        assert response == False


    def test_find_data_by_cpf(self):
        QTD_ROWS = 4
        reader = CsvReader(DATASET)
        result = reader.filter_by_column(ParliamentarySpending.CPF_COLUMN_INDEX, "42105560334")
        assert len(result) == QTD_ROWS
        assert result[0][0] == "Rejane Dias"
        assert result[1][0] == "Rejane Dias"
        assert result[2][0] == "Rejane Dias"
        assert result[3][0] == "Rejane Dias"

        assert result[0][1] == "42105560334"
        assert result[1][1] == "42105560334"
        assert result[2][1] == "42105560334"
        assert result[3][1] == "42105560334"

    def test_find_data_by_name(self):
        QTD_ROWS = 4
        reader = CsvReader(DATASET)
        result = reader.filter_by_column(ParliamentarySpending.NAME_COLUMN_INDEX, "Rejane Dias")
        assert len(result) == QTD_ROWS
        assert result[0][0] == "Rejane Dias"
        assert result[1][0] == "Rejane Dias"
        assert result[2][0] == "Rejane Dias"
        assert result[3][0] == "Rejane Dias"

        assert result[0][1] == "42105560334"
        assert result[1][1] == "42105560334"
        assert result[2][1] == "42105560334"
        assert result[3][1] == "42105560334"

    def test_find_data_no_result(self):
        QTD_ROWS = 0
        reader = CsvReader(DATASET)
        result = reader.filter_by_column(ParliamentarySpending.NAME_COLUMN_INDEX, "Marcos Paulo")
        assert len(result) == QTD_ROWS

class TestParliamentarySpending:

    def test_show_dataset_order_by_sum_expenses(self):
        report_parliamentary = ParliamentarySpending(DATASET, "PI")
        report_parliamentary.load_data_dict()
        result = report_parliamentary.show_dataset_order_by_sum_expenses()

        assert result[0]["nome"] == "TESTE"
        assert result[0]["cpf"] == "42105561111"
        assert result[0]["totalGasto"] == 240

        assert result[1]["nome"] == "Rejane Dias"
        assert result[1]["cpf"] == "42105560334"
        assert result[1]["totalGasto"] == 1440.0

    def test_load_data_dict(self):
        report_parliamentary = ParliamentarySpending(DATASET, "PI")
        report_parliamentary.load_data_dict()

        assert report_parliamentary.data_process["42105560334"]["nome"] == "Rejane Dias"
        assert report_parliamentary.data_process["42105560334"]["totalGasto"] == 1440.0
        assert report_parliamentary.data_process["42105560334"]["maiorDespesa"] == 1200.0

        assert report_parliamentary.data_process["42105561111"]["nome"] == "TESTE"
        assert report_parliamentary.data_process["42105561111"]["totalGasto"] == 240.0
        assert report_parliamentary.data_process["42105561111"]["maiorDespesa"] == 120.0

    def test_get_by_cpf(self):
        report_parliamentary = ParliamentarySpending(DATASET, "PI")
        report_parliamentary.load_data_dict()
        response = report_parliamentary.get_by_cpf("42105560334")
        assert response

    def test_get_by_cpf_not_found(self):
        report_parliamentary = ParliamentarySpending(DATASET, "PI")
        report_parliamentary.load_data_dict()
        response = report_parliamentary.get_by_cpf("42105560332")
        assert response == False

