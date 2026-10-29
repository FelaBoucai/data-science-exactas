#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Práctica 1 - Ejercicio 21
"""

import numpy as np

def traza(A):
    resp = 0
    minTraza = 1
    i = 0
    if ((A.shape)[0] <= (A.shape)[1]):
        minTraza = (A.shape)[0]
    else:
        minTraza = (A.shape)[1]

    while (i < minTraza):
        resp = resp + A[i,i]
        i = i + 1
    return resp

def sumamodulo(A):
    resp = 0
    filas = (A.shape)[0]
    columnas = (A.shape)[1]
    _fila = 0
    _columna = 0

    while (_fila < filas):
        while(_columna < columnas):
            resp = resp + np.abs(A[_fila, _columna])
            _columna = _columna + 1
        _columna = 0
        _fila = _fila + 1

    
    return resp


def positivosmayoresanegativos(A):
    resp = True
    neg = 0
    pos = 0
    filas = (A.shape)[0]
    columnas = (A.shape)[1]
    _fila = 0
    _columna = 0

    while (_fila < filas):
        while(_columna < columnas):
            if (A[_fila, _columna] <= 0):
                neg = neg + np.abs(A[_fila, _columna])
            else:
                pos = pos + np.abs(A[_fila, _columna])
            _columna = _columna + 1
        _columna = 0
        _fila = _fila + 1

    resp = pos > neg
    return resp


def main():

    #Definición de matriz
    A = np.array([[ 1, -2, -1, -2],
                  [-4, -4,  5, -9],
                  [-9,  0,  8, -1],
                  [ 8,  3,  3, -3]])

    print('Matriz A\n', A)
    
    print('Traza de A:', traza(A))
    assert traza(A)==2
    
    print('Suma en módulo de elementos de A:', sumamodulo(A))
    assert sumamodulo(A)==63
    
    print('Positivos mayores a negativos?:', positivosmayoresanegativos(A))
    assert positivosmayoresanegativos(A)==False


if __name__ == "__main__":
    main()
    