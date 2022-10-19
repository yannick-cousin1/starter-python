"""
J'ai essayé d'utiliser la logique combinatoire, mais ces notions étant encore floues, je n'ai pas pu les implémenter
 
L'idée est de définir toutes les combinaisons possible en partant de la chaine de caractère originale.
Par exemple, si la chaine originale contient 3 caractères, il y aura 3! (6) combinaisons possible :
chaine originale = abc
combinaisons = abc / acb / bac / bca / cab / cba
De manière générale, pour une chaine de x caractère, il y aura x! combinaisons possible.
Pour les générer, je dois d'abord générer toute les combinaisons possibles commençant par le 1er caractère
Ensuite, il me suffit de "décaler" (voir fonction "decalage") chacune de ces combinaisons
autant de fois que nécessaire pour obtenir toute les combinaisons.
J'ai réussi à implémenter le décalage, mais pas à générer toutes les combinaisons commençant par un même caractère
Du coup, je n'ai pas non plus implémenter le "main" qui devait ensuite, pour chaque combinaison, chercher si
elle existe dans le dictionnaire (pour ne garder que celle qui y sont). Et de calculer le nombre de point
de chaque combinaison "gagnante".
"""

def length(string):    #function to return length of a string (or a list)
    c = 0
    for i in string:
        c += 1
    return c

def string_to_list(string):   #function to convert a string to a list (each char of the string as a value of the list)
    LIST = []
    for i in string:
        LIST.append(i)
    return LIST

def list_to_string(LIST):   #function to convert a list to a string (each value of the list as a char in the string)
    string = ''
    for i in LIST:
        string += i
    return string

def facto(x):    #Function to calculate facotrial operation (x!)
    res = 1
    while x > 1:
        res *= x
        x -= 1
    return res

def permut(LIST,x,y):    #function to swap two value of a list
    LIST[x],LIST[y] = LIST[y],LIST[x]
    return LIST

def combi(LIST):     #function to create all combination of a string (but keeping the first char always in the first position)
    NLIST = []      #Unfortunately, it doesn't work.
    tmp = LIST[0]
    NLIST.append(list_to_string(LIST))

    for i in range(1,length(LIST)):
        LIST[i-1] = LIST[i]
    LIST.pop()

    for j in range(length(LIST)-1):
        NLIST.append(tmp + list_to_string(decalage(LIST)))
        LIST = decalage(LIST)

    LIST = decalage(LIST)
    permut(LIST)

    print (NLIST)



def decalage(LIST):      # Function to swap values of a list one by one
    tmp = LIST[0]        # ( exemple, list = [ 'a','b','c'] will return a list = ['b','c','a'] )
    for j in range(length(LIST)-1):
        LIST[j] = LIST[j+1]
    LIST[-1] = tmp
    return LIST



def ana(string):       #Second try to make my thing , but it doesn't work neither
    LIST = string_to_list(string)
    NLIST = []

    NLIST.append(list_to_string(LIST))
    for i in range(1,length(LIST)):
        NLIST.append(list_to_string(decalage(LIST)))

    decalage(LIST)
    permut(LIST,-1,-2)
    NLIST.append(list_to_string(LIST))
    for j in range(1,length(LIST)):
        NLIST.append(list_to_string(decalage(LIST)))

    decalage(LIST)
    permut(LIST,-1,-2)
    permut(LIST,-2,-3)



    print(NLIST)
    print(LIST)

################################################


### main

letters = input("Entrez vos lettres : ")
word = ''
LIST = []
p = facto(length(letters))


ana(letters)
