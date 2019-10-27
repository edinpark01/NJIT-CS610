class ServiceStation:
    def __init__(self):
        self.remainingServiceTime = 0
        self.servingPassenger = None
    
    def isIdle(self):
        return self.remainingServiceTime == 0
