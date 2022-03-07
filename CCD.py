# r -> Ler w -> Escrever a -> Acrescentar

import os

def conversor(quantidade_bytes):
    #Realizando conversão 1 megabyte = 1048576 bytes
    return str(round(quantidade_bytes/1048576, 2)).replace('.', ',')

def porcentagem(espaco_usado, total):
    return str(round(espaco_usado*100/total,2)).replace('.', ',')

if os.path.exists('usuarios.txt'):
    usuarios_espacos_txt = open('usuarios.txt', 'r')
    usuarios_espacos = usuarios_espacos_txt.read().split('\n')

    if len(usuarios_espacos) > 0:
        arquivo_relatorio = open('relatorio.txt', 'wt')
        arquivo_relatorio.write('ACME Inc.           Uso do espaço em disco pelos usuários\n')
        arquivo_relatorio.write('-' * 72 + '\n')

        arquivo_relatorio.write('Nr.'.ljust(5))
        arquivo_relatorio.write('Usuário'.ljust(15))
        arquivo_relatorio.write('Espaço Utilizado'.ljust(21))
        arquivo_relatorio.write('% Do Uso'.ljust(9) + '\n\n')

        espaco_total = 0
        for usuario_espaco in usuarios_espacos:
            espaco_total += int(usuario_espaco.split()[1])

        for indice_usuario_espaco in range(len(usuarios_espacos)):
            usuario_espaco = usuarios_espacos[indice_usuario_espaco].split()

            usurio = usuario_espaco[0]
            espaco = usuario_espaco[1]

            arquivo_relatorio.write(str(indice_usuario_espaco+1).ljust(5))
            arquivo_relatorio.write(usurio.ljust(15))
            arquivo_relatorio.write(conversor(int(espaco)).rjust(7) + 'MB            ')
            arquivo_relatorio.write(porcentagem(int(espaco), espaco_total).ljust(7) + '%\n')

        arquivo_relatorio.write('\nEspaço total ocupado: ' + conversor(espaco_total) + "MB\n")
        arquivo_relatorio.write('Espaço Médio Ocupado: ' + conversor(espaco_total/len(usuarios_espacos)) + 'MB')

        arquivo_relatorio.close()
else:
    print('Arquivo não Existe')






