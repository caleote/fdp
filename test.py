# 2017-2018 Programação 1 (LTI)
# Grupo 008
# 51705 Catarina Sofia Esteves Leote
# 50701 Martim Duarte da Costa Seco

def get_hours(hm):
    """
    Get the number of hours from a HH:MM time representation.
    @requires: hm str with a time represented as HH:MM.
    @ensures: int with the number of hours.
    """
    return int(hm.split(':')[0])


def get_minutes(hm): #Catarina
    """
    Get the number of minutes from a HH:MM time representation.
    @requires: hm str with a time represented as HH:MM.
    ´@ensures: int with the number of minutes.
    """
    return int(hm.split(':')[1])


def add_minutes(hm, incr): #Catarina
    """
    Increment the given time by the given amount of minutes.
    @requires:
    - hm str with a time represented as HH:MM;
    - incr int with the number of minutes.
    @ensures: str with a time represented as HH:MM, the result of incrementing hm by incr minutes.
    """
    hours = get_hours(hm)
    minutes = get_minutes(hm)
    incrementation = minutes + incr
    if incrementation > 60 :
        if incrementation % 60 == 0:
            incrhour = incrementation // 60
            return hours + incrhour
        #else:



                
        #finalincr = incr % 60
        
print (add_minutes('14:10', 120))
