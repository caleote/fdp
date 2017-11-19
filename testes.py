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
        print(o)

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


def testAssigning():
    operators = [
        {'name': 'Ricardo Tavares', 'language': 'portuguese', 'domains': ['mobiles', 'printers'], 'hourFinish': '14:15',
         'minutesDone': '42'},
        {'name': 'Carl Thompson', 'language': 'english', 'domains': ['laptops'], 'hourFinish': '14:17',
         'minutesDone': '54'},
        {'name': 'NÃºria Castro', 'language': 'spanish', 'domains': ['cameras', 'hifi'], 'hourFinish': '14:24',
         'minutesDone': '37'},
        {'name': 'Giovanni Olivetti', 'language': 'italian', 'domains': ['laptops', 'bimby', 'hifi'],
         'hourFinish': '14:52', 'minutesDone': '21'},
        {'name': 'Georg Muller', 'language': 'deutsch', 'domains': ['cameras'], 'hourFinish': '15:05',
         'minutesDone': '31'}
    ]
    requests = [
        {'name': 'Henry Miller', 'language': 'english', 'domain': 'laptops', 'service': 'premium', 'duration': 3},
        {'name': 'FranÃ§ois Greenwich', 'language': 'spanish', 'domain': 'cameras', 'service': 'premium', 'duration': 6},
        {'name': 'Ricardo Carvalho', 'language': 'portuguese', 'domain': 'refrigerators', 'service': 'premium',
         'duration': 2}
    ]
    assignments = assigning.assign_tasks(operators,requests,"14:55")
    print(assignments)


#testReadingWriting()
#testDateTime()
testAssigning()
