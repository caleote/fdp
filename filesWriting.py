# coding=utf-8
# 2017-2018 Fundamentos de Programação (MI)
# Grupo 008
# 51705 Catarina Sofia Esteves Leote
# 50701 Martim Duarte da Costa Seco

from assigning import *

def write_operators_file(operators, header, file_name): # Martim
    """
    Write a file from a collection of operators.
    Requires: operators, the list of operators
    Requires: header, the first 7 lines of the file
    Requires: file_name, str with the name of a text file to write a list of operators.
    Ensures: the file is written on the file system
    """
    out_file = open(file_name, 'w')
    for line in header:
        out_file.write(line) # writes one line at a time
    out_file.write('\n')
    operatorsorded = sorted(operators, key=lambda k: k['hourFinish']) #aqui não sei ordenar de acordo com a hora e com a ordem alfabética, só consigo 1 de cada vez
    for op in operatorsorded:
        domains = '(%s)' %('; '.join(op['domains'])) #ao pormos logo aqui o (%s) estamos a juntar os domínios dentro de parênteses separados por ;
        #domainspar = '(%s)' % domains # e depois podemos tirar esta parte
        values = [op['name'],op['language'],domains,op['hourFinish'],str(op['minutesDone'])] # os minutesDone têm de ser string senão ele não consegue fazer join
        line = ', '.join(values) # junta os atributos separados por , numa só linha
        out_file.write('%s\n' % line) # escreve a linha no ficheiro com ENTER no fim
    out_file.close()

def write_assignments_file(assignments, header, file_name): # Catarina
    """
    Write a file from a collection of assignments.
    Requires: assignments, the list of assignments
    Requires: header, the first 7 lines of the file # porquê as 7 primeiras linhas?
    Requires: file_name, str with the name of a text file to write a list of assignments.
    Ensures: the file is written on the file system
    """
    out_file = open (file_name, 'w')
    for line in header:
        out_file.write(line)
    out_file.write('\n')
    assignmentsorded = sorted(assignments, key=lambda k: k['time'])
    for assign in assignmentsorded:
        values = [assign['time'], assign['client'], assign['operator']]
        line = ','.join(values)
        out_file.write('%s\n' % line)


        
    out_file.close()

header1 = ['Operators:']
header2 = ['Assignments:']
ass, operatorsdic = assign_tasks('operators16h55.txt', 'requests16h55.txt', '17:00')
write_operators_file(operatorsdic, header1, 'operators17h00.txt')
write_assignments_file(ass, header2, 'timetable17h00.txt')
