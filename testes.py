# coding=utf-8
# 2017-2018 Programação 1 (LTI)
# Grupo 008
# 51705 Catarina Sofia Esteves Leote
# 50701 Martim Duarte da Costa Seco

from constants import *

import assigning
from dateTime import add_minutes
from filesReading import *
from filesWriting import *


def testReadingWriting(): #Martim
    """
    This function is for testing the read functions
    """
    print('Reading requests')
    requests = read_requests_file(REQ_FILENAME)
    for r in requests:
        print(r)

    print()

    print('Reading operators')
    operators = read_operators_file(OP_FILENAME)
    for o in operators:
        print(o['name'])

    ## fazer alguma coisa

    header = ["Ola","Ola"] # Tem que ser o header do ficheiro
    write_operators_file(operators, header,OUT_OP_FILENAME)


def testDateTime():  # Martim
    print()
    print('Adding minutes')
    print(add_minutes('14:10', 10))
    print(add_minutes('14:10', 55))
    print(add_minutes('14:10', 90))
    print(add_minutes('14:10', 24 * 60 - 10))


testReadingWriting()
testDateTime()