# -*- coding: utf-8 -*-
"""
Created on Sun May  1 20:21:42 2016

@author: Breno
"""
import random

class Batalha:
    def __init__(self):
        self.jogadas=[]
        self.matriz_1=[[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20],
                     [21,22,23,24,25,26,27,28,29,30],[31,32,33,34,35,36,37,38,39,40],
                     [41,42,43,44,45,46,47,48,49,50],[51,52,53,54,55,56,57,58,59,60],
                     [61,62,63,64,65,66,67,68,69,70],[71,72,73,74,75,76,77,78,79,80],
                     [81,82,83,84,85,89,90],[91,92,93,94,95,96,97,98,99,100]]
        
        self.matriz_2=[[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20],
                     [21,22,23,24,25,26,27,28,29,30],[31,32,33,34,35,36,37,38,39,40],
                     [41,42,43,44,45,46,47,48,49,50],[51,52,53,54,55,56,57,58,59,60],
                     [61,62,63,64,65,66,67,68,69,70],[71,72,73,74,75,76,77,78,79,80],
                     [81,82,83,84,85,89,90],[91,92,93,94,95,96,97,98,99,100]]
         
    def vez_jogador(self,linha,coluna):  
        if len(self.jogadas) % 2 == 0:
            self.matriz_1[linha][coluna]='jogador 1'
            self.jogadas.append(1)  
            self.proxima='jogador 2'
            return 'jogador 1' 
        else: 
            self.matriz_1[linha][coluna]='jogador 1' 
            self.jogadas.append(1)  
            self.proxima='jogador 1'
            return 'jogador 2' 
        print(self.matriz_1)




class Barco:
    nada = 0
    água = 1
    acerto = 2
    afundou = 3
    outro = -1
    
    tamahos = {
        "a" : 5,
        "b" : 4,
        "d" : 3,
        "s" : 3,
        "m" : 2
    }
    
    abreviações = [
        "a",
        "b",
        "d",
        "s",
        "m"
    ]
    
    nomes = {
        "a" : "porta-aviões",
        "b" : "cruzador",
        "d" : "navio",
        "s" : "patrulheiro",
        "m" : "bote"
    }
    
    confirmações = {
        nada : "nada",
        água : "água",
        acerto : "acerto",
        afundou : "afundou"
    }
    
    embarcações = [
       
        "porta-aviões",
        "cruzador",
        "navio",
        "patrulheiro",
        "bote"

    ]



    @staticmethod
    def adquirir_nome_estado(state):
        
        return {Barco.nada : "nada",
                Barco.acerto : "acerto",
                Barco.afundou : "afundou"} [state]

    def __init__(self, x=None, y=None, type=None, vertical=None):
        
        self._x = x
        self._y = y
        self._type = type
        self._vertical = vertical
        self._nome_completo = None
        
        if self._type is not None:
            assert self._type in self.tamanhos.keys()
            self._tamanhos = Barco.tamanhos[self._type]
            
            for nomes in self.Barco:
                if nomes.lower()[0] == self._type:
                    self._nome_completo = nomes
                    break
        
        self._acerto = set([])


    def teste_vertical(self):
        
        return self._vertical
        
    def coordenadas(self):

        return (self._x, self._y)
        
    def origem(self):
        
        return self.coords()
        
    def get_size(self):
    
        return self._size
        
    def quadrados_ocupados(self):
        
        if self._vertical:
            return [(self._x, self._y + i) for i in range(self._size)]
        else:
            return [(self._x + i, self._y) for i in range(self._size)]
            
    def get_covering_set(self):
        '''Return the *set* of covering squares.'''
        
        return set(self.get_covering_squares())
        
    def lista_acertos(self):
        
        return [coord in self._hit for coord in self.get_covering_squares()]
        
    def marcador(self, x, y):
    
        self._hit.add((x, y))
        
    def rotate(self):
        
        self._vertical = not self._vertical

class colocar_barcos:
     """docstring for colocar_barcos"""


    tamanho_barco = 20
    cor_barco = "blue"
    tag = "area_barco"
    tamanho = 150

