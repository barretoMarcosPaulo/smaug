import contextlib
import os

import pytest
from utils.pandas_interface import PandasInterface

BASEDIR = os.getcwd()
DATASET = f"{BASEDIR}/data/test.csv"


class TestPandasInterface:
    @pytest.fixture
    def pandas_interface(self):
        return PandasInterface(filepath=DATASET, delimiter=";", state_uf="PI")

    def test_load_csv(self):
        QTD_ROWS_CSV_TEST = 4
        pandas_interface = PandasInterface(filepath=DATASET, delimiter=";", state_uf="PI")
        assert pandas_interface.dataframe.shape[0] == QTD_ROWS_CSV_TEST

    def test_load_csv_wrong_path(self):
        with contextlib.suppress(Exception):
            PandasInterface(filepath="test.csv", delimiter=";", state_uf="PI")
            assert False

    def test_load_csv_wrong_filetype(self):
        with contextlib.suppress(Exception):
            PandasInterface(filepath="test.txt", delimiter=";", state_uf="PI")
            assert False

    def test_get_dataframe_by_sum_expenses(self, pandas_interface):
        QTD_ROWS_CSV_TEST = 1
        dataframe = pandas_interface.get_dataframe_by_sum_expenses()

        assert dataframe.shape[0] == QTD_ROWS_CSV_TEST
        assert dataframe.at[0, "txNomeParlamentar"] == "Rejane Dias"
        assert dataframe.at[0, "totalGasto"] == 3940
        assert dataframe.at[0, "cpf"] == 42105560334

    def test_get_dataframe_by_max_expenses(self, pandas_interface):
        QTD_ROWS_CSV_TEST = 1
        dataframe = pandas_interface.get_dataframe_by_max_expenses()

        assert dataframe.shape[0] == QTD_ROWS_CSV_TEST
        assert dataframe.at[0, "txNomeParlamentar"] == "Rejane Dias"
        assert dataframe.at[0, "maiorValorGasto"] == 2500
        assert dataframe.at[0, "cpf"] == 42105560334

    def test_change_column_name(self, pandas_interface):
        QTD_ROWS_CSV_TEST = 1
        dataframe_max_expenses = pandas_interface.get_dataframe_by_max_expenses()

        new_dataframe = pandas_interface.change_column_name(dataframe_max_expenses, "txNomeParlamentar", "NomeDeputado")
        new_columns = list(new_dataframe.columns)

        assert new_dataframe.shape[0] == QTD_ROWS_CSV_TEST
        assert "NomeDeputado" in new_columns
        assert "txNomeParlamentar" not in new_columns

    def test_order_dataframe_desc(self, pandas_interface):
        MAX_VALUE = 2500
        data = pandas_interface.order_dataframe(pandas_interface.dataframe, "vlrLiquido", False)
        assert data.at[0, "vlrLiquido"] == MAX_VALUE
