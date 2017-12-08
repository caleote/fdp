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
    return request['service'] == 'premium'

def reqTupleToDict(req):
    return {'name':req[0],
         'language':req[1],
         'domain':req[2],
         'service':req[3],
         'duration':req[4]
         }

def opTupleToDict(op):
    return {'name':op[0],
        'language':op[1],
        'domains':op[2],
        'hourFinish':op[3],
        'minutesDone':op[4]
         }

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
    for op in oplist:
        opdict.append(opTupleToDict(op))
    reqlist = read_requests_file(requests)
    premium = []
    fremium = []
    for req in reqlist:
        reqdict = reqTupleToDict(req)
        if isPremium(reqdict):
            premium.append(reqdict)
        else:
            fremium.append(reqdict)
    requests = premium + fremium
    assignments = []
    for req in requests:
        op = findMatchingOperator(opdict, req['duration'], req['language'], req['domain'], current_time)
        if op != None:
            start_time = max_time(current_time, op['hourFinish'])
            assignment = {'operator': op['name'], 'client': req['name'], 'time': start_time}
            op['hourFinish'] = add_minutes(current_time, req['duration'])
        else:
            assignment = {'operator': 'not-assigned', 'client': req['name'], 'time': current_time}
        assignments.append(assignment)
    return assignments

def findMatchingOperator(operators, duration, language, domain, time): # Martim
    '''
    TODO preencer
    :param operators:
    :param language:
    :param domain:
    :param time:
    :return:
    '''

    omin = None
    for op in operators:
        if op['language'] == language and domain in op['domains'] and int(op['minutesDone']) + duration <= 240:
            if omin == None or op['hourFinish'] < omin['hourFinish'] or op['hourFinish'] == omin['hourFinish'] and (op['minutesDone'] < omin['minutesDone'] or op['minutesDone'] == omin['minutesDone'] and op['name'] < omin['name']):
                omin = op
    return omin

ass = assign_tasks('examples/example2/operators11h05.txt','examples/example2/requests11h05.txt', '11:10')
print ('ass:', ass)

def headername(file_name): #Catarina
    in_file = open(file_name, 'r')
    lines = in_file.readlines()
    time = lines[3]
    typeoffile = (lines[6])[:-2]
    in_file.close()
    return time, typeoffile

