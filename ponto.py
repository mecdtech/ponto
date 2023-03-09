import datetime

class Ponto:
    def __init__(self, id, nome, hora_entrada, hora_saida):
        self.id = id
        self.nome = nome
        self.hora_entrada = hora_entrada
        self.hora_saida = hora_saida
        self.lista_ponto = []

    def registrar_entrada(self):
        self.id = len(self.lista_ponto) + 1
        self.nome = input("Digite seu nome: ")
        hora_atual = datetime.datetime.now().strftime("%H:%M:%S")
        self.hora_entrada = hora_atual
        self.lista_ponto.append(Ponto(self.id, self.nome, self.hora_entrada, ""))
        print(f"Entrada registrada com sucesso às {hora_atual}.")

    def registrar_saida(self):
        nome = input("Digite seu nome: ")
        encontrado = False
        for ponto in self.lista_ponto:
            if ponto.nome == nome and ponto.hora_saida == "":
                hora_atual = datetime.datetime.now().strftime("%H:%M:%S")
                ponto.hora_saida = hora_atual
                encontrado = True
                print(f"Saida registrada com sucesso às {hora_atual}.")
        if not encontrado:
            print("Não foi possível registrar a saída.")

    def visualizar_relatorio(self):
        nome = input("Digite o nome do funcionário: ")
        encontrado = False
        for ponto in self.lista_ponto:
            if ponto.nome == nome:
                encontrado = True
                print(f"\nID: {ponto.id}")
                print(f"Nome: {ponto.nome}")
                print(f"Hora de entrada: {ponto.hora_entrada}")
                print(f"Hora de saída: {ponto.hora_saida}")
        if not encontrado:
            print("Não foi possível encontrar o relatório de ponto desse funcionário.")



def menu():
    ponto = Ponto(0, "", "", "")
    while True:
        print("\n== MENU ==")
        print("1 - Registrar entrada")
        print("2 - Registrar saída")
        print("3 - Visualizar relatório de ponto")
        print("4 - Sair")
        opcao = int(input("Digite uma opção: "))
        if opcao == 1:
            ponto.registrar_entrada()
        elif opcao == 2:
            ponto.registrar_saida()
        elif opcao == 3:
            ponto.visualizar_relatorio()
        elif opcao:
            pass


if __name__ == "__main__":
    menu().iniciar()