# 2017-2018 Fundamentos de Programacao  (MI)
# Grupo 008
# 51705 Catarina Sofia Esteves Leote
# 50701 Martim Duarte da Costa Seco

from dateTime import *
from filesReading import *
from constants import *

def isPremium(request):
    """
    Returns the information if the service of the request is premium or not
    Requires:
    - request, one request, structures as the output of filesReading.read_request_file with a service.
    Ensures: that returns True if the service of a request is premium and False if it is not.
    """
    return request['service'] == 'premium'

def reqTupleToDict(req):
    '''
    Returns a dictionary with the requests keys
    Requires:
    - req, a tuple with one request
    Ensures: a dictionary with the values of the tuple inserted
    '''
    return {'name':req[0],
         'language':req[1],
         'domain':req[2],
         'service':req[3],
         'duration':int(req[4])
         }

def opTupleToDict(op):
    '''
    Returns a dictionary with the operators keys
    Requires:
    - op, a tuple with one operator
    Ensures: a dictionary with the values of the tuple inserted
    '''
    return {'name':op[0],
        'language':op[1],
        'domains':op[2],
        'hourFinish':op[3],
        'minutesDone':int(op[4])
         }

def assign_tasks(operators, requests, current_time):
    """
    Assign operators to pending requests.
    Requires:
    - operators, a collection of operators, structured as the output of
      filesReading.read_operators_file;
    - requests, a list of requests, structured as the output of filesReading.read_requests_file;
    - current_time, str with the HH:MM representation of the time for this update step.
    Ensures: a list of assignments of operators to requests, according to the conditions indicated
    in the general specification (omitted here for the sake of readability) and a list of operators.
    """
    opdict = []
    for op in operators:
        opdict.append(opTupleToDict(op))
    premium = []
    fremium = []
    for req in requests:
        reqdict = reqTupleToDict(req)
        if isPremium(reqdict):
            premium.append(reqdict)
        else:
            fremium.append(reqdict)
    requests = premium + fremium
    assignments = []
    for req in requests:
        op = findMatchingOperator(opdict, req['duration'], req['language'], req['domain'])
        if op != None:
            start_time = max_time(current_time, op['hourFinish'])
            op['minutesDone'] = op['minutesDone'] + req['duration']
            assignment = {'operator': op['name'], 'client': req['name'], 'time': start_time}
            op['hourFinish'] = add_minutes(start_time, req['duration'])
        else:
            assignment = {'operator': 'not-assigned', 'client': req['name'], 'time': current_time}
        assignments.append(assignment)
        #print(assignment)
    return assignments, opdict

def findMatchingOperator(operators, duration, language, domain):
    '''
    Finds the matching operator to a given request
    Requires:
    - operators, a dictionary of operators
    - duration, the duration of a given request
    - language, the language of a given request
    - domain, the domain of a given request
    Ensures: an operator that is the match for the given request
    '''
    omin = None
    for op in operators:
        if op['language'] == language and domain in op['domains'] and op['minutesDone'] + duration <= 240:
            if (omin == None or
                op['hourFinish'] < omin['hourFinish'] or
                op['hourFinish'] == omin['hourFinish'] and
                op['minutesDone'] < omin['minutesDone'] or
                op['minutesDone'] == omin['minutesDone'] and op['name'] < omin['name']):
                omin = op
    return omin