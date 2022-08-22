from Models.Cliente import Cliente
from Utils.Helper import Formata_float_moeda

class Conta:
    codigo = 100

    def __init__(self:object,cliente:Cliente) -> None:

        self.__numero: int = Conta.codigo
        self.__cliente:Cliente = cliente
        self.__saldo:float = 0.0
        self.__limite:float = 100.0
        self.__saldo_total:float = self.calcula_s_T
        Conta.codigo += 1

    def __str__(self:object)->str:
        return f'Numero da conta:{self.numero} \nCliente: {self.cliente.nome} \nSaldo Total: {Formata_float_moeda(self.saldo_total)}'

    @property
    def numero(self:object)->int:
        return self.__numero

    @property
    def cliente(self: object) -> Cliente:
        return self.__cliente

    @property
    def saldo(self:object) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self:object,valor:float) -> None:
        self.__saldo = valor

    @property
    def limite(self: object) -> float:
        return self.__limite

    @limite.setter
    def limite(self:object,valor:float) -> None:
        self.__limite = valor

    @property
    def saldo_total(self:object) -> float:
        return self.__saldo_total

    @saldo_total.setter
    def saldo_total(self:object,valor:float) -> None:
        self.__saldo_total = valor

    @property
    def calcula_s_T(self: object) -> float:
        return self.saldo + self.limite

    def depositar(self:object,valor:float) -> None:
        if valor > 0:
            self.saldo = self.saldo + valor
            self.saldo_total = self.calcula_s_T
            print("depósito efetuado com sucesso!")
        else:
            print("erro ao efetuar o depósito, tente novamente")

    def sacar(self:object,valor:float) -> None:
        if valor > 0 and self.saldo_total >= valor:
            if self.saldo >= valor:
                self.saldo =  self.saldo - valor
                self.saldo_total = self.calcula_s_T

            else:
                rest:float = self.saldo - valor
                self.limite = self.limite + rest
                self.saldo = 0
                self.saldo_total = self.calcula_s_T

            print("saque efetuado com sucesso!")
        else:
            print("saque não realizado, tente novamente!")

    def transferir(self:object,destino:object,valor:float) -> float:
        if valor > 0 and self.saldo_total >= valor:
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self.calcula_s_T
                destino.saldo = destino.saldo + valor
                destino.saldo_total = destino.calcula_s_T


            else:
                rest:float = self.saldo - valor
                self.limite = self.limite + rest
                self.saldo = 0
                self.saldo_total = self.calcula_s_T
                destino.saldo = destino.saldo + valor
                destino.saldo_total = destino.calcula_s_T

            print("transferencia feita com sucesso! ")
        else:
            print("transferencia não foi realizada!")