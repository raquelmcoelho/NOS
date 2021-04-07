print("1. Dada a string “A persistência é o caminho do êxito” codifique-a utilizando UTF-8 e UTF-16")

a = "A persistência é o caminho do êxito"
b = a.encode()
c = a.encode("utf-16")
print("\noriginal:", a, "\nutf-8:", b, "\nutf-16:", c)

b = b.decode()
c = c.decode("utf-16")
print("\ndecodificados:\nutf-8:", b, "\nutf-16:", c)
