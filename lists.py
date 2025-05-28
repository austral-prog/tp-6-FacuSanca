
def remove_elements(list_to_remove_elements):
    lista = list_to_remove_elements
    if len(lista) > 5:
        del lista[5]
    if len(lista) > 4:
        del lista[4]
    if len(lista) != 0:
        del lista[0]
    
    return(lista)


def add_elements(list_to_add_elements):
    lista = list_to_add_elements
    lista.insert(0 , "Pink")
    lista.insert(len(lista) , "Yellow") 
    return(lista)


def is_empty(list_to_check):
    if len(list_to_check) == 0:
        return True
    else:
        return False

def check_lists(list_to_compare1, list_to_compare2):
    lista1 = list_to_compare1
    lista2 = list_to_compare2
    if len(lista1)>2 and len(lista2) > 2:
        if lista1[2] == lista2[2]:
            return True
        else:
            return False
    else:
        return False

def list_of_lists(list_of_lists_to_modify):
    lista = list_of_lists_to_modify
    #1
    lista2 = lista[0]
    lista2 = lista2[0:2]
    #2
    lista3 = lista[1]
    lista3 = lista3[1:4]
    #3
    lista4 = lista[2]
    lista4 = lista4[ -2: ]
    abc = [lista2, lista3, lista4]
    return abc    


