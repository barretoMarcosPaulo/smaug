import csv
from .csv_reader import CsvReader
from .sort import SortValues


class ParliamentarySpending:
    UF_COLUMN_INDEX = 5
    NAME_COLUMN_INDEX = 0
    CPF_COLUMN_INDEX = 1
    PROVIDER_COLUMN_INDEX = 12
    DATE_COLUMN_INDEX = 16
    VALUE_COLUMN_INDEX = 19
    URL_COLUMN_INDEX = 30
    POLITICAL_COLUMN_INDEX = 6
    
    def __init__(self, filepath, state_uf):
        self.filepath = filepath
        self.state_uf = state_uf
        self._reader = CsvReader(filepath)
        self.dataframe = self.load_dataframe()
        self.data_process = {}

    def load_dataframe(self):
        return self._reader.filter_by_column(ParliamentarySpending.UF_COLUMN_INDEX, self.state_uf)

    def load_data_dict(self):
        self.transform_to_dict()
        self._set_sum_expenses()
        self._set_max_expenses()

    def transform_to_dict(self):
        for row in self.dataframe:
            cpf = row[1]
            if self.data_process.get(cpf, None):
                self.data_process[cpf]["registros"].append(
                    {
                        "txtFornecedor":row[ParliamentarySpending.PROVIDER_COLUMN_INDEX], 
                        "dataEmissao":row[ParliamentarySpending.DATE_COLUMN_INDEX], 
                        "vlrLiquido":row[ParliamentarySpending.VALUE_COLUMN_INDEX], 
                        "urlDocuemnto":row[ParliamentarySpending.URL_COLUMN_INDEX]
                    }
                )
            else:
                self.data_process[cpf] = {
                    "nome":row[ParliamentarySpending.NAME_COLUMN_INDEX], 
                    "cpf":cpf,
                    "sgPartido":row[ParliamentarySpending.POLITICAL_COLUMN_INDEX], 
                    "totalGasto":0, 
                    "maiorDespesa":0, 
                    "registros":[]
                }
        return self.data_process

    def _set_sum_expenses(self):
        for index in self.data_process:
            values = [float(data["vlrLiquido"]) for data in self.data_process[index]["registros"]]
            total = round(sum(values), 2)
            self.data_process[index]["totalGasto"] = total
        return self.data_process

    def _set_max_expenses(self):
        for index in self.data_process:
            values = [float(data["vlrLiquido"]) for data in self.data_process[index]["registros"]]
            sorter = SortValues(values)
            sorter.sort_elements()
            self.data_process[index]["maiorDespesa"] = sorter.values[len(values)-1]
        return self.data_process

    def show_dataset_order_by_sum_expenses(self):

        list_data = []
        for key in self.data_process:
            list_data.append(self.data_process[key])
        
        report_max = SortValues(list_data)
        report_max.sort_elements(dict_field="totalGasto")
        for i in report_max.values:
            print("Nome:", i["nome"])
            print("Total gasto", i["totalGasto"])
            print("Maior despesa", i["maiorDespesa"])
            print("-----------------------------------")
        return report_max.values
    
    def show_all_data(self):
        for key in self.data_process:
            print("Nome:", self.data_process[key]["nome"])
            print("CPF:", self.data_process[key]["cpf"])
            print("Total gasto", self.data_process[key]["totalGasto"])
            print("Maior despesa", self.data_process[key]["maiorDespesa"])
            print("Registros: ")
            
            registers = self.data_process[key]["registros"]
            for register in registers:

                print("\tFornecedor: ", register["txtFornecedor"])
                print("\tData: ", register["dataEmissao"])
                print("\tValor: ", register["vlrLiquido"])
                print("\tURL: ", register["urlDocuemnto"])
                print("\t----------------------------------------------------------")
            print("\n")

    def get_by_cpf(self, cpf=None):
        if not cpf:
            cpf = input("Informe o CPF do deputado: ")
        
        finded = self.data_process.get(cpf, None)
        if finded:
            print("Nome:", self.data_process[cpf]["nome"])
            print("Total gasto", self.data_process[cpf]["totalGasto"])
            print("Maior despesa", self.data_process[cpf]["maiorDespesa"])
            print("Registros: ")
            
            registers = self.data_process[cpf]["registros"]
            for register in registers:

                print("\tFornecedor: ", register["txtFornecedor"])
                print("\tData: ", register["dataEmissao"])
                print("\tValor: ", register["vlrLiquido"])
                print("\tURL: ", register["urlDocuemnto"])
                print("\t----------------------------------------------------------")
            print("\n")
            return True
        else:
            print("Não encontrado")
            return False