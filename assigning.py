# coding=utf-8
# 2017-2018 Fundamentos de Programação (MI)
# Grupo 008
# 51705 Catarina Sofia Esteves Leote
# 50701 Martim Duarte da Costa Seco

from dateTime import *
from filesReading import *

def isPremium(request): #Catarina
    """
    Returns the information if the service of the request is premium or not
    Requires:
    - request, one request, structures as the output of filesReading.read_request_file with a service.
    Ensures: that returns True if the service of a request is premium and False if it is not.
    """
    if request['service'] == 'premium':
        return True
    else:
        return False

def assign_tasks(operators, requests, current_time): #Catarina Martim
    """
    Assign operators to pending requests.
    Requires:
    - operators, a collection of operators, structured as the output of
      filesReading.read_operators_file;
    - requests, a list of requests, structured as the output of filesReading.read_requests_file;
    - current_time, str with the HH:MM representation of the time for this update step.
    Ensures: a list of assignments of operators to requests, according to the conditions indicated
    in the general specification (omitted here for the sake of readability).
    """

    oplist = read_operators_file(operators)
    opdict = []
    for t in range (len(oplist)):
        opdict.append(
        {'name':oplist[t][0],
        'language':oplist[t][1],
        'domains':oplist[t][2],
        'hourFinish':oplist[t][3],
        'minutesDone':oplist[t][4]
         })

    reqlist = read_requests_file(requests)
    reqdict = []
    for t in range (len(reqlist)):
        reqdict.append(
        {'name':reqlist[t][0],
         'language':reqlist[t][1],
         'domain':reqlist[t][2],
         'service':reqlist[t][3],
         'duration':reqlist[t][4]
         })
    assignments = []
    fremiumList = []
    for req in reqdict:
        if isPremium(req) == True:
            #encontrar operador match
            op = findMatchingOperator(opdict, req['language'], req['domain'], current_time)

            if op != None:
                start_time = max_time(current_time, op['hourFinish'])

                assignment = {'operator': op['name'], 'client': req['name'], 'time': start_time}
                op['minutesDone'] = int(op['minutesDone']) + req['duration']
                op['hourFinish'] = add_minutes(current_time, req['duration'])
            else:
                assignment = {'operator': 'not-assigned', 'client': req['name'], 'time': current_time}

            assignments.append(assignment) #começa com lista vazia e vai adicionando um operador a um request
        else:
            fremiumList.append(req)

    for fre in fremiumList:
        op = findMatchingOperator(opdict, fre['language'], fre['domain'], current_time)
        if op != None:
            start_time = max_time(current_time, op['hourFinish'])
            assignment = {'operator': op['name'], 'client': fre['name'], 'time': start_time}
            op['minutesDone'] = int(op['minutesDone']) + fre['duration']
            op['hourFinish'] = add_minutes(current_time, fre['duration'])
        else:
            assignment = {'operator': 'not-assigned', 'client': fre['name'], 'time': current_time}
        assignments.append(assignment)
    # When all assignments are done :
    return assignments

def findMatchingOperator(operators, language, domain, time): # Martim
    '''
    TODO preencer
    :param operators:
    :param language:
    :param domain:
    :param time:
    :return:
    '''

    #TODO Ordenar (com desempates e reordenação depois do update)
    # Ordena-se primeiro... faltam os desempates e a reordenação depois de um update

    for op in operators:
        if op['language'] == language and domain in op['domains']:
            return op
    return None

def headername(file_name): #Catarina
    in_file = open(file_name, 'r')
    lines = in_file.readlines()
    time = lines[3]
    typeoffile = (lines[6])[:-2]
    in_file.close()
    return time, typeoffile