class Funcionario:
    def __init__(self, nome, matricula, salario_base):
        self.nome = nome
        self.matricula = matricula
        self.__salario_base = salario_base

    def get_salario_base(self):
        return self.__salario_base

    def set_salario_base(self, novo_salario):
        if novo_salario > 0:
            self.__salario_base = novo_salario
            return True
        return False

    def calcular_salario_final(self):
        return self.__salario_base


class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario_base, bonus_gestao):
        super().__init__(nome, matricula, salario_base)
        self.bonus_gestao = bonus_gestao

    def calcular_salario_final(self):
        return self.get_salario_base() + self.bonus_gestao


class Desenvolvedor(Funcionario):
    def __init__(self, nome, matricula, salario_base, nivel):
        super().__init__(nome, matricula, salario_base)
        self.nivel = nivel

    def calcular_salario_final(self):
        if self.nivel == "Senior":
            return self.get_salario_base() + 1500
        return self.get_salario_base()


gerente = Gerente("Maria Souza", "G-101", 8000, 2000)
desenvolvedor = Desenvolvedor("João Silva", "D-202", 6000, "Senior")

gerente.__salario_base = -100

autoridade = Funcionario("Ana Paula", "F-001", 3500)
autoridade.__salario_base = -200

print(f"{gerente.nome} - Salário final: R$ {gerente.calcular_salario_final():.2f}")
print(f"{desenvolvedor.nome} - Salário final: R$ {desenvolvedor.calcular_salario_final():.2f}")
print(f"Salário base do gerente após tentativa direta: R$ {gerente.get_salario_base():.2f}")
print(f"Salário base do funcionário após tentativa direta: R$ {autoridade.get_salario_base():.2f}")
