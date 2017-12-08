# coding=utf-8
# 2017-2018 Fundamentos de Programação (MI)
# Grupo 008
# 51705 Catarina Sofia Esteves Leote
# 50701 Martim Duarte da Costa Seco

from dateTime import *
from filesReading import *
from constants import *

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
            op = findMatchingOperator(opdict, req['duration'], req['language'], req['domain'], current_time)

            if op != None:
                start_time = max_time(current_time, op['hourFinish'])

                assignment = {'operator': op['name'], 'client': req['name'], 'time': start_time}
                op['hourFinish'] = add_minutes(current_time, req['duration'])
            else:
                assignment = {'operator': 'not-assigned', 'client': req['name'], 'time': current_time}

            assignments.append(assignment) #começa com lista vazia e vai adicionando um operador a um request
        else:
            fremiumList.append(req)

    for fre in fremiumList:
        op = findMatchingOperator(opdict, fre['duration'], fre['language'], fre['domain'], current_time)
        if op != None:
            start_time = max_time(current_time, op['hourFinish'])
            assignment = {'operator': op['name'], 'client': fre['name'], 'time': start_time}
            op['hourFinish'] = add_minutes(current_time, fre['duration'])
        else:
            assignment = {'operator': 'not-assigned', 'client': fre['name'], 'time': current_time}
        assignments.append(assignment)
    # When all assignments are done :
    return assignments

def minMinutes(minutes1, minutes2):
    '''
    #TODO preencher
    :param minutes1:
    :param minutes2:
    :return:
    '''
    minutes1 = int(minutes1)
    minutes2 = int(minutes2)
    if minutes1 <= minutes2:
        return minutes1
    else:
        return minutes2

def firstInAlphabet(word1, word2):
    '''
    #TODO preencher
    SE HOUVER TEMPO CORRIGIR ISTO PARA O CASO DA ANA E DA ANABELA
    :param word:
    :return:
    '''
    if word1 == word2:
        return word1
    else:
        for l in range (len(word1)):
            if word1[l] == word2[l]:
                l += 1
            else:
                if word1[l] < word2[l]:
                    return word1
                else:
                    return word2

def findMatchingOperator(operators, duration, language, domain, time): # Martim
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
        for op2 in operators:
            if op2 != op:
                if op['language'] == language and domain in op['domains']:
                    print('op14:', op['name'])
                    print('op24:', op2['name'])
                    if op['hourFinish'] == str(min_time(op['hourFinish'], op2['hourFinish'])):
                        print('op15:', op['name'])
                        print('op25:', op2['name'])
                        if op['minutesDone'] == str(minMinutes(op['minutesDone'], op2['minutesDone'])):
                            op['minutesDone'] = int(op['minutesDone']) + duration
                            if op['minutesDone'] <= 240:
                                if op['name'] == firstInAlphabet(op['name'], op2['name']):
                                    return op
    return None

operators = [('Tiago','french','laptops', '16:50','113'), ('Helena','french', 'laptops', '16:57', '198')]
ass = assign_tasks('operators16h55.txt', 'requests16h55.txt', '17:00')
print ('ass:', ass)


def headername(file_name): #Catarina
    in_file = open(file_name, 'r')
    lines = in_file.readlines()
    time = lines[3]
    typeoffile = (lines[6])[:-2]
    in_file.close()
    return time, typeoffile

