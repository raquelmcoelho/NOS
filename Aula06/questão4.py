"""4. Procure no texto apontado no link todas as ocorrências números percentuais. https://
www.uol/economia/especiais/energia-solar-e-eolica-.htm#de-vento-em-popa
5. Encontre todos as contas do Instagram indicadas no texto do link. http://
www.businessinsider.com/instagram-top-10-people-2017-2017-11
"""

import re
with open("uol", "r") as f:
    print("porcentagens encontrada no link 1:")
    print(re.findall("\d*.\d*%", f.read()))

with open("instagram", "r") as f2:
    print("\ncontas do instagram encontradas no segundo link:")
    print(re.findall("@.*,", f2.read()))