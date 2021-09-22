cidade = str(input('Em qual cidade você nasceu? ')).strip().upper().lower().title()
nome = 'Santo' in cidade
print(nome)

cid = str(input('Em qual cidade você nasceu? ')).strip().upper().lower().title()
print(cid[:5] == 'Santo')