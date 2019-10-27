import uuid, random

class Passenger:
    """ A Passenger to embark on a flight.

    Attributes:
        type: Which class type the passenger is, coach OR first class .
        arrival: Actual Time in which passenger arrived at queue.
        service: Time the passenger will require for service (this value is randomly generated). 
        ID: Passenger's Unique Identifier.
    """
    def __init__(self, kind: str, current, svc: int):
        self.type    = kind         
        self.arrival = current
        self.service = self.__randomAverage(svc)
        self.ID      = uuid.uuid1()
    
    def __randomAverage(self, A: int) -> int:
        """ Returns a random number, so that average is A """
        return random.randint(1, 2 * A - 1)