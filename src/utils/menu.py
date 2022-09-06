class Menu:
    EXIT_CODE = "0"

    def __init__(self):
        self.options = {}

    def show_options(self):
        value = -1

        print("Olá, sou o SMAUG!!")
        print("Escolha uma opção e aperte ENTER:")

        while value != Menu.EXIT_CODE:
            print("\n")
            print("[1] - Relatório mostrando o somatório de gastos e o maior gasto")
            print("[2] - Exibir todos os dados da planilha")
            print("[3] - Buscar por deputado(a) e exibir relatorio")
            print("-------------------------------------")
            print("[0] - Sair\n")
            value = input()
            self._execute_action(value)

    def _execute_action(self, value):
        if function_execute := self.options.get(value, None):
            function_execute()
