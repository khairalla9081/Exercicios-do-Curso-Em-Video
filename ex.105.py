def notas(*nt, sit=False):
    """
    -> Função para analizar notas e situações de vários alunos:
    :nt: Recebe uma quantidade indeterminada de números.
    :sit: sit=True Mostra a situação da turma.
    :return: Retorna o diconário com as informações.
    """
    info = {
        'total':len(nt),
        'maior':max(nt),
        'menor':min(nt),
        'media':sum(nt) / len(nt) # média no dicionário
    }

    if info['media'] <= 4.9:
        info['situação'] = 'RUIM'
    elif info['media'] >= 5.0 and info['media'] <= 6.9:
        info['situação'] = 'RAZUAVEL'
    else:
        info['situação'] = 'BOA'

    return info


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
#help(notas)