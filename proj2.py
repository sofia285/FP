'''
nome: Sofia Paiva  nº102835  e-mail: sofia.paiva@tecnico.ulisboa.pt
'''

#2.1.1 - TAD posição
def cria_posicao(x,y):
    '''
    Através dos valores que recebe que correspondem a coordenadas, cria uma posição  
    (int,int --> posição)
    '''
    if type(x)!=int or type(y)!=int or x<0 or y<0:
        #Levanta erro no caso de os valores inseridos não estarem de acordo com os parâmetros de entrada
        raise ValueError('cria_posicao: argumentos invalidos')
    return (x,y)

def cria_copia_posicao(p):
    '''
    devolve uma cópia da posição p  
    (posição --> posição)
    '''
    return p.copy()

def obter_pos_x(p):
    '''
    Devolve o valor correspondente ao x da posição
    (posição --> int)
    '''
    return p[0]

def obter_pos_y(p):
    '''
    Devolve o valor correspondente ao y da posição 
    (posição --> int)
    '''
    return p[1]

def eh_posicao(arg):
    '''
    Devolve o valor lógico do argumento inserido, ou seja se o argumento é posição válida 
    (posição --> boolean)
    '''
    if type(arg)!=tuple or len(arg)!=2:
            return False
        
    if type(obter_pos_x(arg))!=int or type(obter_pos_y(arg))!=int:
        return False
    
    if obter_pos_x(arg)<0 or obter_pos_y(arg)<0 :
        return False
    
    return True
    
def posicoes_iguais(p1,p2):
    '''
    Devolve o valor lógico da verificação da validade das posições inseridas e se são iguais
    (posição,posição --> boolean)
    '''
    return p1==p2 and eh_posicao(p1) and eh_posicao(p2)

def posicao_para_str(p):
    '''
    Transforma a posição inserida em string
    (posição --> string)
    '''
    return str(p)

def obter_posicoes_adjacentes(p):
    '''
    Obtém as posições válidas que se encontram à volta da posição inserida 
    (posição --> tuple)
    '''
    l=[(obter_pos_x(p),obter_pos_y(p)-1),(obter_pos_x(p)+1,obter_pos_y(p)),(obter_pos_x(p),obter_pos_y(p)+1),(obter_pos_x(p)-1,obter_pos_y(p))]
    l2=()
    for i in range(0,len(l)):
        if l[i][0]>=0 and l[i][1]>=0:
            l2+=(l[i],)
    return l2

def ordenar_posicoes(t):
    '''
    Devolve as posições adjacentes de uma certa posição pela ordem de leitura do prado  
    (tuple --> tuple)
    '''
    return tuple(sorted(t, key=lambda k: [k[1], k[0]]))

#2.1.2 - TAD animal
def cria_animal(s,r,a):
    '''
    Através dos valores que recebe que correspondem a uma espécie e à frequência de reprodução e alimentacão dela, esta funcão cria um animal  
    (string,int,int --> animal)
    '''
    if type(s)!=str or len(s)==0 or type(a)!=int or type(r)!=int or r<=0 or a<0:
        #Levanta erro no caso de os valores inseridos não estarem de acordo com os parâmetros de entrada
        raise ValueError('cria_animal: argumentos invalidos')
    return [s,r,a,0,0]

def cria_copia_animal(a):
    '''
    Cria uma cópia do animal 'a' 
    (animal --> animal)
    '''
    return a.copy()

def obter_especie(a):
    '''
    Devolve o nome da espécie  
    (animal --> string)
    '''
    return a[0]

def obter_freq_reproducao(a):
    '''
    Devolve a frequência de reprodução do animal 
    (animal --> int)
    '''
    return a[1]

def obter_freq_alimentacao(a):
    '''
    Devolve a frequência de alimentação do animal
    (animal --> int)
    '''
    return a[2]

def obter_idade(a):
    '''
    Devolve a idade do animal  
    (animal --> int)
    '''
    return a[3]

def obter_fome(a):
    '''
    Devolve a fome do animal(predador)  
    (animal --> int)
    '''
    return a[4]

def aumenta_idade(a):
    '''
    Função que acrescenta uma unidade à idade de um certo animal
    (animal --> animal)
    '''
    
    a[3] += 1 
    
    return a

def reset_idade(a):
    '''
    Função que reinicia a idade de um certo animal, ou seja o animal volta a ter idade=0  
    (animal --> animal)
    '''
    
    a[3] = 0
    
    return a

def aumenta_fome(a):
    '''
    Função que acrescenta uma unidade à fome de um certo animal 
    (animal --> animal)
    '''
    if eh_predador(a):
        a[4] += 1
    
    return a
    
def reset_fome(a):
    '''
    Função que reinicia a fome de um certo animal, ou seja a fome desse animal passa a ser igual a 0.
    (animal --> animal)
    '''
    if eh_predador(a):
        a[4] = 0
    return a

def eh_animal(arg):
    '''
    Função que verifica se um dado argumento é um animal.
    (universal --> boolean)
    '''
    if type(arg)!=list or len(arg)!=5:
        return False
    
    if type(obter_freq_reproducao(arg))!=int or type(obter_freq_alimentacao(arg))!=int or type(obter_especie(arg))!=str:
        return False
    
    if type(obter_fome(arg))!=int or type(obter_idade(arg))!=int:
        return False
    
    if obter_freq_reproducao(arg)<=0 or obter_freq_alimentacao(arg)<0:
        return False  
    
    if obter_fome(arg)<0 or obter_idade(arg)<0:
        return False
    
    return True

def eh_predador(arg):
    '''
    Função que verifica se um certo argumento é um animal predador. 
    (universal --> boolean)
    '''
    return eh_animal(arg) and obter_freq_alimentacao(arg)>0

def eh_presa(arg):
    '''
    Função que verifica se um certo argumento corresponde a um animal presa
    (universal --> boolean)
    '''
    return eh_animal(arg) and obter_freq_alimentacao(arg)==0 and obter_fome(arg)==0

def animais_iguais(a1,a2):
    '''
    Função que verifica se dois animais intruduzidos são de facto animais e se são animais idênticos
    (animal,animal --> boolean)
    '''
    if not eh_animal(a1) or not eh_animal(a2):
        return False
    
    if obter_especie(a1)!=obter_especie(a2):
        return False
    
    if obter_freq_reproducao(a1)!=obter_freq_reproducao(a2):
        return False
    
    if obter_freq_alimentacao(a1)!=obter_freq_alimentacao(a2):
        return False
    
    if obter_idade(a1) != obter_idade(a2):
        return False
    
    return True

def animal_para_char(a):
    '''
    Função que devolve a inical da especie do animal
    (animal --> string)
    '''
    especie=obter_especie(a).replace(' ','')
    if eh_presa(a):
        return especie[0].lower()
    if eh_predador(a):       
        return especie[0].capitalize()

def animal_para_str(a):
    '''
    Função que devolve a representação do animal
    (animal --> string)
    '''
    if eh_presa(a):
        return str(obter_especie(a)) + ' ['+ str(obter_idade(a))+'/'+str(obter_freq_reproducao(a))+']'
    if eh_predador(a):
        return str(obter_especie(a)) + ' ['+ str(obter_idade(a))+'/'+str(obter_freq_reproducao(a))+';'+str(obter_fome(a))+'/'+str(obter_freq_alimentacao(a))+']'    
    
def eh_animal_fertil(a):
    '''
    verifica se um certo animal se pode reproduzir, ou seja se a idade de um animal é igual à sua frequência de reprodução
    (animal --> boolean)
    '''
    return obter_idade(a)==obter_freq_reproducao(a)

def eh_animal_faminto(a):
    '''
    Verifica se um animal é predador e se por isso a fome dele é igual ou superior à sua frequência de alimentação
    (animal --> boolean)
    '''
    return eh_predador(a) and obter_fome(a)>=obter_freq_alimentacao(a)

def reproduz_animal(a):
    '''
    Função que reproduz um animal, ou seja cria um animal idêntico ao inserido. A idade do animal inserido passa a ser 0
    (animal --> animal)
    '''
    a = reset_idade(a)
    
    return reset_fome(cria_copia_animal(a))

#2.1.3 - TAD prado
def  cria_prado(d,r,a,p):
    '''
    Através dos valores inseridos(limites exteriores do prado,obstáculos,animais,posições dos animais), esta função cria um prado
    (posição,tuple,tuple,tuple --> prado)
    '''
    if not eh_posicao(d) or type(r)!= tuple or len(a)<1 or len(a)!=len(p) or type(r)!=type(a)!=type(p)!=tuple or not eh_prado([d,r,a,p]):
        #Levanta erro no caso de os valores inseridos não estarem de acordo com os parâmetros de entrada
        raise ValueError('cria_prado: argumentos invalidos')
    
    for j in range(0,len(r)):
        if type(r[j])!=tuple:
            raise ValueError('cria_prado: argumentos invalidos')
    for i in range(0,len(a)):
        if not eh_animal(a[i]) or not eh_posicao(p[i]):
            raise ValueError('cria_prado: argumentos invalidos')
        
    
    return [d,r,list(a),list(p)]

def cria_copia_prado(m):
    '''
    Função que cria um prado idêntico ao inserido
    (prado --> prado)
    '''
    new_m = m.copy()
    animais=[]
    posicoes=[]
    for i in range(0,len(m[2])):
        a=cria_copia_animal(m[2][i])
        p=m[3][i]
        animais+=[a]
        posicoes+=[p]
        
    new_m[2] = animais
    new_m[3] = posicoes
    return new_m

def obter_tamanho_x(m):
    '''
    Devolve a posição Nx (maior x) do prado
    (prado --> int)
    '''
    return m[0][0]+1

def obter_tamanho_y(m):
    '''
    Devolve a posição Ny (maior y) do prado
    (prado --> int)
    '''
    return m[0][1]+1


def obter_numero_predadores(m):
    '''
    Função que devolve o número de predadores no prado
    (prado --> int)
    '''
    count=0
    for i in m[2]:
        if eh_predador(i):
            count+=1
    return count

def obter_numero_presas(m):
    '''
    Função que devolve o número de presas no prado
    (prado --> int)
    '''
    count=0
    for i in m[2]:
        if eh_presa(i):
            count+=1
    return count

def obter_posicao_animais(m):
    '''
    Devolve as posições dos animais no prado
    (prado --> tuple)
    '''
    return ordenar_posicoes(m[3])


def obter_animal(m,p):
    '''
    Devolve o animal do prado que se encontra na posição inserida
    (prado,posição --> animal)
    '''
    if eh_prado(m) and eh_posicao(p):
        for i in range(0,len(m[3])):
            if posicoes_iguais(p,m[3][i]):
                return m[2][i]


def eliminar_animal(m,p):
    '''
    Função que elimina o animal que está na posição inserida
    (prado,posição --> prado)
    '''
    if eh_prado(m) and eh_posicao(p):
        for i in range(0,len(m[3])):
            if posicoes_iguais(m[3][i],p):
                del m[2][i]
                del m[3][i]
                break
            
    return [m[0],m[1],m[2],m[3]]
    
def mover_animal(m,p1,p2):
    '''
    Função que move um animal da posição onde se encontra para outra posição inserida
    (prado,posição,posição --> prado)
    '''
    if eh_prado(m) and eh_posicao(p1) and eh_posicao(p2):
        for i in range(0,len(m[3])):
            if posicoes_iguais(m[3][i],p1):
                m[3][i] = p2
                break
        
    return [m[0],m[1],m[2],m[3]]

def inserir_animal(m,a,p):
    '''
    Função que insere um animal numa dada posição
    (prado,animal,posição --> prado)
    '''
    m[2] += [a]
    m[3] += [p]
    
    return [m[0],m[1],m[2],m[3]]
    

def eh_prado(arg):
    '''
    Função que verifica se um dado argumento corresponde a um prado
    (universal --> boolean)
    '''
    if type(arg)!=list or len(arg)!=4 or len(obter_posicao_animais(arg))<1:
        return False
    
    if not eh_posicao(arg[0]) or type(arg[1])!=type(arg[2])!=type(obter_posicao_animais(arg))!=tuple:
        return False
    
    if len(obter_posicao_animais(arg))!=(obter_numero_presas(arg)+obter_numero_predadores(arg)):
        return False
    
    for j in range(0,len(arg[1])):
        if not eh_posicao(arg[1][j]):
            return False
        if obter_pos_x(arg[1][j])==0 or obter_pos_y(arg[1][j])==0:
            return False
        if obter_pos_x(arg[1][j])>=obter_pos_x(arg[0]) or obter_pos_y(arg[1][j])>=obter_pos_y(arg[0]):
            return False
    
    for i in range(0,len(arg[2])):
        if not eh_animal(arg[2][i]) or not eh_posicao(arg[3][i]):
            return False
        if obter_pos_x(arg[0])<=obter_pos_x(arg[3][i]):
            return False
        if obter_pos_y(arg[0])<=obter_pos_y(arg[3][i]):
            return False
        if arg[3][i] in arg[1]:
            return False
    
    return True

def eh_posicao_animal(m,p):
    '''
    Função que verifica se uma certa posição corresponde a uma posição de um animal
    (prado,posição --> boolean)
    '''
    return bool(p in obter_posicao_animais(m)) 

def eh_posicao_obstaculo(m,p):
    '''
    Função que verifica se uma certa posição corresponde a uma posição de um obstáculo
    (prado,posição --> boolean)
    '''
    return bool(p in m[1]) or obter_pos_x(p)==0 or obter_pos_y(p)==0 or obter_pos_x(p)==obter_tamanho_x(m)-1 or obter_pos_y(p)==obter_tamanho_y(m)-1 

def eh_posicao_livre(m,p):
    '''
    Função que verifica se uma certa posição corresponde a uma posição livre
    (prado,posição --> boolean)
    '''
    return not eh_posicao_animal(m,p) and not eh_posicao_obstaculo(m,p)

def prados_iguais(p1,p2):
    '''
    Função que recebe dois prados e verifica se são idênticos
    (prado,prado --> boolean)
    '''
    return eh_prado(p1) and eh_prado(p2) and p1[0]==p2[0] and p1[1]==p2[1] and p1[2]==p2[2] and p1[3]==p2[3] 


def prado_para_str(m):
    '''
    Função que devolve a cadeia de caracteres que representa o prado
    (prado --> string)
    '''
    s=''
    c_max = obter_tamanho_x(m) - 1
    l_max = obter_tamanho_y(m) - 1
    for l in range(0,l_max + 1):
        for c in range(0,c_max + 1):
            if (l==0 and c>0 and c<c_max) or (l==l_max and c>0 and c<c_max):
                s+='-'
            elif (l==0 and c==0) or (c==0 and l==l_max) or (c==c_max and l==l_max):
                s+='+'
            elif l==0 and c==c_max:
                s+='+\n'
            elif (c==0 and l>0 and l<l_max):
                s+='|'
            elif c==c_max and l>0 and l<l_max:
                s+='|\n'
            elif l>0 and l<l_max and c>0 and c<c_max and eh_posicao_livre(m,(c,l)):
                s+='.'
            elif l>0 and l<l_max and c>0 and c<c_max and eh_posicao_obstaculo(m,(c,l)):
                s+='@'
            elif l>0 and l<l_max and c>0 and c<c_max and eh_posicao_animal(m,(c,l)):
                s+=animal_para_char(obter_animal(m,(c,l)))
    return s


def obter_valor_numerico(m,p):
    '''
    Função que devove o valor númerico de uma dada posição
    (prado,posição --> int)
    '''
    return obter_pos_y(p)*obter_tamanho_x(m)+obter_pos_x(p)

def aux_obter_movimento(m,p):
    '''
    Função auxiliar da função 'obter_movimento' 
    (prado,posição --> posição)
    '''
    p2=list(obter_posicoes_adjacentes(p))
    d=len(p2)
    p3=[]
    for i in range(0,d):
        if obter_pos_x(p2[i])!=0 and obter_pos_y(p2[i])!=0:
            p3+=[p2[i]]
    return p3

def obter_movimento(m,p):
    '''
    Função que devolve a posição seguinte do animal que se encontra na posição p dentro do prado m
    (prado,posição --> posição)
    '''
    if eh_prado(m) and eh_posicao(p):
        p2=aux_obter_movimento(m,p)
        a=obter_animal(m,p)
        n=obter_valor_numerico(m,p)
        p3=[]
        p4=[]
        if len(p2)>0:
            if eh_presa(a):
                for i in range(0,len(p2)):
                    if eh_posicao_livre(m,p2[i]):
                        p3+=[p2[i]]
                if len(p3)>0:
                    index=n%(len(p3))               
                    return p3[index]
                return p
            elif eh_predador(a):
                for i in range(0,len(p2)):
                    if eh_posicao_animal(m,p2[i]) and eh_presa(obter_animal(m,p2[i])):
                        p3+=[p2[i]]
                    elif eh_posicao_livre(m,p2[i]):
                        p4+=[p2[i]]
                if len(p3)>0:
                    index=n%(len(p3))
                    return p3[index]
                elif len(p3)==0:
                    index=n%(len(p4))
                    return p4[index]
                    
                return p
        return p    
  


def geracao(m3):
    '''
    Função que modifica o prado recebido de acordo com a evolução correspondente a uma geração completa
    (prado --> prado)
    '''
    m2 = cria_copia_prado(m3)
    fertil = False
    faminto = False
    aux_an = ()
    aux_pos = ordenar_posicoes(m2[3])
    
    
    for p in aux_pos: 
        if eh_posicao_animal(m2,p):
            a = obter_animal(m2,p)
            if a not in aux_an:
                
                aux_an += (a,)
                
                mov=obter_movimento(m2,p)             
                aumenta_idade(a)
                
                if eh_animal_fertil(a):
                    new_a = reproduz_animal(a)
                    fertil = True
                    
                if eh_predador(a):
                    aumenta_fome(a)
                    if eh_presa(obter_animal(m2,mov)):
                        eliminar_animal(m2,mov)
                        reset_fome(a)
                    if eh_animal_faminto(a):
                        eliminar_animal(m2,p)
                        faminto = True
                        
                if not faminto:        
                    mover_animal(m2,p,mov)
                if not obter_animal(m2,p) and fertil:
                    inserir_animal(m2, new_a, p)
                    
                fertil = False
                faminto = False
    return m2


 
def aux_simula_eco(m,g,v,i,predadores,presas):
    '''
    Função auxiliar da função 'simula_ecossistema'
    (prado,int,boolean,int,int --> prado)
    '''
    if i==g:
        print('Predadores:',obter_numero_predadores(m),'vs Presas:',obter_numero_presas(m),'(Gen.',str(i) + ')')
        print(prado_para_str(m))
        
        return (obter_numero_predadores(m),obter_numero_presas(m))
    elif v==True and (obter_numero_predadores(m) != predadores or obter_numero_presas(m) != presas):
        print('Predadores:',obter_numero_predadores(m),'vs Presas:',obter_numero_presas(m),'(Gen.',str(i) + ')')
        print(prado_para_str(m))
        
    return aux_simula_eco(geracao(m),g,v,i+1,obter_numero_predadores(m),obter_numero_presas(m))
    


def simula_ecossistema(f,g,v):
    '''Função que simula o ecossistema de um prado. No caso do argumento v ter sido introduzido como True, no final de cada geração é mostrado o prado e o número de presas e predadores. Se v ter sido introduzido como False, então é apenas apresentado o prado com o número de presas e predadores da primeira e da última geração.
    (string,int,boolean --> tuple)
    '''
    animais=[]
    pos=[]
    with open(f,'r') as f1:
        line=f1.readlines()
        
        for l in range(2,len(line)):
            a = eval(line[l])
            animais+=(cria_animal(a[0],a[1],a[2]),)
            pos+=(cria_posicao(a[3][0],a[3][1]),)
        m=cria_prado(eval(line[0]),eval(line[1]),animais,pos)
    print('Predadores:',obter_numero_predadores(m),'vs Presas:',obter_numero_presas(m),'(Gen.',str(0) + ')')
    print(prado_para_str(m))
    return aux_simula_eco(m,g,v,0,obter_numero_predadores(m),obter_numero_presas(m)) 