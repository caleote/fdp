# coding=utf-8
# 2017-2018 Fundamentos de Programação (MI)
# Grupo 008
# 51705 Catarina Sofia Esteves Leote
# 50701 Martim Duarte da Costa Seco

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

    for o in operators:
        domains = ('; '.join(o['domains'])) # junta os dominios separados por ;
        domainspar = '(%s)' % domains # coloca () à volta dos domínios
        values = [o['name'],o['language'],domainspar,o['hourFinish'],o['minutesDone']] # faz a lista de atributos.
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
    
    out_file.write('/n')

    for assign in assignments:
        values = [assign['name'], requests['name'], start_time] #erro no segundo name
        line = ','.join(values)
        out_file.write('%s\n' %line)
        
    out_file.close()
