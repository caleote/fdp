# 2017-2018 Fundamentos de Programacao  (MI)
# Grupo 008
# 51705 Catarina Sofia Esteves Leote
# 50701 Martim Duarte da Costa Seco

def get_hours(hm):
    """
    Get the number of hours from a HH:MM time representation.
    Requires:
    - hm str with a time represented as HH:MM.
    Ensures: int with the number of hours.
    """
    return int(hm.split(':')[0])

def get_minutes(hm):
    """
    Get the number of minutes from a HH:MM time representation.
    Requires:
    - hm str with a time represented as HH:MM.
    Ensures: int with the number of minutes.
    """
    return int(hm.split(':')[1])


def add_minutes(hm, incr):
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

def max_time(time1, time2):
    """
    Returns the highest value between t1 and t2.
    Requires:
    - t1 str with a time represented as HH:MM
    - t2 str with a time represented as HH:MM
    Ensures: str with a time represented as HH:MM, the highest value between t1 and t2.
    """
    hours1 = get_hours(time1)
    minutes1 = get_minutes(time1)
    hours2 = get_hours(time2)
    minutes2 = get_minutes(time2)
    if hours1 != hours2 :
        if hours1 > hours2:
            max = '%02d:%02d' % (hours1, minutes1)
        else:
            max = '%02d:%02d' % (hours2, minutes2)
    else:
        if minutes1 > minutes2:
            max = '%02d:%02d' % (hours1, minutes1)
        else:
            max = '%02d:%02d' % (hours2, minutes2)
    return max



