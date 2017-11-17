# coding=utf-8
# 2017-2018 Programação 1 (LTI)
# Grupo 008
# 51705 Catarina Sofia Esteves Leote
# 50701 Martim Duarte da Costa Seco

def write_operators_file(operators, header, file_name): # Martim
    """
    Write a file from a collection of operatiors.
    Requires: operators, the list of operators
    Requires: header, the first 7 lines of the file
    Requires: file_name, str with the name of a text file to write a list of operators.
    Ensures: the file is written on the file system
    """
    out_file = open(file_name, 'w', encoding='iso-8859-1')
    for line in header:
        out_file.write(line) # writes one line at a time

    out_file.write('\n')

    for o in operators:
        domains = ('; '.join(o['domains']))
        domainspar = '(%s)' % domains
        values = [o['name'],o['language'],domainspar,o['hourFinish'],o['minutesDone']]
        line = ', '.join(values)
        out_file.write('%s\n' % line)

    out_file.close()

def write_assignments_file(assignments, header, file_name):
	pass
