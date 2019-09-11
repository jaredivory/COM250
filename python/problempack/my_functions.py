import datetime, math

def questionBlock(num):
    "Creates a block to seperate the questions"
    print("########################################################## %d ##########################################################" % num)

def average(lst):
    return sum(lst) / len(lst)

def addTax(inital_price, salesTax=.08675):
    return ( inital_price * salesTax ) + inital_price

def minsToDays(mins):
    return (mins / (60 * 24))

def minsToHr(mins):
    return (mins / 60)

def celsiusToFahrenheit(celsius):
    return celsius * 9/5 + 32

def compoundInterestAnnual(amtInvested, interest, years):
    "Takes principal and interest then computes amount after years"
    amtInvested = (amtInvested * interest) + amtInvested
    years -= 1
    if (years == 0):
        return amtInvested
    return compoundInterestAnnual(amtInvested, interest, years)

def compoundInterestQuarterly(amtInvested, interest, years):
    for i in range(1, 5):
        amtInvested = (amtInvested * interest) + amtInvested
    years -= 1
    if(years == 0):
        return amtInvested
    return compoundInterestQuarterly(amtInvested, interest, years)

def hhmmssToSeconds(hhmmss):
    "Returns seconds from time format HH:MM:SS"
    hrs,mins,secs = hhmmss.split(":")

    hrs = int(hrs)
    mins = int(mins)
    secs = int(secs)

    secs += hrs*3600 + mins*60

    return secs

def secondsSinceVoyagerLaunch():
    return datetime.datetime.now().timestamp() - datetime.datetime(1977,9,5,12,56).timestamp()

def averageVelocity(displacement, elapsedTime):
    "Takes displacement (meters) and elapsed time (seconds) and returns velocity (m/s)"
    return displacement / elapsedTime

def getRadius(squareFeet):
    return squareFeet / math.pi
def getCircumference(radius):
    return math.pi * 2 * radius