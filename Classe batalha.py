# -*- coding: utf-8 -*-
"""
Created on Sun May  1 20:21:42 2016

@author: Breno
"""
import random
import numpy as np
class Batalha:
    def __init__(self):
        self.jogadas=[]
        self.matriz_1=[[,0,0,0,0,0,0,0,0,0,0][0,0,0,0,0,0,0,0,0,0][0,0,0,0,0,0,0,0,0,0[]0,0,0,0,0,0,0,0,0,0][0,0,0,0,0,0,0,0,0,0]
                      [0,0,0,0,0,0,0,0,0,0][0,0,0,0,0,0,0,0,0,0][0,0,0,0,0,0,0,0,0,0][0,0,0,0,0,0,0,0,0,0][0,0,0,0,0,0,0,0,0,0]]
        
        self,matriz_2=[[,0,0,0,0,0,0,0,0,0,0][0,0,0,0,0,0,0,0,0,0][0,0,0,0,0,0,0,0,0,0[]0,0,0,0,0,0,0,0,0,0][0,0,0,0,0,0,0,0,0,0]
                      [0,0,0,0,0,0,0,0,0,0][0,0,0,0,0,0,0,0,0,0][0,0,0,0,0,0,0,0,0,0][0,0,0,0,0,0,0,0,0,0][0,0,0,0,0,0,0,0,0,0]]
                      
         
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

    def conflito_posição_barcos(self, other):
        
        s1 = self.get_covering_set()
        s2 = other.get_covering_set()
        return len(s1.intersection(s2)) > 0
        
    def get_nome(self):
    
        return self._type
        
    def get_abreviação(self):
        
        return self._type
        
    def get_nome_completo(self):
        
        return self._full_name
        
    def teste_afundou(self):
    
        return len(self._acerto) == self._tamanhos
        
    def _get_str_v(self):
        if self._vertical:
            return "vertical"
        else:
            return "horizontal"
        
    def __str__(self):
        return "Barco %s @ %s orientado %sly" % (self._type, str((self._x, self._y)), self._get_str_v())

class Carrega_Barco(object):
    '''Load ship object from a file.'''
    
    @staticmethod
    def read(fname):
        f = open(fname)
        barcos = []
        
        for line in f:
            if len(line.strip()) == 0 or line.strip().count(" ") != 3:
                continue
                
            barco_type, x, y, v = l = line.strip().split()
            
            if barco_type in Barco.tamanhos:
                barcos = Barco(x=int(x), y=int(y), type=barco_type, vertical=v)
                embarcações.append(barcos)
                
        f.close()
                
        return embarcações

class colocar_barcos:
     """docstring for colocar_barcos"""


    tamanho_barco = 20
    cor_barco = "blue"
    tag = "area_barco"
    tamanho = 150

