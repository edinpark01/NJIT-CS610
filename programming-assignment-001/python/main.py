# Author: Braulio Tonaco
# Date: 09/21/2019

from serviceStation import ServiceStation
from passenger import Passenger
from myqueue import MyQueue
from helpers import *

import time, uuid, logging

TESTCASES = {
    "simulation001": {
        "checkInDuration": 160,
        "coach": {
            "arrivalRate": 6,
            "serviceRate": 5
        },
        "firstClass": {
            "arrivalRate": 4,
            "serviceRate": 6
        }
    },
    "simulation002": {
        "checkInDuration": 1400,
        "coach": {
            "arrivalRate": 7,
            "serviceRate": 16
        },
        "firstClass": {
            "arrivalRate": 10,
            "serviceRate": 18
        }
    },
    "simulation003": {
        "checkInDuration": 4000,
        "coach": {
            "arrivalRate": 2,
            "serviceRate": 16
        },
        "firstClass": {
            "arrivalRate": 2,
            "serviceRate": 5
        }
    },
    "simulation004": {
        "checkInDuration": 60000,
        "coach": {
            "arrivalRate": 5,
            "serviceRate": 5
        },
        "firstClass": {
            "arrivalRate": 5,
            "serviceRate": 5
        }
    }
}

def ongoingSimulation(currentDuration, checkInAlotedTime):
    return not ( 
            coachSvcStation001.isIdle()
        and coachSvcStation002.isIdle() 
        and coachSvcStation003.isIdle()
        and firstClassSvcStation001.isIdle()
        and firstClassSvcStation002.isIdle()
        and firstClassQueue.isEmpty()
        and coachQueue.isEmpty() 
    ) or currentDuration < checkInAlotedTime 

if __name__ == "__main__":
    s = TESTCASES

    while True:
        print("Which simulation to RUN? 1, 2, 3, OR 4  -> ", end="")
        option = input()
        if option == "1" or option == "2" or option == "3" or option == "4":
            break
        print("Wrong INPUT, try again...")

    # Simulation
    SIMULATION = 'simulation00' + option
    checkInDuration = s[SIMULATION]['checkInDuration']

    # Average Rates
    coachAvgSvcRate     = s[SIMULATION]['coach']['serviceRate']
    coachAvgArrivalRate = s[SIMULATION]['coach']['arrivalRate']
    fcAvgSvcRate        = s[SIMULATION]['firstClass']['serviceRate']
    fcAvgArrivalRate    = s[SIMULATION]['firstClass']['arrivalRate']
    
    # Start Queues
    coachQueue      = MyQueue()
    firstClassQueue = MyQueue()

    # Start Service Stations
    coachSvcStation001      = ServiceStation()
    coachSvcStation002      = ServiceStation()
    coachSvcStation003      = ServiceStation()
    firstClassSvcStation001 = ServiceStation()
    firstClassSvcStation002 = ServiceStation()

    # Stats MISC
    coachQueueSTATS = { 'duration': 0.0, 'maxSize': 0, 'maxWait': 0, 'nPass': 0 }
    firstQueueSTATS = { 'duration': 0.0, 'maxSize': 0, 'maxWait': 0, 'nPass': 0 }
    
    # Stats Service Stations
    busyStation = {
        'coach':{'001':0.0, '002':0.0, '003':0.0, }, 
        'first':{'001':0.0, '002':0.0,} 
    }

    duration = 0
    while ongoingSimulation(duration, checkInDuration):
        # Handle New Arrivals 
        # First Class
        if newArrival(checkInDuration, fcAvgArrivalRate, duration):
            psgr = Passenger('First', duration, fcAvgSvcRate)
            firstClassQueue.enqueue(psgr)
            firstQueueSTATS['nPass'] += 1  # Increments total number of passengers in queue
            # Checks Queue Max size
            if firstClassQueue.size() > firstQueueSTATS['maxSize']:
                firstQueueSTATS['maxSize'] = firstClassQueue.size()
        # Coach 
        if newArrival(checkInDuration, coachAvgArrivalRate, duration):
            psgr = Passenger('Coach', duration, coachAvgSvcRate)
            coachQueue.enqueue(psgr)
            coachQueueSTATS['nPass'] += 1  # Increments total number of passengers in queue
            # Checks Queue Max size
            if coachQueue.size() > coachQueueSTATS['maxSize']:
                coachQueueSTATS['maxSize'] = coachQueue.size()

        # Handle BUSY Service Stations
        # FC01
        if firstClassSvcStation001.remainingServiceTime > 1:
            firstClassSvcStation001.remainingServiceTime -= 1
            busyStation['first']['001'] += 1
        elif firstClassSvcStation001.remainingServiceTime == 1:
            firstClassSvcStation001.remainingServiceTime = 0
            p = firstClassSvcStation001.servingPassenger
            busyStation['first']['001'] += 1
        # FC02
        if firstClassSvcStation002.remainingServiceTime > 1:
            firstClassSvcStation002.remainingServiceTime -= 1
            busyStation['first']['002'] += 1
        elif firstClassSvcStation002.remainingServiceTime == 1:
            firstClassSvcStation002.remainingServiceTime = 0
            p = firstClassSvcStation002.servingPassenger
            busyStation['first']['002'] += 1
        # CO01
        if coachSvcStation001.remainingServiceTime > 1:
            coachSvcStation001.remainingServiceTime -= 1
            busyStation['coach']['001'] += 1
        elif coachSvcStation001.remainingServiceTime == 1:
            coachSvcStation001.remainingServiceTime = 0
            p = coachSvcStation001.servingPassenger
            busyStation['coach']['001'] += 1
        # CO02
        if coachSvcStation002.remainingServiceTime > 1:
            coachSvcStation002.remainingServiceTime -= 1
            busyStation['coach']['002'] += 1
        elif coachSvcStation002.remainingServiceTime == 1:
            coachSvcStation002.remainingServiceTime = 0
            p = coachSvcStation002.servingPassenger
            busyStation['coach']['002'] += 1
        # CO03
        if coachSvcStation003.remainingServiceTime > 1:
            coachSvcStation003.remainingServiceTime -= 1
            busyStation['coach']['003'] += 1
        elif coachSvcStation003.remainingServiceTime == 1:
            coachSvcStation003.remainingServiceTime = 0
            p = coachSvcStation003.servingPassenger
            busyStation['coach']['003'] += 1

        # Handle IDLE Service Stations
        # FC01
        if firstClassSvcStation001.remainingServiceTime == 0:
            if not firstClassQueue.isEmpty():
                fcp = firstClassQueue.dequeue()
                firstClassSvcStation001.remainingServiceTime = fcp.service
                firstClassSvcStation001.servingPassenger = fcp
                
                waitTime = duration - fcp.arrival
                if waitTime > firstQueueSTATS['duration']:
                    firstQueueSTATS['maxWait'] = waitTime 
                firstQueueSTATS['duration'] += waitTime
            elif not coachQueue.isEmpty():
                cp = coachQueue.dequeue()
                firstClassSvcStation001.remainingServiceTime = cp.service
                firstClassSvcStation001.servingPassenger = cp
                
                waitTime = duration - cp.arrival
                if waitTime > coachQueueSTATS['maxWait']:
                    coachQueueSTATS['maxWait'] = waitTime 
                coachQueueSTATS['duration'] += waitTime

        # FC02
        if firstClassSvcStation002.remainingServiceTime == 0:
            if not firstClassQueue.isEmpty():
                fcp = firstClassQueue.dequeue()
                firstClassSvcStation002.remainingServiceTime = fcp.service
                firstClassSvcStation002.servingPassenger = fcp
            elif not coachQueue.isEmpty():
                cp = coachQueue.dequeue()
                firstClassSvcStation001.remainingServiceTime = cp.service
                firstClassSvcStation001.servingPassenger = cp
        # CO01
        if coachSvcStation001.remainingServiceTime == 0:
            if not coachQueue.isEmpty():
                cp = coachQueue.dequeue()
                coachSvcStation001.remainingServiceTime = cp.service
                coachSvcStation001.servingPassenger = cp
        # CO02
        if coachSvcStation002.remainingServiceTime == 0:
            if not coachQueue.isEmpty():
                cp = coachQueue.dequeue()
                coachSvcStation002.remainingServiceTime = cp.service
                coachSvcStation002.servingPassenger = cp
        # CO03
        if coachSvcStation003.remainingServiceTime == 0:
            if not coachQueue.isEmpty():
                cp = coachQueue.dequeue()
                coachSvcStation003.remainingServiceTime = cp.service
                coachSvcStation003.servingPassenger = cp

        duration += 1

    print("\nINPUT:")
    print("Sumulation:\t\t{}".format(SIMULATION))
    print("\nCheck-in:\t\t{} minutes".format(checkInDuration))
    print("==> First Class:\tArrival: {}\tAverage Svc: {}".format(fcAvgArrivalRate, fcAvgSvcRate))
    print("==> Coach Class:\tArrival: {}\tAverage Svc: {}".format(coachAvgArrivalRate, coachAvgSvcRate))

    print("\nOUTPUT:")
    print("Simulation Duration::\t{} minutes".format(duration))
    print("\nQueues:")
    print("==> First Class:\tMax Size: {}\t Avg Wait: {}        Max Wait: {}".format(
        firstQueueSTATS['maxSize'], 
        round(firstQueueSTATS['duration'] / firstQueueSTATS['nPass'], 2), 
        firstQueueSTATS['maxWait']))
    print("==> Coach Class:\tMax Size: {}\t Avg Wait: {}         Max Wait: {}".format(
        coachQueueSTATS['maxSize'], 
        round(coachQueueSTATS['duration'] / coachQueueSTATS['nPass'], 2), 
        coachQueueSTATS['maxWait']))

    print("\nService Station:")
    print("==> First Class:")
    print("=====> Station 01:\t{}% busy".format(round(busyStation['first']['001'] / duration * 100, 2)))
    print("=====> Station 02:\t{}% busy".format(round(busyStation['first']['002'] / duration * 100, 2)))
    print("==> Coach Class:")
    print("=====> Station 01:\t{}% busy".format(round(busyStation['coach']['001'] / duration * 100, 2)))
    print("=====> Station 02:\t{}% busy".format(round(busyStation['coach']['002'] / duration * 100, 2)))
    print("=====> Station 03:\t{}% busy".format(round(busyStation['coach']['002'] / duration * 100, 2)))

