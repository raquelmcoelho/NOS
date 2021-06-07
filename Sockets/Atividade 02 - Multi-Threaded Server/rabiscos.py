"""
jogo em si:
cada jogador tem sua visão das cartas
cartas jogadas ficam no centro e todos veêm
tem um sentido de jogo
tem as cartas a serem puxadas
ou mesma cor ou mesmo número
cartas especiais
observadorvitoria
"""
"""
SALA NÚMERO 9998
nickname:[               ]
[entrar]

"""
"""
    SEJA BEM VINDO AO UNO
      [COMEÇAR JOGO]
          [sair]
   
O jogador Raquel entrou na sala
O jogador Yuri entrou na sala
"""
"""
Se maior de 7:

Não é possível entrar na partida, 
ela atingiu seu limite máximo de jogadores
"""

"""
 [UNO] [3-amarelo]
"""
"""
estas serão suas cartas:
[
VERMELHA - 9
AMARELA - zero
VERDE - 3
PRETA +4
PRETA 4CORES
AMARELA - maisdois
]
"""
"""
JOGADOR Yuri VENCEU!!
"""

"""
CAMINHOS DE TESTES 
- travar e embaralhar tudo de novo
- mostrar os request 1 so dps q o 2 ja tiver terminado
- escrever quando ta lockado (eita c gui dava oh)

 """
l2 = ["a", "b", "c", "d", "e"]
vez = 6
posicao = (vez % len(l2))
substituto = []

for i in range(len(l2)):
    substituto.append(l2[posicao - 1])
    posicao -= 1

l2 = substituto
print(l2)