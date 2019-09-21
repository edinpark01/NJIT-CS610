# Module 03 Assignment - Programming Assignment I

Implement a queue data type. Use it to simulate the evolution of waiting queues, by invoking several instances of the queue data type.

## Instructions

To fix your ideas, assume that we are simulating a check-in operation for an airline company at an airport terminal.

We have two classes of service (each class of service has a dedicated queue):

1. First class
   1. Two (2) Service Stations
      1. NOTE: if a first class service station is free and the queue for coach is not empty then the service station serves passengers from the coach queue.
2. Coach class
   1. Tree (3) Service Stations
      1. If First class service station is free and coach queue is not empty, include first class service station.

### Passenger

Passenger object will have the following attributes:

* **Type:** First Class OR Coach Class
* **Arrival Time:** Random, but subject to average arrival times.
  * ***For Example:***
    * First class passenger every five (5) minutes.
    * Coach passenger every two (2) minutes on average. 
    * Actual arrival times are random.
* **Service Time:** Random, but subject to average service times.
  * ***For Example:***
    * First class passengers usually require six (6) minutes of service on average.
    * Coach passengers get on average two (2) minutes of service on average.
    * Actual times vary.
    * All times are measured in minutes.

### The simulation

* **Initialization:**
  * Empty waiting queues
  * Free service stations.
* **Queue INPUT Halt:**
  * At some point in time (usually 40 minutes prior to departure time) the company closes the queues (no more passengers are admitted).
* **Termination:**
  * Simulation ends when all the queues are empty and all the service stations are free.

## Inputs to the simulation

* `Duration of the check in` (make it arbitrarily long, do not worry about it being or not being realistic).
* `Coach average arrival rate`
* `Coach average service rate`
* `First class average arrival rate`
* `First class average service rate`

Outputs of the Simulation:

* `Duration of the simulation` (which may be longer than the input parameter, as when checkin closes, there may be passengers in the waiting queues and service stations).
* `Maximum length of the queue` for each queue.
* `Average waiting time` for each queue
* `Maximum waiting time` for each queue.
* `Rate of occupancy` of each service station (percentage of time each station was busy).
* **Optional:** Show/output the real-time evolution of the queues during the run-time simulation.
