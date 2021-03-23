"""AULA 03 ENCODING
#1. Dada a string “A persistência é o caminho do êxito” codifique-a utilizando UTF-8
e UTF-16.
1.1.O que acontece em cada caso? Justifique. R- mulher codifica para bytes no padrão de cada respectiva utf
1.2.Qual a diferença de tamanho entre as saídas em UTF-8 e UTF-16? grande
1.3.Tente realizar a codificação/decodificação cruzada. O que acontece?
a = "A persistência é o caminho do êxito"
b = a.encode()
c = a.encode("utf-16")
b= b.decode() #decodificar
print("\noriginal:", a,"\nutf-8:", b ,"\nutf-16:", c)

2. Decodifique a sequência de bytes:
2.1.

print(b'\xff\xfeA\x00 \x00p\x00e\x00r\x00s\x00i\x00s\x00t\x00\xea\x00n\x00c\x00i\x00a\x00 \x00\xe9\x00 \x00o\x00 \x00c\x00a\x00m\x00i\x00n\x00h\x00o\x00 \x00d\x00o\x00 \x00\xea\x00x\x00i\x00t\x00o\x00'.decode("utf-16"))

2.2.Qual seu conteúdo? Foi possível decodificar? Qual a codificação correta?
A persistencia é o cmainho de exito, utf-16

3. Tente decodificar a nova sequência:
b'
print(b'\xff\xfeA\x00p\x00r\x00e\x00n\x00d\x00e\x00n\x00d\x00o\x00 \x00p\x00r\x00o\x00g\x00r\x00a\x00m\x00a\x00\xe7\x00\xe3\x00o\x00 \x00e\x00m\x00 \x00P\x00y\x00t\x00h\x00o\x00n\x00'.decode("utf-16"))
aprendendo programação em python

4. O que acontece se for utiliza a codificação errada? Explique o erro mostrado.
dá erro ou mapeia errado

5. Como evitar o erro (UnicodeDecodeError:) do ítem anterior utilizando o
parâmetro ‘replace' ou ‘ignore' do método encode? Pesquise no site
python.org. Diferencie-os.
txt= b'\xff\xfeA\x00p\x00r\x00e\x00n\x00d\x00e\x00n\x00d\x00o\x00 \x00p\x00r\x00o\x00g\x00r\x00a\x00m\x00a\x00\xe7\x00\xe3\x00o\x00 \x00e\x00m\x00 \x00P\x00y\x00t\x00h\x00o\x00n\x00'
print(txt.decode("utf-8", errors="replace"))
print(txt.decode("utf-8", errors="ignore"))
"""


