# coding=utf-8
# 2017-2018 Fundamentos de Programação (MI)
# Grupo 008
# 51705 Catarina Sofia Esteves Leote
# 50701 Martim Duarte da Costa Seco

import assigning
from filesReading import *
from filesWriting import *

def main(op_in, req_in, time_out, op_out): # Martim
    '''
    this is the main funtions, it read the two input files with the operators and requestes,
    produces the output files for the timetable and update yhe operators data
    :param op_in: the filename for the input operators data
    :param req_in: the filename for the input requests data
    :param time_out: the filename for the output timetable data
    :param op_out: the filename for the output operators data
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
    current_time = 0    # TODO falta defenir melhor

    # Assining requests to operators
    assignments = assigning.assign_tasks(operators, requests, current_time)

    # Writing files
    header=''  # TODO ver o que fazer com o header
    write_assignments_file(assignments, header, time_out)
    write_operators_file(operators, header, op_out)

main('operators14h55.txt','requests14h55.txt','timetable15h00.txt','operators15h00.txt')
