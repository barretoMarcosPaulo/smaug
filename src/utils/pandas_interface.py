import pandas as pd


class PandasInterface:
    def __init__(self, filepath, delimiter, state_uf):
        self.filepath = filepath
        self.dataframe = self.load_csv_by_state(filepath, state_uf, delimiter)

    def load_csv_by_state(self, file, state_uf, delimiter):
        try:
            dataframe = pd.read_csv(file, delimiter=delimiter)
            return dataframe[dataframe["sgUF"] == state_uf]
        except Exception:
            raise

    def change_column_name(self, dataset, column_target, new_column_name):
        return dataset.rename(columns={column_target: new_column_name})

    def get_dataframe_by_sum_expenses(self):
        new_dataframe = self.dataframe.groupby(["txNomeParlamentar", "cpf"])["vlrLiquido"].sum().reset_index()
        return self.change_column_name(new_dataframe, "vlrLiquido", "totalGasto")

    def get_dataframe_by_max_expenses(self):
        new_dataframe = self.dataframe.groupby(["txNomeParlamentar", "cpf"])["vlrLiquido"].max().reset_index()
        return self.change_column_name(new_dataframe, "vlrLiquido", "maiorValorGasto")

    def insert_column_in_dataset(self, target_dataset, values, name_column):
        number_of_columns = len(target_dataset.columns)
        target_dataset.insert(number_of_columns, name_column, values)
        return target_dataset

    def order_dataframe(self, dataframe, column, asc):
        return dataframe.sort_values(by=[column], ascending=asc)

    def mount_report_sum_max_expenses(self):
        dataframe_report_max = self.get_dataframe_by_max_expenses()
        dataframe_report_sum = self.order_dataframe(self.get_dataframe_by_sum_expenses(), "totalGasto", False)
        data = self.insert_column_in_dataset(dataframe_report_sum, dataframe_report_max["maiorValorGasto"], "maiorValorGasto")
        data["cpf"] = data["cpf"].astype(str)
        self._show_header("RELATORIO DE GASTOS POR DEPUTADO:")
        print(data)

    def show_dataset(self):
        self._show_header("EXIBINDO TODOS OS DADOS:")
        print(self.dataframe[["txNomeParlamentar", "datEmissao", "txtFornecedor", "vlrLiquido", "urlDocumento"]])

    def search_by_name(self):
        value = input("Digite o nome do(a) deputado(a): ")
        result = self.dataframe.loc[self.dataframe["txNomeParlamentar"] == value]
        self._show_header("EXIBINDO DADOS RETORNADOS:")
        print(result[["txNomeParlamentar", "datEmissao", "txtFornecedor", "vlrLiquido", "urlDocumento"]])
        return result

    def _show_header(self, value):
        print(f"+=============================== {value}===========================+")
