# MEU PROGRAMA
# from datetime import datetime
# def voto(year):  
#     if ida >= 18 and ida < 60:
#         sit = "VOTO OBRIGATORIO"
#         return sit
#     if ida >= 16 and ida < 18 or ida >= 65:
#         sit = "VOTO OPCIONAL"
#         return sit
#     else:
#         sit = "NÃO VOTA"
#         return sit

# nasc = int(input('Digite o seu ano de nascemento: '))
# atual = datetime.today().year
# ida = atual - nasc
# print(f'Com {ida} anos: {voto(nasc)} ')
# --------------------------------------------------------
# PROGRAMA DO GUANABARA
def voto(ano):
    """
    -> voto(year) This function will recibe 
    :year: The day of your birth
    """
    from datetime import date # Escopo de importação
    atual = date.today().year
    idade = atual - ano

    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.' 


nasc = int(input('Digite seu ano de nascimento: '))
print(voto(nasc))
# help(voto)