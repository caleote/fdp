# coding=utf-8
# 2017-2018 Fundamentos de Programação (MI)
# Grupo 008
# 51705 Catarina Sofia Esteves Leote
# 50701 Martim Duarte da Costa Seco

from dateTime import *

def assign_tasks(operators, requests, current_time): #Catarina Martim
    """Assign operators to pending requests.

    Requires:
    - operators, a collection of operators, structured as the output of
      filesReading.read_operators_file;
    - requests, a list of requests, structured as the output of filesReading.read_requests_file;
    - current_time, str with the HH:MM representation of the time for this update step.
    Ensures: a list of assignments of operators to requests, according to the conditions indicated
    in the general specification (omitted here for the sake of readability).
    """
    
    #TODO ordenar primium e fremium

    assignments = []
    for r in requests:
        #encontrar operador mach
        o = find_matching_operator(operators, r['language'], r['domain'], current_time)

        if o != None:
            start_time = max_time(current_time, o['hourFinish'])

            assignment = {'operator' : o['name'], 'client' : r['name'], 'time' : start_time}

        else:
            assignment = {'operator': 'not-assigned', 'client': r['name'], 'time': current_time}

        assignments.append(assignment) #começa com lista vazia e vai adicionando um operador a um request
    # When all assignments are done :
    return assignments




#TODO find mach ope
def find_matching_operator(operators, language, domain, time): # Martim
    '''
    TODO preencer
    :param operators:
    :param language:
    :param domain:
    :param time:
    :return:
    '''

    # Ordena-se primeiro... faltam os desempates e a reordenação depois de um update

    for o in operators:
        if o['language'] == language and domain in o['domains']:
            return o

    return None


