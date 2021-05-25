"""
3. Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
    1. Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
        2. tipoCombustivel.
        3. valorLitro
        4. quantidadeCombustivel
    5. Possua no mínimo esses métodos:
        6. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que
        foi colocada no veículo
        7. abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser
        pago pelo cliente.
        8. alterarValor( ) – altera o valor do litro do combustível.
        9. alterarCombustivel( ) – altera o tipo do combustível.
        10.alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
    11.OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba
"""


class BombaCombustivel:
    def __init__(self, tipocombustivel, valorlitro, qtdcombustivel, dinheirototal):
        self.type = tipocombustivel
        self.value = float(valorlitro)
        self.qtd = float(qtdcombustivel)
        self.money = float(dinheirototal)

    def abastecerporvalor(self, pagamento):
        if pagamento <= self.money:
            self.money -= pagamento
            litros = pagamento / self.value
            self.qtd += litros
            return litros

        else:
            return "pagamento insuficiente"

    def abastecerporlitro(self, litros):
        pagamento = litros * self.value
        if self.money >= pagamento:
            self.qtd += litros
            self.money -= pagamento
            return pagamento

        else:
            return "essa quantidade de litros não pode ser paga com esse valor"

    def alterarvalor(self, newvalue):
        self.value = newvalue

    def alterarcombustivel(self, newtype):
        self.type = newtype

    def alterarquantidadecombustivel(self, newqtd):
        self.qtd = newqtd

    def __str__(self):
        return """
        Tipo de Combutível: %s
        Preço do Litro: %.2f
        Quantidade de cobustível na reserva: %.2f
        Dinheiro restante: %.2f""" % (self.type, self.value, self.qtd, self.money)


meutanque = BombaCombustivel("gasolina", 5.0, 0, 25)
print(meutanque)
meutanque.abastecerporvalor(10)
print("\nAbastecer 10 reais:", meutanque)
meutanque.abastecerporlitro(3)
print("\nAbastecer 3 litros:", meutanque)
meutanque.alterarvalor(6)
print("\nAlterou valor:", meutanque)
meutanque.alterarcombustivel("Diesel")
print("\nAlterou combustível:", meutanque)
meutanque.alterarquantidadecombustivel(12)
print("\nAlterou QTD de combustível:", meutanque)
