# 2017-2018 Fundamentos de Programacao  (MI)
# Grupo 008
# 51705 Catarina Sofia Esteves Leote
# 50701 Martim Duarte da Costa Seco

from assigning import *

def write_operators_file(operators, header, file_name):
    """
    Write a file from a collection of operators.
    Requires: operators, the list of operators
    Requires: header, the first 7 lines of the file
    Requires: file_name, str with the name of a text file to write a list of operators.
    Ensures: the file with the operators is written on the file system
    """
    #print(file_name)
    out_file = open(file_name, 'w')
    for line in header:
        out_file.write(line)
    out_file.write('\n')
    operatorsorded = sorted(operators, key=lambda k: (k['hourFinish'], k['name']))
    for op in operatorsorded:
        domains = '(%s)' %('; '.join(op['domains']))
        values = [op['name'],op['language'],domains,op['hourFinish'],str(op['minutesDone'])]
        line = ', '.join(values)
        out_file.write('%s\n' % line)
    out_file.close()

def write_assignments_file(assignments, header, file_name):
    """
    Write a file from a collection of assignments.
    Requires: assignments, the list of assignments
    Requires: header, the first 7 lines of the file
    Requires: file_name, str with the name of a text file to write a list of assignments.
    Ensures: the file with the assignments is written on the file system
    """
    #print(file_name)
    out_file = open (file_name, 'w')
    for line in header:
        out_file.write(line)
    out_file.write('\n')
    assignmentsorded = sorted(assignments, key=lambda k: (k['time'], k['client']))
    for assign in assignmentsorded:
        values = [assign['time'], assign['client'], assign['operator']]
        line = ', '.join(values)
        out_file.write('%s\n' % line)
    out_file.close()


