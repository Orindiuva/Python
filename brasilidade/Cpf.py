from validate_docbr import CPF

class Cpf:

    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_eh_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")

    def __str__(self):
        return self.formata_cpf()

    def cpf_eh_valido(self, cpf):
        tamanho = len(cpf)
        if tamanho == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de digitos invalida!")


    def formata_cpf(self):
        #fatia_um = self.cpf[:3]
        #fatia_dois = self.cpf[3:6]
        #fatia_tres = self.cpf[6:9]
        #fatia_quatro = self.cpf[9:]
        #cpf_formatado = "{}.{}.{}-{}".format(fatia_um, fatia_dois, fatia_tres, fatia_quatro)
        #return cpf_formatado
        cpf = CPF()
        return cpf.mask(self.cpf)


