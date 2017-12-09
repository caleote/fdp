# coding=utf-8
# 2017-2018 Fundamentos de Programação (MI)
# Grupo 008
# 51705 Catarina Sofia Esteves Leote
# 50701 Martim Duarte da Costa Seco

import assigning
import constants
from filesReading import *
from filesWriting import *

def main(op_in, req_in): # Martim
    '''
    this is the main funtions, it read the two input files with the operators and requestes,
    produces the output files for the timetable and update yhe operators data
    :param op_in: the filename for the input operators data
    :param req_in: the filename for the input requests data
    :return: nothing
    Requires:
        - op_in file contains the operators data sorted by available time and name
        ......  TODO completar .......
    Ensures:
        - The time_out file contains the assignments for the requests in the req_in file
        - The op_out file contain the operators data updted with the request assignment of file time_out
    '''

    # Reading the files and checking current time

    operators = read_operators_file(op_in)
    requests = read_requests_file(req_in)
    oday, otime, ocompany, otype = readHeader(op_in)
    #TODO testar se o otype = type do nome do ficheiro
    rday, rtime, rcompany, rtype = readHeader(req_in)
    #TODO testar se o rtype = type do nome do ficheiro
    if oday == rday and otime == rtime and ocompany == rcompany : #testa se o cabeçalho é igual - EXCEPTION
        current_time = otime

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
main('operators16h55.txt','requests16h55.txt')
