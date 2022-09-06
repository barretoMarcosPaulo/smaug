import os

from utils.menu import Menu
from utils.pandas_interface import PandasInterface

BASEDIR = os.getcwd()
DATASET = f"{BASEDIR}/data/relatorio_2021.csv"


def main():
    pandas_interface = PandasInterface(filepath=DATASET, delimiter=";", state_uf="PI")
    menu = Menu()
    menu.options = {
        "1": pandas_interface.mount_report_sum_max_expenses,
        "2": pandas_interface.show_dataset,
        "3": pandas_interface.search_by_name,
    }
    menu.show_options()


if __name__ == "__main__":
    main()
