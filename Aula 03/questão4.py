print("4.Como evitar o erro (UnicodeDecodeError:) utilizando o parâmetro ‘replace' ou ‘ignore' do método encode?\n")

txt = b'\xff\xfeA\x00p\x00r\x00e\x00n\x00d\x00e\x00n\x00d\x00o\x00 \x00p\x00r\x00o\x00g\x00r\x00a\x00m\x00a\x00\xe7' \
      b'\x00\xe3\x00o\x00 \x00e\x00m\x00 \x00P\x00y\x00t\x00h\x00o\x00n\x00'
print("replace:", txt.decode("utf-8", errors="replace"))
print("ignore:", txt.decode("utf-8", errors="ignore"))
