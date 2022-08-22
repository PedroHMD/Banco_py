from typing import List
from time import sleep

from Models.Cliente import Cliente
from Models.Conta import Conta

contas: List[Conta] = []

def main() -> None:
    menu()

def menu() -> None:
    print("""
    |=====================================|
    |===========| BancoPy |===============|
    |=====================================|
    |                                     |
    | 1) -> Criar Conta                   |
    | 2) -> efetuar saque                 |
    | 3) -> efetuar deposito              |
    | 4) -> efetuar transferencia         |
    | 5) -> listar contas                 |
    | 6) -> sair                          |
    |                                     |
    |=====================================|    
    """)

    opcao: int = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        Listar_contas()
    elif opcao == 6:
        print("volte sempre !!")
        sleep(2)
        exit(0)
    else:
        print("Opção invalida!!")
        sleep(2)
        menu()


def criar_conta() -> None:

    nome:str = input("Nome do cliente: ")
    email:str = input("email: ")
    cpf: str = input("CPF: ")
    data_nascimento: str = input("data de nascimento: ")

    cliente: Cliente = Cliente(nome,email,cpf,data_nascimento)

    conta:Conta = Conta(cliente)

    contas.append(conta)

    print("Conta criada com sucesso!")
    print("dados da conta:")
    print("==================")

    print(conta)
    sleep(2)
    menu()

def efetuar_saque() -> None:
    if len(contas) > 0:
        numero:int = int(input("Informe o numero da sua conta: "))

        conta:Conta = Buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input("Digite o valor que deseja sacar: "))
            conta.sacar(valor)
        else:
            print(f"Conta de numero:{numero} não foi encontrada!")

    else:
        print("ainda não existem contas cadastradas")
    sleep(2)
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero:int = int(input("Informe o numero da sua Conta: "))

        conta:Conta = Buscar_conta_por_numero(numero)

        if conta:
            valor:float = float(input("Digite o valor que deseja depositar: "))
            conta.depositar(valor)

        else:
            print(f"Conta de numero:{numero} não foi encontrada!")
    else:
        print("ainda não existem contas cadastradas")
    sleep(2)
    menu()

def efetuar_transferencia() -> None:
    if len(contas)> 0:
        nume_o:int = int(input("Informe o numero de sua conta: "))

        conta_o:Conta=Buscar_conta_por_numero(nume_o)

        if conta_o:
            nume_d:int = int(input("Informe o numero da conta que deseja transferir: "))

            conta_d:Conta= Buscar_conta_por_numero(nume_d)

            if conta_d:
                valor:float= float(input("digite o valor que deseja fazer a transferencia:"))
                conta_o.transferir(conta_d,valor)

            else:
                print("conta do destinatario nãofoi encontrada! ")
        else:
            print("Conta de origem não encontrada")
    else:
        print("ainda não existem contas cadastradas")

    sleep(2)
    menu()

def Listar_contas()->None:
    if len(contas) > 0:
        for conta in contas:
            print(conta)
            print("--------------------")
            sleep(2)
    else:
        print("ainda não existem contas cadastradas")
    sleep(2)
    menu()

def Buscar_conta_por_numero(numero:int) -> Conta:
    c:Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta

    return c


if __name__ == "__main__":
    main()