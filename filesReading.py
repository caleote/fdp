# coding=utf-8
# 2017-2018 Programação 1 (LTI) #nao achas q aqui é Fundamentos de Programação (MI) em vez disto?
# Grupo 008
# 51705 Catarina Sofia Esteves Leote
# 50701 Martim Duarte da Costa Seco

import constants

def read_operators_file(file_name): # Martim
    """
    Read a file with operators into a collection.
    Requires: file_name, str with the name of a text file with a list of operators.
    Ensures: list, with the requests in the file; each request is a tuple with the various element concerning that request, in the order provided in the file.
    """
    in_file = open(file_name, encoding='iso-8859-1')
    for i in range(constants.HEADER_TOTAL_LINES):  # read some lines to skip the header
        in_file.readline()

    operators = []
    for line in in_file:
        name, language, domains, hourFinish, minutesDone = line.strip().split(', ')
        domains = domains[1:-1].split('; ')
        # É isto que queria catarina ? É uma estrutura de dados, um dicionario
        operators.append(
        {'name':name,
        'language':language,
        'domains':domains,
        'hourFinish':hourFinish,
        'minutesDone':minutesDone
         })
    in_file.close()
    return operators


def read_requests_file(file_name):
    """
    Read a file with requests into a collection.
    Requires: file_name, str with the name of a text file with a list of requests.
    Ensures: list, with the requests in the file; each request is a tuple with the various element
    concerning that request, in the order provided in the file.
    """
    in_file = open(file_name, encoding='iso-8859-1')
    for i in range(constants.HEADER_TOTAL_LINES):  # read some lines to skip the header
        in_file.readline()

    requests = []
    for line in in_file:
        name, language, domain, service, duration = line.strip().split(', ')
        duration = int(duration)
        requests.append(
        {'name':name,
         'language':language,
         'domain':domain,
         'service':service,
         'duration':duration
         })
    in_file.close()
    return requests
