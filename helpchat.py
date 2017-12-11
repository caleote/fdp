# 2017-2018 Fundamentos de Programacao (MI)
# Grupo 008
# 51705 Catarina Sofia Esteves Leote
# 50701 Martim Duarte da Costa Seco

import assigning
import constants
from filesReading import *
from filesWriting import *
import sys

def main(op_in, req_in):
    '''
    This is the main function, that reads the two input files (the operators and requests)
    and produces the output files (the timetable and the updated operators)
    Requires:
    - op_in, the filename for the input operators data
    - req_in, the filename for the input requests data
    Ensures: that the output files are written with the specifications
    (omitted here for the sake of readability)
    '''


    # Exceptions:
    operators = read_operators_file(op_in)
    requests = read_requests_file(req_in)
    oday, otime, ocompany, otype = readHeader(op_in)
    rday, rtime, rcompany, rtype = readHeader(req_in)
    op_in_min, op_in_hour, op_in_type = readFileNameOp(op_in)
    req_in_min, req_in_hour, req_in_type = readFileNameReq(req_in)

    '''  
    try:
        assert(otype.lower() == op_in_type and otime == op_in_hour+':'+op_in_min)
    except AssertionError:
        raise IOError('Error in input file: inconsistency between name and header in file ' + op_in)

    try:
        assert(rtype.lower() == req_in_type and rtime == req_in_hour+':'+req_in_min)
    except AssertionError:
        raise IOError('Error in input file: inconsistency between name and header in file ' + req_in)

    try:
        assert(oday == rday and otime == rtime and ocompany == rcompany)
    except AssertionError:
        raise IOError ('Error in input file: inconsistency between files ' + op_in + ' and ' + req_in)

    current_time = otime'''



    if otype.lower() != op_in_type or otime != op_in_hour+':'+op_in_min:
        raise IOError ('Error in input file: inconsistency between name and header in file ' + op_in)
    if rtype.lower() != req_in_type or rtime != req_in_hour+':'+req_in_min:
        raise IOError ('Error in input file: inconsistency between name and header in file ' + req_in)
    if oday != rday or otime != rtime or ocompany != rcompany:
        raise IOError ('Error in input file: inconsistency between files ' + op_in + ' and ' + req_in)
    else:
        current_time = otime


    '''
    try:
        if otype.lower() == op_in_type or otime == op_in_hour + ':' + op_in_min:
            current_time = otime
    except IOError:
        raise Exception ('Error in input file: inconsistency between name and header in file ' + op_in)
    try:
        if rtype.lower() == req_in_type or rtime == req_in_hour + ':' + req_in_min:
            current_time = otime
    except IOError:
        raise Exception ('Error in input file: inconsistency between name and header in file ' + req_in)
    try:
        if oday == rday or otime == rtime or ocompany == rcompany:
            current_time = otime
    except IOError:
        raise Exception ('Error in input file: inconsistency between files ' + op_in + ' and ' + req_in)'''

    # Assining requests to operators
    assignments, operators = assigning.assign_tasks(operators, requests, current_time)

    # Writing files
    nextTime = add_minutes(current_time, constants.DELTA_TIME)
    header = 'Day:\n'+ oday + 'Time:\n' + nextTime + '\n' + 'Company:\n' + ocompany
    ttHeader='Timetable:'
    opHeader='Operators:'
    time_out = constants.ASSIGNMENTS_FILE_PREFIX + '%02dh%02d' % (get_hours(nextTime), get_minutes(nextTime)) + constants.FILE_EXTENSION
    op_out = constants.OPERATORS_FILE_PREFIX + '%02dh%02d' % (get_hours(nextTime), get_minutes(nextTime)) + constants.FILE_EXTENSION
    write_assignments_file(assignments, header + ttHeader, time_out)
    write_operators_file(operators, header + opHeader, op_out)

#Testing all files
# try:
#     main('examples/example1/operators14h55.txt','examples/example1/requests14h55.txt')
#     main('examples/example2/operators11h05.txt','examples/example2/requests11h05.txt')
#     main('examples/example3/operators16h55.txt','examples/example3/requests16h55.txt')
#     main('examples/example4/operators14h55.txt','examples/example4/requests14h55.txt')
#     main('examples/example5/operators14h55.txt','examples/example5/requests11h05.txt')
# except IOError as e :
#     print (e.args[0])

try:
  if len(sys.argv) == 3:
    main(sys.argv[1],sys.argv[2])
  else:
      print("Usage: python3 "+sys.argv[0]+ " operatorsfile requestsfile")
except IOError as e:
    print(e.args[0])

#https://docs.python.org/2/tutorial/errors.html



#cd "/Users/martim/Desktop/1 semestre FCUL/Fundamentos de Programação/fdp"
#python3 helpchat.py operators14h55.txt requests14h55.txt


# exemplo 1 passou nos testes com uma alteração feita neste ficheiro ',' para ', '
