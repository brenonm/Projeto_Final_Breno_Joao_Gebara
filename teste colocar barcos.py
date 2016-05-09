# -*- coding: utf-8 -*-
"""
Created on Mon May  9 17:15:47 2016

"""

import random

def colocar_barcos(self):
        escolhas= range(100)
        random.shuffle(escolhas)
        self.locations={}
        for ctr, lit in enumerate (("porta-aviões", "cruzador", "navio", "patrulheiro")):
            chave=escolhas[ctr]
            self.locations[chave]=lit
            print (lit, chave)