import csv
import os

from utils.menu import Menu
from utils.parliamentary_spending import ParliamentarySpending
from utils.sort import SortValues


BASEDIR = os.getcwd()
DATASET = f"{BASEDIR}/data/relatorio_2021.csv"

    
def main():
    
    report_parliamentary = ParliamentarySpending(DATASET, "PI")
    report_parliamentary.load_data_dict()

    menu = Menu()
    menu.options = {
        "1": report_parliamentary.show_dataset_order_by_sum_expenses,
        "2": report_parliamentary.show_all_data,
        "3": report_parliamentary.get_by_cpf,
    }
    menu.show_options()


if __name__ == "__main__":
    main()