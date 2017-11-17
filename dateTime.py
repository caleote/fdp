# coding=utf-8
# 2017-2018 Programação 1 (LTI)
# Grupo 008
# 51705 Catarina Sofia Esteves Leote
# 50701 Martim Duarte da Costa Seco

def get_hours(hm):
    """
    Get the number of hours from a HH:MM time representation.
    Requires: hm str with a time represented as HH:MM.
    Ensures: int with the number of hours.
    """
    return int(hm.split(':')[0])


def get_minutes(hm): #Catarina
    """
    Get the number of minutes from a HH:MM time representation.
    Requires: hm str with a time represented as HH:MM.
    Ensures: int with the number of minutes.
    """
    return int(hm.split(':')[1])


def add_minutes(hm, incr): #Catarina e Martim
    """
    Increment the given time by the given amount of minutes.
    Requires:
    - hm str with a time represented as HH:MM;
    - incr int with the number of minutes.
    Ensures: str with a time represented as HH:MM, the result of incrementing hm by incr minutes.
    """
    hours = get_hours(hm)
    minutes = get_minutes(hm)
    allminutes = hours*60+minutes
    allminutes = allminutes + incr
    return '%02d:%02d' % (int(allminutes/60)%24, allminutes%60)


# para adicionar datas e horas e minutos e segundos
# import date
# import datetime
# datetime.datetime(2100,2,28,23,50) + datetime.timedelta(minutes=11)
# conta com tudo, até anos bissextos