#Projeto FP Jogo do Galo ist199202 Diogo Godinho Melita

def eh_tabuleiro(tab):
    '''Esta funcao recebe um argumento de qualquer tipo e devolve TRUE se 
    o argumento corresponde a um tabuleiro e FALSE em caso contrario, sem 
    nunca gerar erros. '''
    
    if not type(tab) == tuple:
        return False
    if len(tab) != 3:
        return False
    for linha in tab:
        if not isinstance(linha, tuple):
            return False
        if len(linha) != 3:
            return False
        for i in (linha):
            if not type(i) == int:
                return False
            if not -1 <= i <= 1:
                return False
    return True

def eh_posicao(n):
    ''' Esta funcao recebe um argumento de qualquer tipo e devolve True se 
    o argumento corresponde a uma posicao e False em caso contrario, sem
    nunca gerar erros. '''
    
    if not type(n) == int:
        return False
    if not 1 <= n <= 9:
        return False
    return True

def obter_coluna(tab, n):
    ''' Esta funcao recebe um tabuleiro e um inteiro com valor de 1 a 3 que
    representa o numero da coluna, e devolve um vetor com os valores dessa
    coluna. Se algum dos argumentos dados for invalido a funcao deve gerar
    um erro com a mensagem 'obter_coluna: algum dos argumentos e invalido'. '''
    
    if not eh_tabuleiro(tab):
        raise ValueError('obter_coluna: algum dos argumentos e invalido')
    if not type(n) == int or not 1 <= n <= 3:
        raise ValueError('obter_coluna: algum dos argumentos e invalido')
    resultado = ()
    for linha in tab:
        resultado = resultado + (linha[n-1],)
    return resultado

def obter_linha(tab, n):
    '''Esta funcao recebe um tabuleiro e um inteiro com valor de 1 a 3 que
    representa o numero da linha, e devolve um vetor com os valores dessa
    linha. Se algum dos argumentos dados for invalido a funcao deve gerar
    um erro com a mensagem 'obter_linha: algum dos argumentos e invalido'. '''
    
    if not eh_tabuleiro(tab):
        raise ValueError('obter_linha: algum dos argumentos e invalido')
    if not type(n) == int or not 1 <= n <= 3:
        raise ValueError('obter_linha: algum dos argumentos e invalido')
    return tab[n-1]

def obter_diagonal(tab, n):
    '''Esta funcao recebe um tabuleiro e um inteiro que representa a direcao da
    diagonal, 1 para descendente da esquerda para a direita e 2 para ascendente
    da esquerda para a direita e devolve um vetor com os valores dessa
    diagonal. Se algum dos argumentos dados for invalido a funcao deve gerar
    um erro com a mensagem 'obter_diagonal: algum dos argumentos dados e 
    inavalido'. '''
    
    if not eh_tabuleiro(tab):
        raise ValueError('obter_diagonal: algum dos argumentos e invalido')
    if not type(n) == int or not 1 <= n <= 2:
        raise ValueError('obter_diagonal: algum dos argumentos e invalido')
    if n == 1:
        return (tab[0][0], tab[1][1], tab[2][2])
    if n == 2:
        return (tab[2][0], tab[1][1], tab[0][2])
    
def tabuleiro_str(tab):
    '''Esta funcao recebe um tabuleiro e devolve a cadeia de caracteres que o 
    representa (representacao para "os nossos olhos"). Se o argumento dado for
    invalido a funcao deve gerar um erro com a mensagem 'tabuleiro_str: o 
    argumento e invalido'.'''
    
    if not eh_tabuleiro(tab):
        raise ValueError('tabuleiro_str: o argumento e invalido')
    string = ''
    j = 0
    while j < len(tab):
        i = 0
        for linha in tab:
            while i < len(linha):
                if tab[j][i] == 0:
                    string = string + '   '
                if tab[j][i] == 1:
                    string = string + ' X '
                if tab[j][i] == -1:
                    string = string + ' O '
                if i < 2:
                    string = string + '|'
                i = i + 1        
        if j < 2:
            string = string + '\n-----------\n'
        j = j + 1
    return string

def eh_posicao_livre(tab, n):
    '''Esta funcao recebe um tabuleiro e uma posicao e devolve TRUE se a
    possicao corresponde a uma posicao livre do tabuleiro e FALSE em caso
    contrario. Se algum dos argumentos dados for invalido, a funcao deve gerar
    um erro com a mensagem 'eh_posicao_livre: algum dos argumentos e invalido'.
    '''
    
    if not eh_tabuleiro(tab):
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')
    if not type(n) == int or not 1 <= n <= 9:
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')
    
    if n % 3 == 0: # posicoes 3, 6, 9
        j = n // 3 - 1
        i = 2
    elif n % 3 == 1: # posicoes 1, 4, 7
        j = n // 3
        i = 0
    elif n % 3 == 2: # posicoes 2, 5, 8
        j = n // 3
        i = 1 
    
    return tab[j][i] == 0

def obter_posicoes_livres(tab):
    '''Esta funcao recebe um tabuleiro, e devolve o vetor ordenado com todas as
    posicoes livres do tabuleiro. Se o argumento dado for invalido, a funcao 
    deve gerar um erro com a mensagem ' obter_posicoes_livres: o argumento e 
    invalido'. '''
    
    if not eh_tabuleiro(tab):
        raise ValueError('obter_posicoes_livres: o argumento e invalido')
    res = ()
    n = 1
    while n <= 9:
        if eh_posicao_livre(tab, n):
            res = res + (n,)
        n = n + 1
    return res

def jogador_ganhador(tab):
    '''Esta funcao recebe um tabuleiro e devolve um valor inteiro a indicar o
    jogador que ganhou a partida  no tabuleiro passado por argumento, sendo o
    valor igual a 1 se ganhou o jogador que joga com 'X', -1 se ganhou o jogador
    que joga com 'O' ou 0 se nao ganhou nenhum jogador. Se o argumento dado for
    invalido, a funcao deve gerar um erro com a mensagem 'jogador_ganhador: o
    argumento e invalido'.'''
    
    if not eh_tabuleiro(tab):
        raise ValueError('jogador_ganhador: o argumento e invalido')
    n = 1
    
    while n <= 2:
        if obter_linha(tab, n)[0] == obter_linha(tab, n)[1] == \
           obter_linha(tab, n)[2]:
            return obter_linha(tab, n)[0]
        elif obter_coluna(tab, n)[0] == obter_coluna(tab, n)[1] == \
             obter_coluna(tab, n)[2]:
            return obter_coluna(tab, n)[0]
        elif obter_diagonal(tab, n)[0] == obter_diagonal(tab, n)[1] == \
             obter_diagonal(tab, n)[2]:
            return obter_diagonal(tab, n)[0]
        n = n + 1
    n = 3
    if obter_linha(tab, n)[0] == obter_linha(tab, n)[1] == \
       obter_linha(tab, n)[2]:
        return obter_linha(tab, n)[0]
    elif obter_coluna(tab, n)[0] == obter_coluna(tab, n)[1] == \
         obter_coluna(tab, n)[2]:
        return obter_coluna(tab, n)[0]
    
    return 0

def marcar_posicao(tab, jogador, n):
    '''Esta funcao recebe um tabuleiro, um inteiro identificando um jogador
    (1 para o jogador 'X' e -1 para o jogador 'O') e uma posicao LIVRE e
    devolve um novo tabuleiro modificado com uma nova marca do jogador nessa 
    posicao. Se algum dos argumentos dados for invalido, a funcao deve gerar um
    erro com a mensagem 'marcar_posicao; algum dos argumentos e invalido'.'''
    
    if not eh_tabuleiro(tab):
        raise ValueError('marcar_posicao: algum dos argumentos e invalido')
    if not type(jogador) == int:
        raise ValueError('marcar_posicao: algum dos argumentos e invalido')
    if jogador != -1 and jogador != 1:
        raise ValueError('marcar_posicao: algum dos argumentos e invalido')
    if not type(n) == int:
        raise ValueError('marcar_posicao: algum dos argumentos e invalido')    
    if not 1 <= n <= 9:
        raise ValueError('marcar_posicao: algum dos argumentos e invalido')    
    if n not in obter_posicoes_livres(tab):
        raise ValueError('marcar_posicao: algum dos argumentos e invalido')    
    
    nova_linha = ()
    novotab = ()
    
    n = n - 1 # garantir que n = 3, 6 ou 9 nao aparece em duas condicoes
    
    if n // 3 == 0: #1 linha
        nova_linha = (tab[0][0:n]) + (jogador,) + (tab[0][n+1:3])
        novotab = (nova_linha,) + (tab[1:3])
        
        # n+1 devolve o valor inicial a n
        
    if n // 3 == 1: #2 linha
        n = n - 3 # garante que o indice do tuplo ira ficar entre 0 e 2
        nova_linha = (tab[1][0:n]) + (jogador,) + (tab[1][n+1:3])  
        novotab = (tab[0],) + (nova_linha,) + (tab[2],)
        
    if n // 3 == 2: #3 linha
        n = n - 6 # garante que o indice do tuplo fica entre 0 e 2
        nova_linha = (tab[2][0:n]) + (jogador,) + (tab[2][n+1:3])
        novotab = (tab[0:2]) + (nova_linha,) 
    
    return novotab

def escolher_posicao_manual(tab):
    '''Esta funcao realiza a leitura de uma posicao introduzida manualmente por 
    um jogador e devolve esta posicao escolhida. Se o argumento dado for 
    invalido a funcao deve gerar um erro com a mensagem 'escolher_posicao_manual
    : o argumento e invalido'. A funcao apresenta a mensagem 'Turno do jogador. 
    Escolha uma posicao livre: ', para pedir ao utilizador para introduzir uma
    posicao livre. Se o valor introduzido nao corresponder a uma funcao livre do
    tabuleiro a funcao deve gerar um erro com a mensagem 'escolher_posicao_manu-
    al: a posicao introduzida e invalida'. '''
    
    if not eh_tabuleiro(tab):
        raise ValueError('escolher_posicao_manual: o argumento e invalido')
    
    posicao = eval(input('Turno do jogador. Escolha uma posicao livre: '))
    
    if not eh_posicao(posicao):
        raise ValueError('escolher_posicao_manual: a posicao introduzida' + \
                         ' e invalida')                
    
    if not type(posicao) == int:
        raise ValueError('escolher_posicao_manual: a posicao introduzida' + \
                         ' e invalida')        
    
    if posicao not in obter_posicoes_livres(tab):
        raise ValueError('escolher_posicao_manual: a posicao introduzida' + \
                         ' e invalida')
    return posicao

def escolher_posicao_auto(tab, pc, modo):
    '''Esta funcao recebe um tabuleiro, um inteiro identificando um jogador
    (1 para o jogador 'X' e -1 para o jogador 'O') e uma cadeia de caracteres 
    correspondente a estrategia e devolve a posicao escolhida automaticamente
    de acordo com a estrategia selecionada. Se algum dos argumentos dados for
    invalido, a funcao deve gerar um erro com a mensagem 'escolher_posicao_auto:
    algum dos argumentos e invalido'.'''
    
    if not eh_tabuleiro(tab):
        raise ValueError('escolher_posicao_auto: algum dos argumentos e ' \
                         + 'invalido')
    if not type(pc) == int:
        raise ValueError('escolher_posicao_auto: algum dos argumentos e ' \
                         + 'invalido')        
    if pc != 1 and pc != -1:
        raise ValueError('escolher_posicao_auto: algum dos argumentos e ' \
                         + 'invalido')
    if modo != 'basico' and modo != 'normal' and modo != 'perfeito':
        raise ValueError('escolher_posicao_auto: algum dos argumentos e ' \
                         + 'invalido')
    
    if modo == 'basico':
        return epa_basico(tab, pc)
    if modo == 'normal':
        return epa_normal(tab, pc)
    if modo == 'perfeito':
        return epa_perfeito(tab, pc)
    
def cantos(tab):
    if tab[0][0] == 0:
        return 1
    elif tab[0][2] == 0:
        return 3
    elif tab[2][0] == 0:
        return 7
    elif tab[2][2] == 0:
        return 9

def cantos_possivel(tab):
    '''Esta funcao verifica se a funcao cantos retorna algum valor, se sim 
    retorna TRUE'''
    if cantos(tab) == None:
        return False
    return True

def laterais(tab):
    if tab[0][1] == 0:
        return 2
    elif tab[1][0] == 0:
        return 4
    elif tab[1][2] == 0:
        return 6
    elif tab[2][1] == 0:
        return 8    

def laterais_possivel(tab):
    '''Esta funcao verifica se a funcao laterais retorna algum valor, se sim
    retorna TRUE'''
    if laterais(tab) == None:
        return False
    return True

def epa_basico(tab, pc): #epa = escolher posicao auto
    #centro livre
    if tab[1][1] == 0: #posicao 5
        return 5
    
    #cantos
    elif cantos_possivel(tab):
        return cantos(tab)
                    
    #laterais
    elif laterais_possivel(tab):
        return laterais(tab)
    
def canto_oposto(tab, pc):
    if tab[0][0] == 0 and tab[2][2] != pc and tab[2][2] != 0:
        return 1
    elif tab[0][2] == 0 and tab[2][0] != pc and tab[2][0] != 0:
        return 3
    elif tab[2][0] == 0 and tab[0][2] != pc and tab[0][2] != 0:
        return 7
    elif tab[2][2] == 0 and tab[0][0] != pc and tab[0][0] != 0:
        return 9

def canto_oposto_possivel(tab, pc):
    '''Esta funcao verifica se a funcao canto oposto retorna algum valor, se sim
    retorna TRUE'''
    if canto_oposto(tab, pc) == None:
        return False
    return True

def vitoria(tab, pc):
    n = 1
    while n <= 9:
        if eh_posicao_livre(tab, n):
            if jogador_ganhador(marcar_posicao(tab, pc, n)) == pc:
                return n
        n = n + 1

def vitoria_possivel(tab, pc):
    '''Esta funcao verifica se a funcao vitoria retorna algum valor, se sim
    retorna TRUE'''
    if vitoria(tab, pc) == None:
        return False
    return True

def bloqueio(tab, pc):
    if pc == 1:
        n = 1
        while n <= 9:
            if eh_posicao_livre(tab, n):
                if jogador_ganhador(marcar_posicao(tab, -1, n)) == -1:
                    return n
            n = n + 1
    
    if pc == -1:
        n = 1
        while n <= 9:
            if eh_posicao_livre(tab, n):
                if jogador_ganhador(marcar_posicao(tab, 1, n)) == 1:
                    return n
            n = n + 1
    
def bloqueio_possivel(tab, pc):
    '''Esta funcao verifica se a funcao bloqueio retorna algum valor, se sim 
    retorna TRUE'''    
    if bloqueio(tab, pc) == None:
        return False
    return True

def epa_normal(tab, pc): # epa = escolher posicao auto
    #vitoria
    if vitoria_possivel(tab, pc):
        return vitoria(tab, pc)
    
    #bloqueio
    elif bloqueio_possivel(tab, pc):
        return bloqueio(tab, pc)
            
    #centro livre
    elif tab[1][1] == 0: #posicao 5
        return 5
            
    #canto oposto
    elif canto_oposto_possivel(tab, pc):
        return canto_oposto(tab, pc)
            
    #cantos
    elif cantos_possivel(tab):
        return cantos(tab)
                    
    #laterais
    elif laterais_possivel(tab):
        return laterais(tab)
    
def epa_perfeito(tab, pc):
    #vitoria
    if vitoria_possivel(tab, pc):
        return vitoria(tab, pc)
    
    #bloqueio
    elif bloqueio_possivel(tab, pc):
        return bloqueio(tab, pc)
            
    #centro livre
    elif tab[1][1] == 0: #posicao 5
        return 5
            
    #canto oposto
    elif canto_oposto_possivel(tab, pc):
        return canto_oposto(tab, pc)
            
    #cantos
    elif cantos_possivel(tab):
        return cantos(tab)
                    
    #laterais
    elif laterais_possivel(tab):
        return laterais(tab)    
    
def jogo_do_galo(jogador, estrategia):
    '''Esta funcao corresponde a funcao principal que permite jogar um jogo 
    completo de Jogo do Galo de um jogador contra o computador. O jogo comeca 
    sempre com o jogador 'X' a marcar uma posicao livre e termina quando um dos
    jogadores vence ou, se nao existem posicoes livres no tabuleiro. A funcao 
    recebe duas cadeias de caracteres e devolve o identificador do jogador 
    ganhador 'X' ou 'O'). Em caso de empate, a funcao deve devolver a cadeia de 
    caracteres 'EMPATE'. O primeiro argumento corresponde a marca ('X' ou 'O') 
    que deseja utilizar o jogador humano e o segundo argumento seleciona a 
    estrategia de jogo utilizada pela maquina. Se algum dos argumentos dados for
    invalido, a funcao deve gerar um erro com a mensagem 'jogo_do_galo: algum 
    dos argumentos e invalido'. A funcao deve apresentar a mensagem 'Turno do 
    computador (<estrategia>):' em que <estrategia> corresponde a cadeia de 
    caracteres passada como argumento, quando for o turno do computador'''
    
    if jogador != 'X' and jogador != 'O':
        raise ValueError('jogo_do_galo: algum dos argumentos e invalido')
    if estrategia != 'basico' and estrategia != 'normal' and \
       estrategia != 'perfeito':
        raise ValueError('jogo_do_galo: algum dos argumentos e invalido')
    
    print("Bem-vindo ao JOGO DO GALO.\nO jogador joga com " + "'" + jogador +\
          "'.")
    
    if jogador == 'O':
        jogador = -1
    elif jogador == 'X':
        jogador = 1

    
    tab = ((0, 0, 0), (0, 0, 0), (0, 0, 0)) # tabuleiro inicial
    
    while jogador_ganhador(tab) == 0:
        if jogador == -1:
            pc = 1
            print('Turno do computador ({}):'.format(estrategia))
            
            tab = marcar_posicao(tab, pc, escolher_posicao_auto(tab, pc, \
                                                                estrategia))
            print(tabuleiro_str(tab))
            
            if obter_posicoes_livres(tab) == ():
                return 'EMPATE'
            if jogador_ganhador(tab) == -1:
                return 'O'
            if jogador_ganhador(tab) == 1:
                return 'X'            
            
            tab = marcar_posicao(tab, jogador, escolher_posicao_manual(tab))
        
            print(tabuleiro_str(tab))
            
            if obter_posicoes_livres(tab) == ():
                return 'EMPATE'
            if jogador_ganhador(tab) == -1:
                return 'O'
            if jogador_ganhador(tab) == 1:
                return 'X'            
            
        elif jogador == 1:
            pc = -1
            tab = marcar_posicao(tab, jogador, escolher_posicao_manual(tab))
            print(tabuleiro_str(tab))
            
            if obter_posicoes_livres(tab) == ():
                return 'EMPATE'
            if jogador_ganhador(tab) == -1:
                return 'O'
            if jogador_ganhador(tab) == 1:
                return 'X'            
            
            print('Turno do computador ({}):'. format(estrategia))
            tab = marcar_posicao(tab, pc, escolher_posicao_auto(tab, pc, \
                                                                estrategia))
            print(tabuleiro_str(tab))
            
            if obter_posicoes_livres(tab) == ():
                return 'EMPATE'
            if jogador_ganhador(tab) == -1:
                return 'O'
            if jogador_ganhador(tab) == 1:
                return 'X'