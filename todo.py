from functools import reduce

def firstChars(L):
    """ Maps strings in L to a list with the first character of each string.
    For instance:
    firstChars(['python', 'is', 'pythy']) == ['p', 'i', 'p']
    """
    return list( map( lambda x: x[0], L ) )

def sum(L):
    """ Sums the elements in L """
    return reduce( lambda acc, x: acc+x, L, 0 )

def avg(L):
    """ Returns the average of the elements in L """
    return sum(L) / reduce( lambda acc, x: acc+1, L, 0 )
    

def maxString(L):
    """ Retorna a maior string dentre as strings em L.
    Por exemplo: maxString(['python', 'is', 'pythy']) == 'python'
    Se houver empate, retorna a primeira string encontrada.
    """
    return reduce( lambda x, y: x if len(x) >= len(y) else y, L, "" )

def add2Dict(D, N, S):
    """ Insere a string S na lista associada ao inteiro N dentro
    do dicionario D.
    Por exemplo, se D = {1: ['b'], 2: ['xd'], 3: ['abc']}, entao,
    add2Dict(D, 2, 'ww') produz o novo dicionario:
    {1: ['b'], 2: ['xd', 'ww'], 3: ['abc']}
    Voce pode usar essa funcao para completar buildLenFreq
    """
    D[N] = D[N] + [S] if N in D else [S]
    return D

def buildLenFreq(L):
    """ Esta funcao constroi um dicionario que associa inteiros a listas com
    palavras daquele tamanho. Por exemplo:
    ins(['abc', 'xd', 'b', 'xxx']) = {1: ['b'], 2: ['xd'], 3: ['abc', 'xxx']}
    """
    return reduce( lambda D, x: add2Dict(D, len(x), x), L, {} )

def incValue(D, N):
    """Esta funcao incrementa o valor associado a chave N dentro do dicionario
    D. Por exemplo, se D = {1: 2, 2: 4, 3: 11}, entao 
    incValue(D, 2) == {1: 2, 2: 5, 3: 11}
    Voce pode usar essa funcao para completar countFirsts
    """
    D[N] = D[N] + 1 if N in D else 1
    return D

def countFirsts(L):
    """ Conta o numero de ocorrencias do primeiro caracter de cada string em L.
    Por exemplo, countFirsts(['python', 'is', 'pythy']) === {'i': 1, 'p': 2}
    Note que essa funcao retorna um dicionario com cada caracter associada ao
    numero de strings que comecam com aquele caracter.
    """
    return reduce( lambda D, x: incValue(D, x[0]), L, {} )

def mostCommonFirstChar(L):
    """ Retorna a letra mais comum entre as primeiras letras de strings em L.
    Por exemplo:
    mostCommonFirstChar(['python', 'is', 'pythy']) === 'p'
    """
    CF = countFirsts(L)
    return reduce(lambda a, b: a[0] if CF[a[0]] >= CF[b[0]] else b[0], L, L[0])  



L0 = [1, 2, 3, 4, 5, 6, 7]
L1 = ["amora", "abacate", "beterraba", "cereja", "damasco", "ervilha"]

print( "firstChars(L): ", firstChars(L1) )
print( "sum: ", sum(L0) )
print( "avg: ", avg(L0) )
print( "maxString: ", maxString(L1) )

D1 = {1: ['b'], 2: ['xd'], 3: ['abc']}
print( "add2Dict: ", add2Dict(D1, 2, 'ww') )
print( "add2Dict: ", add2Dict(D1, 7, 'aa') )

L2 = ['abc', 'xd', 'b', 'xxx']
print("\nL2: ", L2)
print( "buildLenFreq: ", buildLenFreq(L2) )

D2 = {1: 2, 2: 4, 3: 11}
print( "incValue: ", incValue(D2, 2) )

L3 = ['amar', 'o', 'estranho', 'deixa', 'confuso', 'este', 'coracao']
print( "countFirsts: ", countFirsts(L3) )
print( "mostCommonFirstChar: ", mostCommonFirstChar(L3) )



