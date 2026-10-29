import numpy as np
import networkx as nx
import scipy as sp

def leer_archivo(input_file_path):

    f = open(input_file_path, 'r')
    n = int(f.readline())
    m = int(f.readline())
    W = np.zeros(shape=(n,n))
    for _ in range(m):
        line = f.readline()
        i = int(line.split()[0]) - 1
        j = int(line.split()[1]) - 1
        W[j,i] = 1.0
    f.close()
    
    return W

def dibujarGrafo(W, print_ejes=True):
    
    options = {
    'node_color': 'yellow',
    'node_size': 200,
    'width': 3,
    'arrowstyle': '-|>',
    'arrowsize': 10,
    'with_labels' : True}
    
    N = W.shape[0]
    G = nx.DiGraph(W.T)
    
    #renombro nodos de 1 a N
    G = nx.relabel_nodes(G, {i:i+1 for i in range(N)})
    if print_ejes:
        print('Ejes: ', [e for e in G.edges])
    
    nx.draw(G, pos=nx.spring_layout(G), **options)

def calcularRanking(W, p):
    #Hago descomposición LU de la martiz contectividad escalonada
    LU = desc_lu(matriz_conectividad(W, p))

    #Crea los vectores a partir de desc_lu()
    L = LU[0]
    U = LU[1]
    e = np.ones(L.shape[0])

    #Resuelve el sistema LUx = e (Ux = y,  Ly = e). Donde scr es el vector con el valor de cada página
    y = sp.linalg.solve_triangular(L, e, lower = True)
    scr = sp.linalg.solve_triangular(U, y, lower = False)

    #Normaliza el vector
    k = np.sum(scr)
    scr /= k

    #Sorting del vector según el indice
    rnk = np.argsort(scr)[::-1] + 1

    return rnk, scr

def obtenerMaximoRankingScore(M, p):
    output = -np.inf
    # calculo el ranking y los scores
    rnk, scr = calcularRanking(M, p)
    output = np.max(scr)
    
    return output


'''
--------------------------------------- FUNCIONES AUXILIARES ---------------------------------------
'''

#Crea la matriz (I - p * WD) a partir de una matriz de entrada y el valor p
def matriz_conectividad(M, p):
    R = np.copy(M)
    cant_pag = R.shape[0]

    #Divide la columna por la suma de la misma (al ser todos 1 es la cantidad de links)
    for k in range(0, cant_pag):
        den = R[:, k].sum()
        if den != 0:
            R[:, k] /= den

    # Devuelve la matriz (I - p * WD)
    return np.identity(cant_pag) - (R*p)



#Escalona la matriz, pero en vez de ir dejando ceros, deja el vector r. Devuelve una matriz del tipo L + U (L sin unos en la diagonal)
def escalonar_matriz(M):
    A = np.copy(M)
    dim = A.shape[0]

    #Itera sobre la dimensión de la matriz, va haciendo el algoritmo sobre A[i:][i:]
    for i in range(0, dim):
        #Pivoteo parcial (Busco la fila de mayor valor, y la intercambio con la primera)
        fila_mayor = A[i:, i].argmax() + i
        A[[i,fila_mayor],i:] = A[[fila_mayor,i],i:]

        #Restamos el multiplo de la primera, exeptuando la primer columna 
        for j in range(i+1, dim):
            A[j, i+1:] -= (A[i, i+1:] * (A[j,i]/A[i,i]))
            
        #Asignamos el valor r al primer elemento de la fila
        A[i+1:, i] /= A[i,i]

    return A




#Separa la matriz en dos. Devuelve L y U en una tupla
def separar_matriz(M):
    A = np.copy(M)
    dim = A.shape[0]

    #De la matríz A, copia el triangulo inferior, le resta su misma diagonal y le suma la identidad
    L = (np.tril(A) - np.diag(np.diag(np.tril(A)))) + np.identity(dim)
    #De la matríz A, copia el triangulo superior
    U = np.triu(A)

    return (L, U)



#Llama dos funciones (escalonar y separar), devuelve (L, U)
def desc_lu(M):
    A = np.copy(M)
    return separar_matriz(escalonar_matriz(A))