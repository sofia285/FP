#Recursao e iteracao
#Variante 1
#a
def soma_divisores_primos(n):
    if n==0:
        return 0
    
    elif eh_primo(n):
        return n + soma_divisores_primos(n-1)
    
    return soma_divisores_primos(n-1)

#b
def soma_divisores_primos(n):
    def aux_soma_divisores_primos(n,soma,primo):
        if primo==0:
            return soma
        
        elif eh_primo(primo) and n%primo==0:
            return aux_soma_divisores_primos(n,soma+primo,primo-1)
        
        return aux_soma_divisores_primos(n,soma,primo-1)
    
    return aux_soma_divisores_primos(n,0,n)

#c
def soma_divisores_primos(n):
    primo=0
    soma=0
    while primo<=n:
        
        if eh_primo(primo) and n%primo==0:
            soma+=primo
        i+=1
        
    return soma

#Variante 2
#a
def numero_digitos_pares(n):
    if n==0:
        return 0
    
    elif (n%10)%2==0:
        return 1 +numero_digitos_pares(n//10)
    
    return numero_digitos_pares(n//10)

#b
def numero_digitos_pares(n):
    def aux_numero_digitos_pares(n,soma):
        if n==0:
            return soma
        
        elif (n%10)%2==0:
            return aux_numero_digitos_pares(n//10,soma+1)
        
        return aux_numero_digitos_pares(n//10,soma)
    return aux_numero_digitos_pares(n,0)

#c
def numero_digitos_pares(n):
    soma=0
    
    while n>0:
        if (n%10)%2==0:
            soma+=1
        n=n//10    
    return soma


#Variante 3
#a
def soma_digitos_impares(n):
    digito=n%10
    if n==0:
        return 0
    
    elif digito % 2 != 0:
        return digito + soma_digitos_impares(n//10)
    
    return soma_digitos_impares(n//10)

#b
def soma_digitos_impares(n):
    def aux_soma_digitos_impares(n,soma):
        digito=n%10
        if n==0:
            return soma
        
        elif digito%2!=0:
            return aux_soma_digitos_impares(n//10,soma+digito)
        
        return aux_soma_digitos_impares(n//10,soma)
    
    return aux_soma_digitos_impares(n,0)

#c
def soma_digitos_impares(n):
    soma=0
    
    while n>0:
        digito=n%10
        
        if digito%2!=0:
            soma+=digito
        n=n//10
    
    return soma

#TADs
#Variante 1
#a
def nova_fila():
    return {}

def entra_fila(fila,el):
    return fila+{el}

def primeiro(fila):
    if comprimento(fila)==0:
        raise ValueError('indefenida')
    return fila[0]

def comprimento(fila):
    return len(fila)

def sai_fila(fila):
    if comprimento(fila)==0:
        raise ValueError('indefinida')
    return fila[1:]

def eh_fila(arg):
    return not isinstance(arg,(str,tuple,list,dict))
    

def codifica_lista_numeros(lista):
    num=1
    i=1
    
    while len(lista)>0:
        
        num=num * n_esimo_primo(i)**lista[0]
        lista=lista[1:]
        
    return num



def explode(n):
    tup=()
    if not isinstance(n,int) or n < 0:
        raise ValueError('Argumento invalido')
    
    while n>0:
        tup = (n%10,) + tup
        n = n//10
    
    return tup

def implode(n):
    res=0
    
    for i in n:
        res = res * 10 + i
    
    return res

def valor(q,j,n):
    if not isinstance((q,n),int) or q < 0 or not isinstance(j,float) or j <= 0 or j>= 1 or n < 0:
        raise ValueError('Argumentos invalidos')
    
def mantem_multiplos(l,n):
    new_l = []
    for i in l:
        if i % n == 0:
            new_l += [i]
    
    return new_l

def mantem_multiplos2(l,n):
    
    for i in range(0,len(l)):
        if l[i] % n != 0:
            l.remove(l[i])

    return l

def duplica_elementos_pares(l):
    lista_n=[]
    for i in range(0,len(l)):
        if l[i]%2==0:
            lista_n+=[l[i]]+[l[i]]
        else:
            lista_n+=[l[i]]
        
    return lista_n

def apenas_digitos_pares(n):
    
    res = 0
    tup=()
    
    while n > 0:
        digito = n % 10
        if digito % 2 == 0:
            tup = (digito,) + tup
            
        n = n // 10
        
    for i in tup:
        res = res * 10 + i
        
    return res 

def codifica(n):
    res = 0
    if not isinstance(n,int) or n < 0:
        raise ValueError('Argumentos invalidos')
    
    while n > 0: 
        digito = n % 10
            
        if digito % 2 == 0:
            if digito == 0:
                res = res * 10 + 8
            elif digito != 0:
                res = res * 10 + digito - 2
            
        elif digito % 2 != 0:
            if digito == 9:
                res = res * 10 + 1
            elif digito != 9:
                res = res * 10 + digito + 2
        
        n = n//10
    
    return res

def parte(lst, i):
    l_menor = []
    l_maior = []
    for j in lst:
        if j < i:
            l_menor += [j]
        
        elif j >= i:
            l_maior += [j]
            
    return [l_menor,l_maior]
    

def retira(l1,l2):
    l_new = []
    for i in l1:
        if i not in l2:
            l_new += [i]
            
    return l_new

from functools import reduce

def soma_cubos_pares(l):
    return reduce(lambda x,y: x + y, map(lambda x: x ** 3, filter(lambda x: x % 2 == 0,l)))


def soma_quadrados_mul3(l):
    return reduce(lambda x,y: x + y, map(lambda x: x ** 2, filter(lambda x: x % 3 == 0,l)))

def todos_lista(l,fn):
    return l == list(filter(fn,l))

def soma_divisores(n):
    
    def aux(n,soma,i):
        if i == 0:
            return soma
        
        elif n % i == 0:
            return aux(n,soma+i,i-1)
        
        else:
            return aux(n,soma,i-1)
        
    return aux(n,0,n)

def reconhece(frase):
    if frase[0] not in 'ABCD':
        return False
    i = 1
    while i <= len(frase) - 1 and frase[i] in '1234':
        i += 1
    if i > 1 != len(frase):
        while i <= len(frase) - 1 and frase[i] in 'ABCD':
            i += 1
        return i == len(frase)
    else:
        return False
    
def soma_cumulativa(l):
    lista = []
    soma = 0
    
    for i in l:
        soma += i
        lista += [soma]
        
    return lista

def conta_palavras(cc):
    def coloca_dic(d,pal):
        if pal in d:
            d[pal] += 1
        else:
            d[pal] = 1
    i = 0
    while cc[i] == ' ':
        i += 1
    res, palavra, ant = {},'',''
    for i in range(i,len(cc)):
        if cc[i] != ' ' or ant != ' ':
            if cc[i] == ' ' and ant != ' ':
                coloca_dic(res,palavra)
                palavra = ''
            else:
                palavra += cc[i]
        ant = cc[i]
    if cc[len(cc) - 1] != ' ':
        coloca_dic(res,palavra)
    return res

def soma_pares(l):
    soma = 0
    for i in l:
        if i % 2 == 0:
            soma += i
            
    return soma

def soma_pares(l):
    if l == []:
        return 0
    
    elif l[0] % 2 == 0:
        return l[0] + soma_pares(l[1:])
    else:
        return soma_pares(l[1:])
    
    
def soma_pares(l):
    def aux_soma_pares(l,soma):
        if l == []:
            return soma
        elif l[0] % 2 == 0:
            return aux_soma_pares(l[1:], soma + l[0])
        else:
            return aux_soma_pares(l[1:], soma)
    return aux_soma_pares(l,0)

from functools import reduce

def soma_pares(l):
    return reduce(lambda x,y: x+y, filter(lambda x: x % 2 == 0, l))
    
    
def vetor(x,y):
    if isinstance((abcissa(arg),ordenada(arg)),(int,float)):
        return {'x': x, 'y': y}
    raise ValueError('vetor: argumentos incorretos')

def abcissa(v):
    return v['x']

def ordenada(v):
    return v['y']

def eh_vetor(arg):
    return isinstance((abcissa(arg),ordenada(arg)),(int,float)) and len(arg) == 2 and 'x' in arg and 'y' in arg

def eh_vetor_nulo(v):
    return abcissa(arg) == 0 and ordenada(arg) == 0

def vetores_iguais(v1,v2):
    return eh_vetor(v1) and eh_vetor(v2) and v1 == v2

def soma_vetores(v1,v2):
    return (abcissa(v1) + abcissa(v2), ordenada(v1) + ordenada(v2))

def soma_digitos(n):
    soma = 0
    if not isinstance(n,int) or n < 0:
        raise ValueError('O argumento deve ser inteiro positivo')
    
    while n > 0:
        digito = n % 10
        soma += digito
        n = n // 10
        
    return soma

def triangular(n):
    if n == 0:
        return False
    else:
        soma = 0
        m=0
        while soma < n:
            m += 1
            soma += m
            
        return soma == n


def parte(lst,e):
    l_menor = []
    l_maior = []
    for i in lst:
        if i < e:
            l_menor += [i]
        elif i >= e:
            l_maior += [i]
    return [l_menor,l_maior]

def codifica2(s):
    l1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
    l2 = ['n','o','p','q','r','s','t','u','v','w','x','y','z']
    new_s = ''
    for i in s:
        if i not in l1 and i not in l2:
            new_s += i
        if i in l1:
            j = l1.index(i)
            new_s += l2[j]
        elif i in l2:
            j = l2.index(i)
            new_s += l1[j]
            
    return new_s


def soma_n_vezes(a,b,n):
    i=0
    while i < n:
        b += a
        i += 1
    return b

def soma_n_vezes(a,b,n):
    if n == 0:
        return b
    else:
        return a + soma_n_vezes(a,b,n - 1)
    
def soma_n_vezes(a,b,n):
    def aux_soma_n_vezes(a,b,n,soma):
        if n == 0:
            return soma
        
        else:
            aux_soma_n_vezes(a,b,n-1,soma+a)
            
    return aux_soma_n_vezes(a,b,n,0)

def soma_quadrados_lista(l):
    return reduce(lambda x,y: x + y, map(lambda x: x ** 2, l))


def reconhece(s):
    d = {'a': 0, 'b': 0, 'c': 0}
    if s[0]!=s[len(s)-1] or s[0]!='a' or s[len(s)-1]!='a':
        return False
    for i in s:
        if i not in d:
            return False
        else:
            d[i] += 1
    if d['a'] % 2 != 0 or d['b'] % 2 != 0:
        return False
    for i in range(0,len(s)-1):
        if (s[i]=='a' and s[i+1]=='c') or (s[i]=='c' and s[i+1]=='a'):
            return False
    if d['a']==0 or d['b']==0 or d['c']==0:
        return False
    return True
    

def multiplos_filtrados(n,pred):
    d={}
    for i in range(1,n+1):
        if pred(i):
            l=[]
            for j in range(1,n+1):
                l += [i * j]
            res[i] = l
    return res

def cria_tempo(h,m):
    if isinstance((h,m),int) and h >= 0 and m >= 0 and m <= 59:
        return {'hora': h, 'min': m}
    raise ValueError('tempo: argumentos inválidos')

def horas(t):
    return t['horas']

def minutos(t):
    return t['minutos']

def eh_tempo(arg):
    return isinstance((h,m),int) and h >= 0 and m >= 0 and m <= 59

def tempos_iguais(t1,t2):
    return eh_tempo(t1) and eh_tempo(t2) and t1 == t2

def depois(t1,t2):
    if tempos_iguais(t1,t2):
        return False
    elif horas(t1) < horas(t2):
        return False
    elif horas(t1) == horas(t2) and minutos(t1) < minutos(t2):
        return False
    return True  

def h_m_s(n):
    if not isinstance(n,int) or n < 0:
        raise ValueError('h_m_s: o argumento deve ser inteiro positivo')
    else:
        h = n//3600
        m = (n - h*3600)//60
        s = n - h*3600 - m*60
    return (h,m,s)

from random import random
def euromilhoes():
    def insere_ord(n,ln):
        if ln == []:
            return [n]
        else:
            i = 0
            while i < len(ln) and ln[i] < n:
                i += 1
            return ln[:i] + [n] + ln[i:]
    def geralista (max_val, comp):
        nums = []
        while len(nums) != comp:
            n = int(max_val * random()) + 1
            if n not in nums:
                nums = insere_ord(n,nums)
        return nums
    return [geralista(50,5),geralista(12,2)]

def triangular(n):
    soma = 0
    i = 1
    while i < n:
        soma += i
        i += 1
        
    return soma == n

def nesimo_triangular(n):
    cont = 0
    num = 1
    while cont != n:  
        if triangular(num):
            cont = cont + 1
        num = num + 1
    return num - 1    

def reconhece2(s):
    letras = 'ABCD'
    nums = '1234'
    if s[0] not in letras or s[-1] not in nums:
        return False
    else:
        for i in range(0,len(s)-1):
            if s[i] not in letras or s[i] not in nums:
                return False            
            if s[i] in nums and s[i+1] in letras:
                return False
    return True

def codifica(s):
    pares = ''
    impares = ''
    for i in range(0,len(s)):
        if i % 2 == 0:
            pares += s[i]
        else:
            impares += s[i]
    return pares + impares

def decodifica(s):
    res = ''
    pares = 0
    if len(s) % 2 == 0:
        impares = len(s) // 2
    else:
        impares = len(texto) // 2 + 1
    while impares < len(s):
        res = res + s[pares] + s[impares]
        pares = pares + 1
        impares = impares + 1
    if len(s) % 2 != 0:
        res = res + s[pares]
    return res

def junta_ordenados(t1,t2):
    tup = ()
    while len(t1) > 0 or len(t2) > 0:
        if len(t1) > 0 and len(t2) > 0:
            if t1[0] < t2[0]:
                tup += (t1,)
                t1 = t1[1:]
            elif t2[0] < t1[0]:
                tup += (t2,)
                t2 = t2[1:]
        if len(t1) == 0:
            for i in t2:
                tup += (i,)
        elif len(t2) == 0:
            for j in t1:
                tup += (j,)
            
    return tup

def conta_menores(tup,n):
    count = 0
    for i in tup:
        if i < n:
            count += 1
    return count

def soma_divisores(n):
    if not isinstance(n,int) or n < 0:
        raise ValueError('o argumento tem que ser um inteiro positivo')
    
    def aux_soma_divisores(n,i,soma):
        if i==n:
            return 0
        
        elif n % i == 0:
            return aux_soma_divisores(n,i+1,soma+i)
        
        else:
            return aux_soma_divisores(n,i+1,soma)
        
    return aux_soma_divisores(n,0,0)

def conhece(s):
    d={'antes': 0, 'b': 0,  'depois': 0}
    letras = 'ab'
    if len(s) % 2 == 0:
        return False
    for i in s:
        if i not in letras:
            return False
    for i in s:
        if i == 'a' and d['b'] == 0:
            d['antes'] += 1
        elif i == 'b':
            d['b'] += 1
        elif i == 'a' and d['b'] >= 1:
            d['depois'] += 1
    if d['b'] != 1:
        return False
    if d['antes'] != d['depois']:
        return False
    return True    

def cria_lista_multiplos(n):
    l = []
    i = 0
    while len(l) < 10:
        if i % n == 0:
            l += [i]
            i += 1
        else:
            i += 1
    return l
    
def parte(l,n):
    menores = []
    maiores = []
    for i in l:
        if i < n:
            menores += [i]
        elif i >= n:
            maiores += [i]
    return [menores, maiores]

def max_div(n,d):
    num = n
    i = d
    while i < n:
        if n % i == 0:
            num = n // i
            i = i * d
        else:
            i = i * d
    return num
    
from functools import reduce

def soma_quadrados(l):
    return reduce(lambda x,y: x + y, map(lambda x: x ** 2,l))


def inverte_dic(d):
    res = {}
    for e in d:
        for v in d[e]:
            if v in res:
                res[v] = res[v] + [e]
            else:
                res[v] = [e]
    return res 

def cria_tempo(h,m):
    if h < 0 or m < 0 or m > 59 or not isinstance((h,m),int):
        raise ValueError('cria_tempo: argumentos inválidos')
    return (h,m)

def horas(t):
    return t[0]

def minutos(t):
    return t[1]

def eh_tempo(arg):
    if type(arg) != tuple or len(arg) != 2:
        return False
    if type(horas(arg))!=int or horas(arg) < 0:
        return  False
    if type(minutos(arg)) != int or minutos(arg) < 0 or minutos(arg) > 59:
        return False
    return True

def tempos_iguais(t1,t2):
    return t1 == t2

def depois(t1,t2):
    if not eh_tempo(t1) or not eh_tempo(t2):
        return False
    if tempos_iguais(t1,t2):
        return False
    if horas(t1) < horas(t2):
        return False
    if horas(t1) == horas(t2) and minutos(t1) < minutos(t2):
        return False
    return True

def f(n):
    if not isinstance(n,int) or n < 0:
        raise ValueError('argumentos inválidos')
    if n < 3 and n >= 0:
        return n
    else:
        return f(n-1) + 2*f(n-2) + 3*f(n-3)


def digitos(n):
    tup = ()
    if not isinstance(n,int) or n < 0:
        raise ValueError('argumentos inválidos')
    while n > 0:
        digito = n % 10
        tup = (digito,) + tup
        n = n // 10
    return tup

def dig_pares(n):
    tup = digitos(n)
    res = 0
    for i in tup:
        if i % 2 != 0:
            res = res * 10 + i
    return res

from functools import reduce

def dig_impares(n):
    return reduce(lambda x,y: x * 10 + y, filter(lambda x: x % 2 != 0, digitos(n)))


    
def soma_divisores(n):
    if n == 0:
        raise ValueError('argumentos inválidos')
    def aux_soma_divisores(n,i,soma):
        if i == n:
            return soma
        elif n % i == 0:
            return aux_soma_divisores(n,i+1,soma+1)
        else:
            return aux_soma_divisores(n,i+1,soma)
    return aux_soma_divisores(n,0,0) 

def conta_linhas(f):
    with open(f,'r') as f:
        n = 0
        lines = f.readlines()
        for linha in linhas:
            if len(linha) > 1:
                n += 1
    return n

def agrupa_por_chave(pares):
    res = {}
    for par in pares:
        if par[0] not in res:
            res[par[0]] = []
        res[par[0]].append(par[1])
    return res
    
    
def soma_divisores_primos(n):
    def aux_soma_divisores_primos(n,i,soma):
        if i == n:
            return soma
        elif eh_primo(i) and n % i == 0:
            return aux_soma_divisores_primos(n,i+1,soma+i)
        else:
            return aux_soma_divisores_primos(n,i+1,soma)
    return aux_soma_divisores_primos(n,0,0)

def soma_divisores_primos(n):
    soma = 0
    for i in range(n):
        if n % i == 0 and eh_primo(i):
            soma += i
    return soma

def numero_digitos_pares(n):
    count = 0
    while n > 0:
        digito = n % 10
        if digito % 2 == 0:
            count += 1
        n = n // 10
    return count

def numero_digitos_pares(n):
    digito = n % 10
    if n == 0:
        return 0
    elif digito % 2 == 0:
        return 1 + numero_digitos_pares(n//10)
    return numero_digitos_pares(n//10)

def numero_digitos_pares(n):
    def aux_numero_digitos_pares(n,count):
        digito = n % 10
        if n == 0:
            return count
        elif digito % 2 == 0:
            return aux_numero_digitos_pares(n//10,count+1)
        else:
            return aux_numero_digitos_pares(n//10,count)
    return aux_numero_digitos_pares(n,0)

def soma_digitos_impares(n):
    digito = n % 10
    if n == 0:
        return 0
    elif digito % 2 != 0:
        return digito + soma_digitos_impares(n//10)
    else:
        return soma_digitos_impares(n//10)
    
def soma_digitos_impares(n):
    def aux_soma_digitos_impares(n,soma):
        digito = n % 10
        if n == 0:
            return soma
        elif digito % 2 != 0:
            return aux_soma_digitos_impares(n//10,soma + digito)
        else:
            return aux_soma_digitos_impares(n//10,soma)
    return aux_soma_digitos_impares(n,0)


def nova_fila():
    return []

def primeiro(fila):
    return fila[0]

def comprimento(fila):
    return len(fila)

def entra_fila(fila,el):
    return fila + [el]

def sai_fila(fila):
    return fila[1:]

def eh_fila(arg):
    return type(lista) == list

def eh_fila_vazia(fila):
    return len(fila) == 0

def junta_filas(f1,f2):
    f = f1 + f2
    return f

def nova_arv():
    return {}

def cria_arv(r, ae, ad):
    return {'raiz': r, 'arv_esq': ae, 'arv_dir': ad}

def raiz(a):
    return ['raiz']

def arv_esq(a):
    return ['arv_esq']

def arv_dir(a):
    return ['arv_dir']

def eh_arv_vazia(a):
    return len(a) == 0

def arv_iguais(a1,a2):
    return a1 == a2

import numpy as np

def leon(a, dif = 1e-6):
    (n,n) = a.shape
    i = np.eye(n)
    p = 1
    while (a**p)-i >= dif:
        i += a**p
        p += 1
    return i
    
    
    
    