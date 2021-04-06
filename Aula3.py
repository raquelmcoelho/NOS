# AULA 03 ENCODING
# PRIMEIRA QUESTÃO
print("1. Dada a string “A persistência é o caminho do êxito” codifique-a utilizando UTF-8 e UTF-16")
a = "A persistência é o caminho do êxito"
b = a.encode()
c = a.encode("utf-16")
print("\noriginal:", a, "\nutf-8:", b, "\nutf-16:", c)
b = b.decode()
c = c.decode("utf-16")
print("\ndecodificados:\nutf-8:", b, "\nutf-16:", c)


# SEGUNDA QUESTÃO
print("\n\n", r"2. Decodifique a sequência de bytes: \xff\xfeA\x00 \x00p\x00e\x00r\x00s\x00i\x00s\x00t\x00\xea\x00n"
              r"\x00c\x00i\x00a\x00 \x00\xe9\x00 \x00o\x00 \x00c\x00a\x00m\x00i\x00n\x00h\x00o\x00 \x00d\x00o\x00 \x00"
              r"\xea\x00x\x00i\x00t\x00o\x00")
d = b'\xff\xfeA\x00 \x00p\x00e\x00r\x00s\x00i\x00s\x00t\x00\xea\x00n\x00c\x00i\x00a\x00 \x00\xe9\x00 \x00o\x00 \x00c' \
    b'\x00a\x00m\x00i\x00n\x00h\x00o\x00 \x00d\x00o\x00 \x00\xea\x00x\x00i\x00t\x00o\x00'
print("decodificado:", d.decode("utf-16"))


# TERCEIRA QUESTÃO
print("\n\n", r"3.Tente decodificar a nova sequência:b'\xff\xfeA\x00p\x00r\x00e\x00n\x00d\x00e\x00n\x00d\x00o\x00 "
              r"\x00p\x00r\x00o\x00g\x00r\x00a\x00m\x00a\x00\xe7\x00\xe3\x00o\x00 \x00e\x00m\x00 \x00P\x00y\x00t\x00h"
              r"\x00o\x00n\x00'")
print("decodificado:", b'\xff\xfeA\x00p\x00r\x00e\x00n\x00d\x00e\x00n\x00d\x00o\x00 \x00p\x00r\x00o\x00g\x00r\x00a\x00m'
                       b'\x00a\x00\xe7\x00\xe3\x00o\x00 \x00e\x00m\x00 \x00P\x00y\x00t\x00h\x00o'
                       b'\x00n\x00'.decode("utf-16"))


# QUARTA QUESTÃO
print("\n\n4.Como evitar o erro (UnicodeDecodeError:) utilizando o parâmetro ‘replace' ou ‘ignore' do método encode? ")
txt = b'\xff\xfeA\x00p\x00r\x00e\x00n\x00d\x00e\x00n\x00d\x00o\x00 \x00p\x00r\x00o\x00g\x00r\x00a\x00m\x00a\x00\xe7' \
     b'\x00\xe3\x00o\x00 \x00e\x00m\x00 \x00P\x00y\x00t\x00h\x00o\x00n\x00'
print(txt.decode("utf-8", errors="replace"))
print(txt.decode("utf-8", errors="ignore"))
