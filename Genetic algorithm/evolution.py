# -*- coding: utf-8 -*-
#!/home/marko/anaconda3/bin/python3.8

import numpy as np
import os
from sys import platform
import random
import json


n_species = 100
p_death = 0.4
n_words = 1000
p_mutation = 0.1
mutation_random = [True]*int(p_mutation*1000) + [False]*int((1-p_mutation)*1000)

n_evolution = 51

cwd = os.getcwd()
if platform == "linux" or platform == "linux2":
    # Linux
    tmp = f'/{n_species}_{p_death}_{p_mutation}_{n_words}'
elif platform == "win64" or platform == "win32":
    # Windows...
    tmp = f'\{n_species}_{p_death}_{p_mutation}_{n_words}'
    
from path import path_size_2_fingers
from path import plot_path

if not os.path.exists(cwd+tmp):
    os.mkdir(cwd+tmp)

# Loading word count    
f = open("data.txt", 'r')
word_count = f.readlines()[0]
f.close()
word_count = word_count[1:-1]
word_count = word_count.replace(":", "").replace(",", "").replace("'", "").split(' ')

# Sorting
word_count_int = []
for i in word_count[1::2]:
    word_count_int.append(int(i))
SRT = np.argsort(word_count_int)[::-1]
word_count = word_count[0::2]
word_stats = []
for i in range(len(word_count)):
    if word_count_int[SRT[i]] == 0:
        continue
    word_stats.append(word_count[SRT[i]])

all_letters = ['Ć', 'Č', 'E', 'R', 'T', 'Z', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Đ', 'Š', 'C', 'V', 'B', 'N', 'M', 'Ž']

def word_list_random():
    word_list_random = []
    for i in range(n_words):
        loc = int(np.random.triangular(0, 0, len(word_stats), 1))
        word_list_random.append(word_stats[loc])
    return word_list_random

def evolution0():
    cwd = os.getcwd()
    if platform == "linux" or platform == "linux2":
        # Linux
        tmp = f'/{n_species}_{p_death}_{p_mutation}_{n_words}/evolutions0.json'
    elif platform == "win64" or platform == "win32":
        # Windows...
        tmp = f'\{n_species}_{p_death}_{p_mutation}_{n_words}\evolutions0.json'
     
    if os.path.exists(cwd+tmp):
        print('Evolution 0 already exists.')
        return
    
    word_list = word_list_random()
    evolution_stats = []
    for i in range(n_species):
        random.shuffle(all_letters)
        evolution_stats.append([str(all_letters), path_size_2_fingers(all_letters, word_list)])
        
    with open(cwd+tmp, 'w') as f:
        json.dump(evolution_stats, f, indent=2)
    f.close()
    return

evolution0()

def mutation(kl):
    kl = kl.replace("[", "").replace(",", "").replace("]", "").replace("'", "").replace(" ", "")
    kl_new = []
    for k in kl:
        kl_new.append(k)
    for i in range(27):
        if np.random.choice(mutation_random) == True:
            if i == 26:
                kl_new[i], kl_new[0] = kl_new[0], kl_new[i]
            else:
                kl_new[i], kl_new[i+1] = kl_new[i+1], kl_new[i]
    return kl_new

def start_evaluation():
    for e in range(n_evolution):
            
            cwd = os.getcwd()
            if platform == "linux" or platform == "linux2":
            # Linux
                tmp = f'/{n_species}_{p_death}_{p_mutation}_{n_words}/evolutions{e}.json'
            elif platform == "win64" or platform == "win32":
            # Windows...
                tmp = f'\{n_species}_{p_death}_{p_mutation}_{n_words}\evolutions{e}.json'
                
            print('Evolution:', e)
            
            with open(cwd+tmp, 'r') as f:
                evolutions_it = json.load(f)
            f.close()
            
            # Sortin, min to max path
            arg = []
            key = []
            for it in evolutions_it:
                arg.append(it[1])
                key.append(it[0])
            SRT = np.argsort(arg)
            evolutions_sort = [None]*n_species
            for i in range(n_species):
                evolutions_sort[i] = key[SRT[i]]
            print(f'Best layout for evolution {e}:', evolutions_sort[0], 'Path size:', arg[SRT[0]]) 
            
            P_death = int(n_species*p_death)
            evolutions_sort = evolutions_sort[:-(P_death)]
            
            t = -1
            new_species = evolutions_sort[:]
            while len(new_species) < n_species:
                specie = evolutions_sort[t]
                mutation_specie = mutation(specie)
                t -= 1
                new_species.append(mutation_specie)
                
            if platform == "linux" or platform == "linux2":
            # Linux
                tmp = f'/{n_species}_{p_death}_{p_mutation}_{n_words}/evolutions{e+1}.json'
            elif platform == "win64" or platform == "win32":
            # Windows...
                tmp = f'\{n_species}_{p_death}_{p_mutation}_{n_words}\evolutions{e+1}.json'
            
            if os.path.exists(cwd+tmp):
                print(f'Evolution {e+1} already exists.')
                continue
            
            word_list = word_list_random()
            evolution_stats = []
            for i in range(n_species):
                ns = new_species[i]
                evolution_stats.append([str(ns), path_size_2_fingers(ns, word_list)])
                
            with open(cwd+tmp, 'w') as f:
                json.dump(evolution_stats, f, indent=2)
            f.close()
            
start_evaluation()  

# Graf konvergencija
# Prikaz najboljeg rješenja

plot_path(['D', 'V', 'Š', 'L', 'H', 'F', 'M', 'Ž', 'Ć', 'P', 'O', 'I', 'Z', 'B', 'J', 'N', 'S', 'Č', 'C', 'R', 'K', 'G', 'E', 'A', 'T', 'U', 'Đ'] , [''])      
        
        
        
        
        
        
        
        
        