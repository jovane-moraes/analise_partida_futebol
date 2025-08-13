def analisar_partida(gols):
    if gols <= 1:
        classificacao = 'Fraco'
        sugestao = 'Precisa treinar mais.'
        return classificacao, sugestao
    elif gols <= 3:
        classificacao = 'Boa'
        sugestao = 'Tá indo bem, mas dá pra melhorar.'
        return classificacao, sugestao
    else:
        classificacao = 'Excelente'
        sugestao = 'Continue assim, tá jogando muito!'
        return classificacao, sugestao

print('*** Análise de desempenho do time ***')

try:
    quantidade_gols = int(input('\nDigite a quantidade de gols: '))
    desempenho, recomendacao = analisar_partida(quantidade_gols)

    print(f'\nO desempenho foi: {desempenho}')
    print(f'A recomendação é: {recomendacao}')
except ValueError:
    print('\nVocê nao digitou um número. Por favor, reinicie e tente novamente.')

