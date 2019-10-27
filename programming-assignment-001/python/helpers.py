# Author: Braulio Tonaco
# Date: 09/24/2019

import json, random

def randomInteger(N: int) -> int:
    """ Returns a Random number between 1 and N """
    return random.randint(1, N)

def randomInterval(A, B: int) -> int:
    """ Returns a Random number between A and B inclusive """
    return random.randint(A, B) if A <= B else -1

def randomEvent(N: int) -> bool:
    """ Returns TRUE on average once every N calls """
    return random.random() <= 1.0 / N

def parseSimulationInput():
    with open('inputs.json', 'r') as f:
        return json.load(f)

def newArrival(checkInAlotedTime: str, frequency, time: int) -> bool:
    """ Returns True on average once every frequency call and 
    time is within the simulation duration """

    return randomEvent(frequency) and time < checkInAlotedTime
