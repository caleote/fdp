# coding=utf-8
# 2017-2018 Fundamentos de Programação (MI)
# Grupo 008
# 51705 Catarina Sofia Esteves Leote
# 50701 Martim Duarte da Costa Seco

import constants

def read_operators_file(file_name):  # Martim
    """
    Read a file with operators into a collection.
    Requires: file_name, str with the name of a text file with a list of operators.
    Ensures: list, with the operators in the file; each operator is a tuple with the
    various elements, in the order provided in the file.
    """
    in_file = open(file_name, 'r')
    for i in range(constants.HEADER_TOTAL_LINES):  # read some lines to skip the header
        in_file.readline()

    operators = []
    for line in in_file:
        name, language, domains, hourFinish, minutesDone = line.strip().split(', ')
        domains = domains[1:-1].split('; ')
        operators.append((name, language, domains, hourFinish, minutesDone))
    in_file.close()

    return operators

def read_requests_file(file_name):
    """
    Read a file with requests into a collection.
    Requires: file_name, str with the name of a text file with a list of requests.
    Ensures: list, with the requests in the file; each request is a tuple with the
    various element concerning that request, in the order provided in the file.
    """
    in_file = open(file_name, 'r')
    for i in range(constants.HEADER_TOTAL_LINES):  # read some lines to skip the header
        in_file.readline()

    requests = []
    for line in in_file:
        name, language, domain, service, duration = line.strip().split(', ')
        duration = int(duration)
        requests.append((name, language, domain, service, duration))
    in_file.close()

    return requests