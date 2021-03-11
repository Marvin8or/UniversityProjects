# -*- coding: utf-8 -*-
#!/home/marko/anaconda3/bin/python3.8

import numpy as np
import matplotlib.pyplot as plt

n_lett_croatian = 27

def path_size_2_fingers(kl, wl):
    
    if isinstance(kl, str):
        kl = list(kl.replace(' ','').replace(',', '').replace("'", '').replace("[", '').replace("]", ''))
        
    test_words = []
    for w in wl:
        for l in w:
            test_words.append(l.capitalize())
        test_words.append('SPACE')
    
    left_arm = []
    right_arm = []
    
    for iw, w in enumerate(test_words):
        if w == 'SPACE':
            right_arm.append([4, 0])
        else:
            try:
                i_ = kl.index(w)
            except:
                continue
                
            if i_ < 9:
                i = i_
                if i < 4:
                    left_arm.append([i, 3])
                else:
                    right_arm.append([i, 3])
            elif i_ < 18:
                i = i_-9
                if i < 4:
                    left_arm.append([i, 2])
                else:
                    right_arm.append([i, 2])
            elif i_ < 27:
                i = i_-18
                if i < 4:
                    left_arm.append([i, 1])
                else:
                    right_arm.append([i, 1])
    
    X_right_arm = []
    Y_right_arm = []
    X_left_arm = []
    Y_left_arm = []
    l_left = 0
    l_right = 0
    
    for i in left_arm:
        X_left_arm.append(i[0])
        Y_left_arm.append(i[1])
        
    for i in right_arm:
        X_right_arm.append(i[0])
        Y_right_arm.append(i[1])
    
    for i in range(len(X_left_arm)-1):
        l_left += np.sqrt((X_left_arm[i+1]-X_left_arm[i])**2+(Y_left_arm[i+1]-Y_left_arm[i])**2)

    for i in range(len(X_right_arm)-1):
        l_right += np.sqrt((X_right_arm[i+1]-X_right_arm[i])**2+(Y_right_arm[i+1]-Y_right_arm[i])**2)
        
    return l_left+l_right

def plot_path(kl, wl, *save):
    
    if isinstance(kl, str):
        kl = list(kl.replace(' ','').replace(',', '').replace("'", '').replace("[", '').replace("]", ''))
    
    plt.figure(figsize=(10,5))
    for i in range(n_lett_croatian):
        if i < 9:
            plt.plot([i-0.5, i+0.5, i+0.5, i-0.5], [2.5, 2.5, 3.5, 3.5], color='black')     
            plt.annotate(kl[i], (i,3))
        elif i < 18:
            plt.plot([i-0.5-9, i+0.5-9, i+0.5-9, i-0.5-9], [1.5, 1.5, 2.5, 2.5], color='black')
            plt.annotate(kl[i], (i-9,2))
        elif i < 27:
            plt.plot([i-0.5-18, i+0.5-18, i+0.5-18, i-0.5-18], [0.5, 0.5, 1.5, 1.5], color='black')  
            plt.annotate(kl[i], (i-18,1))
    plt.plot([2.5, 5.5, 5.5, 2.5], [-0.5, -0.5, 0.5, 0.5], color='black')  
    plt.vlines(x=-0.5, ymin=0.5, ymax=3.5, color='black')
    plt.vlines(x=2.5, ymin=-0.5, ymax=0.5, color='black')
    plt.annotate('SPACE', (4,0))
    
    test_words = []
    for w in wl:
        for l in w:
            test_words.append(l.capitalize())
        test_words.append('SPACE')
    
    left_arm = []
    right_arm = []
    
    for w in test_words:
        if w == 'SPACE':
            right_arm.append([4, 0])
        else:
            i_ = kl.index(w)
            if i_ < 9:
                i = i_
                if i < 4:
                    left_arm.append([i, 3])
                else:
                    right_arm.append([i, 3])
            elif i_ < 18:
                i = i_-9
                if i < 4:
                    left_arm.append([i, 2])
                else:
                    right_arm.append([i, 2])
            elif i_ < 27:
                i = i_-18
                if i < 4:
                    left_arm.append([i, 1])
                else:
                    right_arm.append([i, 1])
    
    X_right_arm = []
    Y_right_arm = []
    X_left_arm = []
    Y_left_arm = []
    
    for i in left_arm:
        X_left_arm.append(i[0])
        Y_left_arm.append(i[1])
        
    for i in right_arm:
        X_right_arm.append(i[0])
        Y_right_arm.append(i[1])
    
    
    plt.plot(X_left_arm, Y_left_arm, 'b')
    plt.plot(X_right_arm, Y_right_arm, 'r')
    # for i in range(len(X_left_arm)-1):
    #     plt.arrow(X_left_arm[i], Y_left_arm[i], X_left_arm[i+1]-X_left_arm[i], Y_left_arm[i+1]-Y_left_arm[i], color='blue', width=0.04)
    # for i in range(len(X_right_arm)-1):
    #     plt.arrow(X_right_arm[i], Y_right_arm[i], X_right_arm[i+1]-X_right_arm[i], Y_right_arm[i+1]-Y_right_arm[i], color='red', width=0.04)

    
    if save:
        plt.savefig(f'{save}.png')
    
    return

# Test
if __name__ == '__main__':
    keyboard_layout = "['G', 'K', 'R', 'P', 'S', 'I', '\u017d', 'E', 'N', 'A', 'V', '\u0110', 'B', 'F', 'O', 'C', '\u010c', '\u0160', 'J', 'T', 'D', 'U', 'L', 'M', 'H', 'Z', '\u0106']"
    word_list_it = ['Teče', 'i', 'teče', 'teče', 'jedan', 'slap'] 
    plot_path(keyboard_layout, word_list_it)
    print(path_size_2_fingers(keyboard_layout, word_list_it))