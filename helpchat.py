# coding=utf-8
# 2017-2018 Programação 1 (LTI)
# Grupo 008
# 51705 Catarina Sofia Esteves Leote
# 50701 Martim Duarte da Costa Seco

from constants import *

import assigning
from filesReading import *
import filesWriting


def testReading():
    """
    This function is for testing the read functions
    """
    print("Reading requests")
    requests = read_requests_file(REQ_FILENAME)
    for r in requests:
        print(r)

    print()

    print("Reading operators")
    operators = read_operators_file(OP_FILENAME)
    for o in operators:
        print(o)

testReading()