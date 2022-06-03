''' 2.1
sec = eval(input('Escreva um número de segundos\n?'))
dias = sec/86400
print('O número de dias correspondentes é: ',dias)
'''

''' 2.2
sec = eval(input('Escreva o número de segundos '))
dias = sec//86400
horas = (sec-(dias*86400))//(3600)
minutos = (sec-(dias*86400)-(horas*3600))//(60)
segundos = sec-(dias*86400)-(horas*3600)-(minutos*60)
print ('Dia = ',dias,'Horas = ',horas,'Minutos = ',minutos,'Segundos = ',segundos)
'''

'''2.3
x,y,z = eval(input('Escreva três números separados por vírgulas\n?'))
if x>y and x>z:
    print('O maior é ',x)
if y>x and y>z:
    print('O maior é ',y)
if z>x and z>y:
    print('O maior é ',z)
'''

''' 2.4
sec = eval(input('Escreva um número de segundos\n(um número negativo para terminar)\n?'))
dias = sec/86400
while sec>=0:
    print('O número de dias correspondentes é ',dias)
    sec = eval(input('Escreva um número de segundos\n(um número negativo para terminar)\n?'))
    dias = sec/86400  
'''
'''
# 2.6
res = 0
num = eval(input('Escreva um digito\n(-1 para terminar)\n?'))
while num != -1:
    res = res * 10 + num
    num = eval(input('Escreva um digito\n(-1 para terminar)\n?'))
print(res)
'''
'''
#2.7
num = eval(input('Escreva um inteiro positivo\n?'))
soma = 0
while num > 0:
    dig = num % 10
    num = num // 10
    if dig % 2 == 0:
        soma += dig
print(soma)
'''
'''
#3.4
def soma_divisores(n):
 soma = 0
 for i in range(1,n+1):
  div = n%i
  if div == 0:
   soma = soma + i
 return soma          


#3.9
def soma(r,n):
  soma = 0
  if n < 0:
   raise ValueError('serie_geom, argumento incorreto')
  for i in range(0,n+1):
   soma += r**i 
  return soma

'''
def amigas(word1,word2):
    if sorted(word1) == sorted(word2):
        print('True')
    else:
        print('False')

def junta_ordenados(tuple1,tuple2):
    n1= 0
    n2 = 0
    res = ()
    while n1 < len(tuple1) and n2 < len(tuple2):
        if tuple1[n1] < tuple2[n2]:
            res = res + (tuple1[n1],)
            n1 += 1
        else:
            res = res + (tuple2[n2])
            n2 += 1
        res = res + tuple1[n1:] + tuple2[n2:]
    return res
        


def remove_multiplos(lista,num):
    for i in range(0,len(lista)):
        if lista[i]%num != 0:
            lista = lista.remove(lista[i])
    return lista

#4.2
def explode(num):
    if isinstance(num,int):
        res = ()
        while num != 0:
            res = (num%10,) + res
            num = num//10
        return res

#4.3
def implode(tup):
    res = 0
    for i in range(0,len(tup)):
        if isinstance(tup[i],int):
            res = res * 10 + tup[i]
            
        else:
            raise ValueError('implode. elemento não inteiro')
    return res

#4.4
def filtra_pares(num):
    res = ()
    for i in num:
        if isinstance (i,int):
            if (i%2)==0:
                res = res+(i,)
        else:
            raise ValueError
    return res

#4.5
def algarismos_pares(num):
    tup = explode(num)
    par = filtra_pares(tup)
    fin = implode(par)
    return fin

#4.8
def junta_ordenados(t1,t2):
    res = ()
    for i in t1:
        if isinstance(i,int):
            res = res + (i,)
    re=res
    for e in t2:
        if isinstance(i,int):
            re = re + (e,)
    r=tuple(sorted(re))       
    return r

#5.1
def lista_codigos(l1):
    res = []
    for i in range(0,len(l1)):
        res = res + [ord(l1[i]),]
    return res

#5.2
def remove_multiplos(l1,n):
    l2=[]
    for i in range(0,len(l1)):
        if (l1[i]%n)==0:
            l2 = l2
        else:
            l2 = l2 + [l1[i]]
    return l2

#5.3
def soma_cumulativa(l1):
    l2 = []
    soma = 0
    for i in range(0,len(l1)):
        soma = soma + l1[i]
        l2 = l2 + [soma]
    return l2

#5.4
def elemento_matriz(m,l,c):
    m2 = m[l]
    m3 = m2[c]
        
    return m3

def soma_mat(a,b):
    m = []
    n =[]
    for i in range(0,len(a)):
        m = a[i]
        n = b[i]
        for i in range(0,len(m)):
            p = m[i] + n[i]
            print(p)
            
def num_occ_lista(l1,n):
    count = 0
    for i in range(0,len(l1)):
        if type (l1[i])==int:
            if l1[i]==n:
                count +=1
        else:
            count += num_occ_lista(l1[i],n)
    return count

def explode(num):
    res = ()
    if isinstance(num,int):
        while num>0:
            n = num%10
            res = (n,) + res
            num = num//10
    else:
        raise ValueError('explode: argumento não inteiro')
    return res   

def implode(tup):
    
    res = 0
    for i in range(0,len(tup)):
        if isinstance(tup[i],int):
            res = res*10 + tup[i] 
        else:
            raise ValueError('implode: elemento não inteiro')
    return res     


def filtra_pares(tup1):
    res = ()
    for i in range(0,len(tup1)):
        if isinstance(tup1[i],int):
            if tup1[i]%2==0:
                res = res + (tup1[i],)
            
    return res


def algarismos_pares(num):
    n=implode(filtra_pares(explode(num)))
    return n
def num_para_seq_cod(num):
    cod = ()
    while num>0:
        if num%10>=0 and num%10<8 and (num%10)%2==0:
            cod = (((num%10)+2),) + cod
        if num%10>=0 and num%10==8 and (num%10)%2==0:
            cod = (0,) + cod
        if num%10>=0 and num%10!=1 and (num%10)%2!=0:
            cod = (((num%10)-2),) + cod
        if num%10>=0 and num%10==1 and (num%10)%2!=0:
            cod = (9,) + cod 
        num = num//10
    return cod
def junta_ordenados(tup1, tup2):
    res = ()
    for i in range(0,len(tup1)):
        res = res + (tup1[i],)
    for i in range(0,len(tup2)):
        res = res + (tup2[i],)
    res = tuple(sorted(res))
    return res

def lista_codigos(cad):
    res = ()
    for i in range(0,len(cad)):
        res = res + (ord(cad[i]),)
    n=[]
    for i in range(0,len(res)):
        n = n + [res[i]]
    return n
def remove_multiplos(l1,num):
    res = []
    for i in range(0,len(l1)):
        if ((l1[i])%num)!=0:
            res = res + [l1[i]]
    return res

def soma_cumulativa(l1):
    l2 = []
    soma = 0
    for i in range(0,len(l1)):
        soma = soma + l1[i]
        l2 = l2 + [soma]
    return l2

def agrupa_por_chave(l1):
    l2 = {}
    for i in range (0,len(l1)):
        if l1[i][0] in l2:
            l2[l1[i][0]] += [l1[i][1]]
        else:
            l2[l1[i][0]] = [l1[i][1]]
    return l2

def baralho():
    valor = ['A','2','3','4','5','6','7','8','9','J','Q','K']
    np = ['esp','copas','paus','ouros']
    l1 = []
    for s in np:
        for a in valor:
            l1 += [{'np': s,'vlr': a}]
    return l1


from random import random
def baralha(baralho):
    for i in range(len(baralho)):
        pos = int(random()*len(baralho))
        baralho[i],baralho[pos] = baralho[pos],baralho[i]
    return baralho

def distribui(baralhos):
    if len(baralhos)%4!=0:
        raise ValueError('não é múltiplo de 4')
    c = []
    jog1,jog2,jog3,jog4 = [],[],[],[]
    for i in range (0,len(baralho),4):
        jog1 += [baralho[i]]
        jog2 += [baralho[i+1]]
        jog3 += [baralho[i+2]]
        jog4 += [baralho[i+3]]
    return [jog1,jog2,jog3,jog4]
    
def mais_antigo(bib):
    mais_antigo2 = bib[0]
    for i in range(0,len(bib)):
        if bib[i]['ano'] < mais_antigo2['ano']:
            mais_antigo2 = bib[i]
    return mais_antigo2 ['titulo']

#9.2-a
def cria_rel(h,m,s):
    return {'h':h,'m':m,'s':s}
def horas(r):
    return r['h']
def minutos(r):
    return r['m']
def segundos(r):
    return r['s']
def eh_relogio(r):
    return type(r)==dict and 'h' in r and 'm' in r and 's' in r and len(r)==3 and type(r['h'])==type(r['m'])==type(r['s'])==int and r['h'] in range(0,24) and r['m'] in range(0,60) and r['s'] in range(0,60)
def eh_meia_noite(r):
    return r['h']==r['m']==r['s']==0
def eh_meio_dia(r):
    return r['h']==12 and r['m']==r['s']==0
def mesmas_horas(r1,r2):
    return r1==r2
def escreve_relogio(rel):
    return '{:02d}:{:02d}:{02d}'.format(horas(rel),minutos(rel),segs(rel))


def conta_vogais(fish):
    f = open(fish,'r')
    res = {'a':0, 'e':0, 'i':0,'o':0,'u':0}
    linhas.readlines()
    for l in linhas:
        for c in l:
            if c in ['a','e','i','o','u']:
                res[c]+=1
    f.close()
    return res
    

def agrupa_por_chave(l1):
    d1 = {}
    for key, value in l1:
        if key in d1:
            d1[key] += [value]
        else:
            d1[key] = [value]
    return d1

def baralho():
    baralho = []
    naipe = ['esp','copas','ouros', 'paus']
    valor = ['A', '2', '3','4','5','6','7','8','9','10','J','Q','K']
    for i in naipe:
        for j in valor:
            baralho += [{'np':i, 'vlr':j}]

    return baralho      

from random import random
def baralha(l1):
    for i in range(0,len(l1)):
        l1[i] += l1.random()
    return l1
def resumo_FP(notas):
    tup = ()
    soma1 = 0
    soma2 = 0
    num = 0
    for key in notas:
        if key>=10:
            soma1 += key*len(notas[key])
            num += len(notas[key])
            media = soma1/num
        if key<10:
            soma2 += len(notas[key])
    tup = (media,) +(soma2,)
    return tup
def cria_data(d,m,a):
    if d != int or m!= int or a!= int or d<1 or d>31 or m<1 or m>12:
        raise ValueError
    return {'dia':d, 'mes':m,'ano':a}

def dia(data):
    return data['dia']

def mes(data):
    return data['mes']

def ano(data):
    return data['ano']

def eh_data(arg):
    if type(arg) != dict or 'dia' not in arg or 'mes' not in arg or 'ano' not in arg:
        return False
    dia, mes, ano = arg["dia"], arg["mes"], arg["ano"]
    return type(dia) == int and type(mes) == int and type(ano) == int and 1 <= mes <= 12

def mesma_data(d1,d2):
    return (dia(d1)==dia(d2) and mes(d1)==mes(d2) and ano(d1)==ano(d2))

def cria_time_stamp(dt,rel):
    return {'data': dt, 'relógio': rel}

def data(ts):
    return ts['data']

def relogio(ts):
    return ts['relógio']

def eh_time_stamp(arg):
    if 'data' not in arg or 'relógio' not in arg:
        return False
    return True

def mesmo_time_stamp(ts1,ts2):
    if not eh_time_stamp(ts1) or not eh_time_stamp(ts2):
        return False
    return ts1['data']==ts2['data'] and ts1['relógio']==ts2['relógio']

def periodos_compativeis(per1,per2):
    if per1['dia']!= per2['dia']:
        return True
    if per1['inicio'] >= per2['fim'] or per2['inicio']>=per1['fim']:
        return True
    return False
def sala_esta_livre(sala,per):
    for periodo in sala['ocupacao']:
        if periodos_compativeis(periodo,per):
            return True
    return False
def cria_periodo(dia,inicio,fim):
    if dia not in ('seg','ter','qua','qui','sex','sab','dom') or type(inicio)!=float or inicio<0 or inicio>24 or type(fim)!=float or fim<0 or fim>24:raise ValueError
    return {'dia':dia,'inicio':inicio,'fim':fim}

def obter_dia_periodo(per):
    return per['dia']

def obter_inicio_periodo(per):
    return per['inicio']

def obter_fim_periodo(per):
    return per['fim']

def cria_sala(nome,tipo,capacidade,ocupacao):
    if type(nome)!=str or type(tipo)!=int or type(capacidade)!= int or ocupacao!=tup:
        raise ValueError
    return {'nome':nome,'tipo':tipo,'capacidade':capacidade,'ocupacao':ocupacao}
def obter_nome_sala(sala):
    return sala['nome']
def obter_tipo_sala(sala):
    return sala['tipo']
def obter_capacidade_sala(sala):
    return sala['capacidade']
def obter_ocupacao_sala(sala):
    return sala['ocupacao']

def periodos_compativeis_new(p1,p2):
    if obter_dia_periodo(p1) != obter_dia_periodo(p2):
        return True
    if obter_inicio_periodo(p1) >= obter_fim_periodo(p2) or obter_inicio_periodo(p2)>=obter_fim_periodo(p1):
        return True
    return False  
def sala_esta_livre(s1,p1):
    for periodo in obter_ocupacao_sala(s1):
        if periodos_compativeis_new(obter_ocupacao_sala(periodo),p1):
            return True
    return False  

def apenas_digitos_impares(num):
    if num == 0:
        return 0
    res = num % 10
    if res % 2 == 0:
        return apenas_digitos_impares(num//10)
    else:
        return apenas_digitos_impares(num//10)*10+res
    
def junta_ordenadas(l1,l2):
    if len(l2)!=0:
        l1 += [l2[0]]
        return junta_ordenadas(l1,l2[1:])
    else:
        return sorted(l1)

def sublistas(l1):
    if len(l1)==0:
        return 0
    elif type(l1[0])==list:
            return 1 + sublistas(l1[0]) + sublistas(l1[1:])
    return sublistas(l1[1:])

def somar_n_vezes(a,b,n):
    if n == 0:
        return 0
    return b+a+somar_n_vezes(a,0,n-1)

def soma_els_atomicos(tup):
    if isinstance(tup,tuple):
        if len(tup)==0:
            return 0
        return soma_els_atomicos(tup[0]) + soma_els_atomicos(tup[1:])
    return tup

def inverte(l1):
    if len(l1)==0:
        return []
    return inverte(l1[1:]) + [l1[0]]

def pertence(l,n):
    if len(l)==0:
        return False
    if l[0]==n:
        return True
    else:
        return pertence(l[1:],n)

def subtrai(l1,l2):
    if len(l1)==0:
        return []
    if pertence(l2,l1[0]):
        return subtrai(l1[1:],l2)
    return [l1[0]] + subtrai(l1[1:],l2)

def parte(l1,n):
    def maior_n(l1,n):
        if len(l1)==0:
            return []
        if l1[0]>=n:
            return [l1[0]] + maior_n(l1[1:],n)
        return maior_n(l1[1:],n)
    def menor_n(l1,n):
        if len(l1)==0:
            return []
        if l1[0]<n and l1[0]!=n:
            return [l1[0]] + menor_n(l1[1:],n)
        return menor_n(l1[1:],n)
    return [menor_n(l1,n),maior_n(l1,n)]

def maior(l1):
    def maior_aux(l1,n):
        if len(l1)==0:
            return n
        if l1[0]>n:
            return maior_aux(l1[1:],l[0])
        return maior_aux(l1[1:],n)
    return maior_aux(l1,l1[0])

def misterio(x,n):
    if n==0:
        return 0
    else:
        return x*n + misterio(x,n-1)
    
def squared(n):
    if n<=1:
        return 1
    return (n+n-1) + squared(n-1)

def squared_2(n):
    def aux(n,acc):
        if n <=1:
            return acc + 1
        return aux(n-1,acc+n+n-1)
    return aux(n,0)

def squared_3(n):
    acc = 0
    for i in range(1, n + 1):
        acc += i + i - 1
    return acc

def numero_digitos(n):
    if not isinstance(n,int):
        raise ValueError ('numero_digitos: argumento inválido')
    if n==0:
        return 0
    else:
        return 1 + numero_digitos(n//10)
    
def numero_digitos_2(n):
    if not isinstance(n,int):
        raise ValueError ('numero_digitos: argumento inválido')    
    def aux(n,res):       
        if n==0:
            return res
        else:
            return aux(n//10,res+1)
    return aux(n,0)

def numero_digitos_3(n):
    count=0
    if not isinstance(n,int):
        raise ValueError ('numero_digitos: argumento inválido')    
    while n>0:
        count+=1
        n = n//10
    return count 

def espelho(n):
    if n/10==0 or n<0 or type(n)!=int:
        raise ValueError('epelho: argumento inválido')
    def aux(n,res):
        if n==0:
            return res
        num = n%10
        return aux(n//10,res*10+num)
    return aux(n,0)

def g(n):
    if n==0:
        return 0
    if n>0:
        return n-g(g(n-1))
    
def maior_int(limite):
    def aux(limite,n,res):
        if res>limite:
            return n-1
        return aux(limite,n+1,res+n+1)
    return aux(limite,1,1)

def soma_divisores(n):
    def aux(n,d,soma):
        if d==0:
            return soma
        if n%d==0 and d!=n:
            return aux(n,d-1,soma+d)
        if n%d!=0 or d==n:
            return aux(n,d-1,soma)
    return aux(n,n,0)

def conta_linhas(s):
    count = 0
    with open(s,'r') as f:
        for c in f.readlines():
            count+=1
    return count

def conta_vogais_2(s):
    d = {'a' : 0, 'e' :0,'i':0,'o':0,'u':0}
    with open(s,'r') as f:
        for c in f.read():
            if c in d:
                d[c]+=1
    return d
    
def fish(s1,s2):
    with open(s1,'r') as f1:
        lines = f1.readlines()
        with open (s2,'w+') as f2:
            f2.writelines(lines)
    
def concatena(l,s):
    with open(s,'w+') as f:
        for c in l:
            f.writelines(c)
            f.writelines(' ')
    
def procura(s1,s2):
    with open(s2,'r') as f:
        lines = f.readlines()
        for c in lines:
            if s1 in c:
                print (c[:-1])

def corta(s1,s2,n):
    with open(s1,'r') as f1:
        with open(s2,'w+') as f2:
            i=0
            for c in f1.read():
                if i>=n:
                    break
                f2.write(l)
                i += 1

def divide(s,n):
    with open(s,'r') as f:
        with open(s + '0','w+') as f0:
            with open(s + '1','w+') as f1:
                i =0
                for c in f.read():
                    if i<=n:
                        f0.write(c)
                    else:
                        f1.write(c)
                        
'''
Funções de ordem superior
a = lambda [argumentos]: [corpo da função]
argumentos: podem ser x,y,z...
corpo da função: por exemplo x+y+z ou x*y*z ou (x,y,z)
'a' é o nome da função lambda
b = lambda x,y,z:[x,y,z-1]
b(1,2,3) --> [1,2,2]

exemplo:
filter(bool,iter)
list(filter(lambda x:x>0,[1,-1,2-2,100,-1000]))
'''

def piatorio(sup_l,inf_l,fn,prox):
    res = 1
    while inf_l<=sup_l:
        res = res*fn(inf_l)
        inf_l=prox(inf_l)
    return res

def fatorial(fn):
    return piatorio(1,n, lambda x:x, lambda x:x+1)

def soma_fn(n,fn):
    res=0
    for i in range(1,n+1):
        res=res+fn(i)
    return res

def soma_fn_2(n,fn):
    def aux(n,fn,res):
        if n==0:
            return res
        return aux(n-1,fn,res+fn(n))
    return aux(n,fn,0)

def filtra(lst,tst):
    if lst==[]:
        return []
    if tst(lst[0]):
        return [lst[0]]+filtra(lst[1:],tst)
    else:
        return filtra(lst[1:],tst)

def transforma(lst,fn):
    if lst==[]:
        return []
    return [fn(lst[0])]+transforma(lst[1:],fn)
def soma_quadrados_impares(l):
    return acumula(transforma(filtra(lst,lambda x: x%2!=0),lambda x:x**2),lambda x,y:x+y)

def n_pares(n):
    l=[]
    while n>0:
        l= [n%10]+l
        n=n//10
    return list(filter(lambda x:x%2==0,l))

    
def explode(n): 
    tup=()
    if not isinstance(n,int) or n<0:
        raise ValueError('explode: argumento invalido')
    while n>0:
        dig=n%10
        tup = (dig,) + tup
        n=n//10
    return tup

def implode(tup):
    res=0
    if type(tup)!=tuple:
        raise ValueError('implode: argumento invalido')
    for i in range(0,len(tup)):
        if type(tup[i])!=int or tup[i]<0:
            raise ValueError('implode: argumento invalido')
    for i in range(0,len(tup)):
        res=res*10+(tup[i])
    return res

def filtra_pares(tup):
    res=()
    if not isinstance(tup,tuple):
        raise ValueError('filtra_pares: argumento invalido')
    for i in tup:
        if i%2==0:
            res+= (i,)
    return res

def algarismos_pares(n):
    res= implode(filtra_pares(explode(n)))
    return res

def num_para_seq_cod(n):
    tup=()
    if not isinstance(n,int) or n<0:
        raise ValueError('explode: argumento invalido')
    while n>0:
        dig=n%10
        tup = (dig,) + tup
        n=n//10
    tup2=()
    for i in tup:
        if i!=8 and i%2==0:
            i+=2
            tup2+=(i,)
        elif i==8:
            i=0
            tup2+=(i,)
        elif i!=1 and i%2!=0:
            i=i-2
            tup2+=(i,)
        else:
            i=9
            tup2+=(i,)
    return tup2

def junta_ordenados(tup1,tup2):
    l1=[]
    res=()
    for i in tup1:
        l1+=[i]
    for j in tup2:
        l1+=[j]
    l1=sorted(l1)
    for n in l1:
        res+=(n,)
    return res

def codifica(s):
    s2=''
    for i in range(len(s)):
        if i%2==0:
            s2+=s[i]
    for j in range(len(s)):
        if j%2!=0:
            s2+=s[j]
    return s2   

def lista_codigos(s):
    l=[]
    for i in s:
        l+=[ord(i)]
    return l

def remove_multiplos(l1,n):
    l2=[]
    for i in l1:
        if i%n!=0:
            l2+=[i]  
    return l2

def soma_cumulativa(l1):
    l2=[]
    res=0
    for i in l1:
        l2= l2+[i+res]
        res=res+i
    return l2

def num_occ_lista(l1,n):
    count=0
    for i in l1:
        if type(i)!=list:
            if i==n:
                count+=1
            del(i)
    return count

def piatorio(l_sup,l_inf,termo,prox):
    res=1
    for i in range(l_inf,l_sup+1):
        res=res*termo(i)
        l_inf=prox(l_inf)
    return res

def fatorial(n):
    return piatorio(1,n, lambda x: x, lambda x:x+1)

def soma_fn(n,fn):
    res=0
    for i in range(1,n+1):
        res+=fn(i)
    return res

def soma_fn(n,fn):
    if n==0:
        return 0
    return fn(n)+soma_fn_2(n-1,fn)

def filtra(lst,tst):
    if lst==[]:
        return []
    if tst(lst[0]):
        return [lst[0]]+filtra(lst[1:],tst)
    else:
        return filtra(lst[1:],tst)

def transforma(lst,fn):
    if lst==[]:
        return []
    return [fn(lst[0])]+ transforma(lst[1:],fn)

def acumula(lst, fn):
    def acumula_aux(acc, lst, fn):
        if len(lst) == 0:
            return acc
        return acumula_aux(fn(acc, lst[0]), lst[1:], fn)

    return acumula_aux(0, lst, fn)

def soma_quadrados_impares(lst):
    return  acumula(transforma(filtra(lst,lambda x : x % 2 != 0),lambda x : x**2),lambda x,y : x+y)

def misterio(num, p):
    if num == 0:
        return 0
    elif p(num % 10):
        return num % 10 + 10 * misterio(num // 10, p)
    else:
        return misterio(num // 10, p)


def filtra_pares(n):
    return misterio(n,lambda n:n%2==0)

def lista_digitos(n):
    return list(map(lambda n: int(n),str(n)))

from functools import reduce

def produto_digitos(n,fn):
    return reduce((lambda x,y:x*y, filter(fn,lista_digitos(n))))

def apenas_digitos_impares(n):
    return reduce(lambda x,y: x*10+y,filter(lambda n:n%2!=0,(map(lambda n:int(n),str(n)))))
       
