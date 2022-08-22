from Models.Cliente import Cliente
from Models.Conta import Conta


pedro: Cliente = Cliente('Pedro','phmirandanifera@gmail.com','123.123.123-00','06/01/2004')

#print(pedro)

contap:Conta = Conta(pedro)

print(contap)