from datetime import datetime


class SistemaBancario:
    def __init__(self, contas):
        self.contas = contas
        self.agencia = "0001"
        self.quantidade_contas = len(contas)

    def criar_conta(self, usuario,nome,cpf,saldo_inicial):
        numero_conta = f"{self.agencia}.{str(datetime.now())}"
        usuario = Usuario(nome=nome,cpf=cpf,saldo_inicial=saldo_inicial,numero_conta=numero_conta)
        self.usuarios.append(usuario)
        self.quantidade_contas = self.quantidade_contas + 1

    def filtrar_contas_por_cpf(self,cpf):
        for conta in self.contas:
            if conta.cpf == cpf:
                return conta
        return "conta não encontrada"

    def filtrar_contas_por_nome(self,nome):
        for conta in self.contas:
            if conta.nome == nome:
                return conta
        return "conta não encontrada"


class Usuario:
    def __init__(self, nome,cpf, saldo_inicial,numero_conta):
        self.nome = nome
        self.cpf = cpf
        self.numero_conta = numero_conta
        self.saldo = saldo_inicial
        self.dia_atual = datetime.today()
        self.saques_restantes = 3
        self.extrato = []

    def depositar(self, valor_deposito):
        if valor_deposito > 0:
            self.saldo = self.saldo + valor_deposito
            operacao = {"operacao": "deposito", "valor": valor_deposito}
            self.extrato.append(operacao)
        else:
            print("valor de deposito invalido")

    def sacar(self, valor_a_sacar):
        if self.saques_restantes > 0:
            if valor_a_sacar <= 500 and valor_a_sacar > 0:
                if valor_a_sacar <= self.saldo:
                    self.saldo = self.saldo - valor_a_sacar
                    operacao = {"operacao": "saque", "valor": valor_a_sacar}
                    self.extrato.append(operacao)
                    self.saques_restantes = self.saques_restantes - 1
                else:
                    print("valor de saque invalido")
            else:
                print("valor de saque invalido")
        else:
            print("não permite mais saques hoje")

    def extrato(self):
        return self.extrato

    def mudou_o_dia(self):
        if self.dia_atual != datetime.today():
            self.saques_restantes = 3
            self.dia_atual = datetime.today()

    def imprimir_extrato(self):
        print("Extrato")
        for valores in self.extrato:
            print(f"{valores['operacao']}-{valores['valor']}")
