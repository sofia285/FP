'''
nome: Sofia Paiva   nº 102835    e-mail: sofia.paiva@tecnico.ulisboa.pt
'''
#1.1 - corrigir_palavra
def corrigir_palavra(palavra):
    ''' 
    Recebe que recebe uma string(cadeia de caracteres) codificada e devolve uma string que corresponde à redução da string inicial
    string(input) --> string(output)
    '''
    palavra2 = ""
    problema = False
    for i in range (1,len(palavra)):
        if(problema):
            problema = False
            continue
        
        if (ord(palavra[i])-ord(palavra[i-1]) != 32) and (ord(palavra[i])-ord(palavra[i-1]) != -32):
            palavra2 += palavra[i-1]
        else:
            problema = True
        
    if not problema:
        palavra2 += palavra[len(palavra)-1]
            
    if palavra == palavra2:
        return palavra2
            
    return corrigir_palavra(palavra2)

#1.2 - eh_anagrama
def eh_anagrama(palavra1,palavra2): 
    '''
    Função que recebe duas strings que são duas palavras que podem ser anagramas. a função devolve o valor lógico da comparação das duas palavras.
    string1,string2(input) --> boolean(output)
    '''
    #Utiliza a função lower para meter todas as letras iguais e poder verificar se é anagrama independentemente das letras serem maiúsculas ou não.
    palavra1=palavra1.lower()
    palavra2=palavra2.lower()
    #Utiliza a função sorted para organizar as letras por ordem alfabetica e verificar se contém as mesmas letras.
    return sorted(palavra1) == sorted(palavra2)

#1.3 - corrigir_doc
def mesma_palavra(palavra1,palavra2):
    '''
    Esta função é apenas utilizada como auxiliar da função corrigir_doc.
    A função recebe duas strings e verifica se as palavras são exatamente iguais.
    string1,string2(input) --> boolean(output)
    '''
    palavra1 = palavra1.lower()
    palavra2 = palavra2.lower()
    return palavra1 == palavra2

def corrigir_doc(doc):
    '''
    Esta função utiliza a função mesma_palavra, eh_anagrama e corrigir_palavra para alterar a string inicialmente introduzida e devolve uma string eqivalente à strings inicial corrigida de acordo com os requesitos da BDB.
    string(input) --> string(output)
    '''
    if type(doc)!=str:
        #levanta erro no caso do input não corresponder a uma cadeia de caracteres
        raise ValueError('corrigir_doc: argumento invalido')
    
    doc3 = doc.replace(' ','')
    if not doc3.isalpha():
        #levanta erro no caso da string inicial conter caracteres que não estejam no alfabeto
        raise ValueError('corrigir_doc: argumento invalido')
    doc2 = corrigir_palavra(doc)
    palavras = doc2.split(' ')  
    for palavra in palavras:
        for palavra_errada in palavras:
            if eh_anagrama(palavra,palavra_errada) and not mesma_palavra(palavra,palavra_errada):
                palavras.remove(palavra_errada)
    
    palavras = ' '.join(palavras)
    return palavras
  

#2.1 - obter_posicao       
def obter_posicao(letra,num):
    '''
    Esta função recebe uma string que corresponde a uma direção e recebe também um número inteiro entre 1 e 9. A função devolve um número inteiro que representa ao número inicial após ter sido executado o movimento inserido pelo utilizador.
    string,int(input) --> int(output)
    '''
    pos = num
    if letra == 'E' and (num == 1 or num == 4 or num == 7):
        pos = num
    if letra == 'D' and (num == 3 or num == 6 or num == 9):
        pos = num
    if num >= 1 and num <=3:
        if letra == 'C':
            pos = num
        if letra == 'B':
            pos = num + 3
        if letra == 'E' and num > 1:
            pos = num - 1
        if letra == 'D' and num < 3:
            pos = num +1
    
    if num >= 4 and num <= 6:
        if letra == 'C':
            pos = num - 3
        if letra == 'B':
            pos = num + 3
        if letra == 'E' and num > 4:
            pos = num - 1
        if letra == 'D' and num < 6:
            pos = num + 1
    if num >= 7 and num <= 9:       
        if letra == 'C':
                pos = num -3
        if letra == 'B':
                pos = num
        if letra == 'E' and num > 7:
                pos = num - 1
        if letra == 'D' and num < 9:
                pos = num +1  
    return pos

#2.2 - obter_digito
def obter_digito(frase,num2):
    '''
    Função que recebe uma string que contém um conjunto de direções e recebe também um número inteiro, sobre o qual vão ser aplicadas as direções. Esta função utiliza a função obter_posição para executar cada movimento.
    string,int(input) --> int(output)
    '''
    seq = tuple(frase)
    pos2 = num2
    for i in range(0,len(seq)):
        pos2 = obter_posicao(seq[i],pos2)
        
    return pos2

#2.3 - obter_pin
def obter_pin(pin):
    '''
    Função que recebe um tuplo que contém um conjunto de strings com direções de maneira descodificar um pin. Utiliza a função obter_digito para obter o digito que resulta de cada elemento do tuplo.
    tuple(input) --> tuple(output)
    '''
    tup = ('C','B','D','E')
    if type(pin)!= tuple:
        #Levanta erro se o input for diferente de um tuplo
        raise ValueError('obter_pin: argumento invalido')
    for i in range(0,len(pin)):
        if len(pin[i])==0:
            #Levanta erro se o tuplo inserido for vazio
            raise ValueError('obter_pin: argumento invalido')
        for j in range(0,len(pin[i])):
            if pin[i][j] not in tup:
                #Levanta erro se nas strings existir uma letra que não esteja no tuplo 'tup'
                raise ValueError('obter_pin: argumento invalido')
    pos = (5,)
    if len(pin) < 4 or len(pin) > 10:
        #Levanta erro se o tuplo inserido tiver um nº de elementos inferior a quatro ou superior a 10
        raise ValueError('obter_pin: argumento invalido') 
    
    else:
        for i in range(0,len(pin)):
            pos = pos + (obter_digito(pin[i],pos[i]),)
            
        res = pos[1:]
            
        return res
    
#3.1 e 4.1 - eh_entrada
def eh_entrada(tup):
    '''
    Esta função verifica todos os casos em que o argumento inserido não esteja de acordo com uma entrada BDB.
    tuple(input) --> boolean(output)
    '''
    count = 0
    if type(tup)!= tuple or len(tup)!=3 or type(tup[0])!= str or type(tup[1])!=str or type(tup[2])!=tuple:
        return False    
    if len(tup[1])!=7 or len(tup[2])<2 or (tup[1][0]!= '[' and tup[1][6]!=']'):
        return False
    for i in range(0,len(tup[2])):
        if type(tup[2][i])!= int or tup[2][i]<0:
            return False
    for i in range(0,len(tup[0])):
        if ord(tup[0][i])>=65 and ord(tup[0][i])<=90:
            return False      
    if len(tup)==3 and type(tup[0])==type(tup[1])==str and type(tup[2])==tuple:
        for i in range(0,len(tup[1])):
            if tup[1][i].isalpha():
                count += 1        
        tup2 = tup[0].replace('-','')
        for i in range(0,len(tup2)):
            if not tup2.isalpha() or count!=5:
                return False        
        return True
    return False

#3.2 - validar_cifra
def validar_cifra(cifra,seq):
    '''
    Função recebe uma string que contém uma ou mais palavras codificadas e recebe também uma string que corresponde a uma sequência de controlo. Esta função vai verificar se a sequência(checksum) está de acordo com a string 'cifra' inserida pelo utilizador, devolvendo o seu valor lógico.
    string1,string2(input) --> boolean(output)
    '''
    count = {}
    count2 = {}
    l1=[]
    cifra2 = cifra.replace('-','')
    seq2 = seq.replace('[','')
    seq3 = seq2.replace(']','')
    if not seq3.isalpha() or not cifra2.isalpha():
        return False
    for i in sorted(cifra2):
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    count = dict(sorted(count.items(), key = lambda t: t[1], reverse = True))
    for i in range(5):
        val = list(count.items())[i]
        count2[val[0]] = val[1]
    for i in range(len(seq3)):
        letter = list(count2.items())[i][0]
        if letter != seq3[i]:
            return False
    return True

#3.3 - filtrar_bdb
def filtrar_bdb(l1):
    '''
    Função que recebe uma lista com várias entradas da BDB e verifica se são entradas válidas com a função eh_entrada e verifica também a validade da sequência de controlo(checksum) em relação à cifra com a função validar_cifra. Esta função devolve uma lista que contém as entradas em que o valor lógico da função validar cifra for False, ou seja não pertence a uma entrada da BDB.
    list(input) --> list(output)
    '''
    l2 = []
    if type(l1) != list or len(l1)==0:
        #Levanta erro se o input não corresponder a uma lista ou for uma lista vazia
        raise ValueError('filtrar_bdb: argumento invalido')
    for i in range(0,len(l1)):
        if not eh_entrada(l1[i]):
            #levanta erro no caso dos elementos da lista não serem entradas válidas da BDB
            raise ValueError('filtrar_bdb: argumento invalido')
    for i in range(0,len(l1)):
        if not validar_cifra(l1[i][0],l1[i][1]):       
            l2 += [l1[i],]
    return l2

#4.2 - obter_num_segurança
def obter_num_seguranca(tup):
    '''
    Função que recebe um tuplo que contém dois ou mais números inteiros. Esta função determina a menor diferença entre dois números contidos no tuplo.
    tuple(input) --> int(output)
    '''
    dif=[]
    for i in range(0,len(tup)):
        for j in range(0,len(tup)):
            if tup[i]==tup[j]:
                dif = dif
            else:
                dif += [abs(tup[i]-tup[j])] 
    mindif = min(dif)
    return mindif

#4.3 - decifrar_texto
def decifrar_texto(cifra,num):
    '''
    Função que recebe uma string que corresponde à cifra codificada e um número inteiro que vai ser utilizado para descodificar a cifra.
    string,int(input) --> string(output)
    '''
    cifra3=[]
    min = 97
    for i in range(0,len(cifra)):
        if ord(cifra[i])==45:
            cifra3 += [chr(32)]
            
        elif i%2==0:
            res = min + ((ord(cifra[i])-min + num + 1) % 26)
            cifra3 += [chr(res)]           
        else:
            res = min + ((ord(cifra[i])-min + num - 1) % 26)
            cifra3 += [chr(res)]
    cifra4 = ''.join(cifra3)
    return cifra4

#4.4 - decifrar_bdb
def decifrar_bdb(l1):
    '''
    Função que recebe uma lista que contém várias entradas da BDB e devolve uma lista com as entradas corrigidas. Utiliza a função eh_entrada para verificar se cada entrada inserida é de facto uma entrada válida da BDB, utiliza a função obter_num_segurança para determinar o número de segurança de cada entrada e por último utiliza a função decifrar_texto para corrigir a cifra. No final devolve uma lista com todas as entradas corrigidas.
    list(input) --> list(output)
    '''
    
    if type(l1)!=list:
        #Levanta erro no caso do argumento inserido não ser uma lista
        raise ValueError('decifrar_bdb: argumento invalido')
    for i in range(0,len(l1)):
        if not eh_entrada(l1[i]):
            #Levanta erro no caso de uma das entradas inseridas não corresponder a uma entrada válida da BDB
            raise ValueError('decifrar_bdb: argumento invalido')
    l2 = []
    for i in range(0,len(l1)):
        tup = l1[i][0]
        num = obter_num_seguranca(l1[i][2])
        cifra = decifrar_texto(tup,num)
        l2 += [cifra]
    return l2
    
#5.1 - eh_utilizador
def eh_utilizador(dicionario):
    '''
    Função que verifica se o argumento inserido, com informação de um utilizador, está de acordo com os parâmetros da BDB.
    dict(input) --> boolean(output)
    '''
    if type(dicionario)!=dict or len(dicionario)!=3:
        return False
    if 'name' not in dicionario or 'pass' not in dicionario or 'rule' not in dicionario:
        return False
    if 'vals' not in dicionario['rule'] or 'char' not in dicionario['rule'] or len(dicionario['rule'])!=2:
        return False
    
    if type(dicionario['name']) != str or type(dicionario['pass'])!=str:
        return False 
    if len(dicionario['name'])<1 or len(dicionario['pass'])<1:
        return False
    if type(dicionario['rule']['vals'])!=tuple or len(dicionario['rule']['vals'])!=2:
        return False
    for i in dicionario['rule']['vals']:
        if i<0:
            return False
    if dicionario['rule']['vals'][0] > dicionario['rule']['vals'][1]:
        return False
    if type(dicionario['rule']['char'])!=str or len(dicionario['rule']['char'])!=1:
        return False
    if ord(dicionario['rule']['char']) <97 or ord(dicionario['rule']['char'])>122:
        return False
    return True

#5.2 - eh senha_valida   
def eh_senha_valida(senha,dicionario):
    '''
    Função que uma cadeia de caracteres que corresponde a uma senha e um dicionário que contém a regra individual de criação de senha. Esta função verifica se a senha e a regra individual são válidas e devolve o valor lógico desta verificção.
    string,dict(input) --> boolean(output)
    '''
    senha2 = sorted(senha)
    count = 0
    count_vogais = 0
    count_igual = 0
    dicionario2 = {'vogais': {'a','e','i','o','u'}}
    for j in range (0,len(senha2)):
        if senha2[j] in dicionario2['vogais']:
            count_vogais+=1
        if senha2[j] == dicionario['char']:
            count += 1  
        if senha[j] == senha[j-1]:
            count_igual+= 1
    if count >= dicionario['vals'][0] and count <= dicionario['vals'][1] and count_vogais>=3 and count_igual >= 1:
        return True
    return False
    
#5.3
def filtrar_senhas(dicionarios):
    '''
    Função que recebe uma lista com vários dicionários que correspondem a utilizadores da BDB. Esta função utiliza a função eh_utilizador para verificar se corresponde a um utlizador válido da BDB, utiliza a função eh_senha_valida para verificar se a senha e a regra individual estão corretas. A função devolve uma lista com o nome dos utilizadores cuja a senha e regra individual não estejam corretas.
    list(input) --> list(output)
    '''
    errado = str()
    lista = []
    if type(dicionarios) != list or dicionarios==[]:
        #Levanta erro se o argumento inserido não for uma lista ou for uma lista vazia
        raise ValueError ('filtrar_senhas: argumento invalido')
    for i in range(0,len(dicionarios)):
        if not eh_utilizador(dicionarios[i]):
            #Levanta erro no caso de cada elemento da lista não corresponder a um utilizador válido da BDB 
            raise ValueError('filtrar_senhas: argumento invalido')
    for i in range(0,len(dicionarios)):
        if not eh_senha_valida(dicionarios[i]['pass'],dicionarios[i]['rule']):
            errado = dicionarios[i]['name']
            lista += [errado]  
            lista = sorted(lista)
    return lista