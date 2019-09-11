# Python - Problem Pack I
import pprint as pp
import my_functions as func
# 1. Calculate and print the average of the numbers: 583, 42, 192. Round to 3 decimal placs.
func.questionBlock(1)

averageSet = [583, 42, 192]
avg = round(func.average(averageSet), 3)
print("The average of list: %s is %d" %  (''.join(str(averageSet)), avg))

# 2.You need to purchase a new pair of sneakers. They cost $128 before tax. What is the totalcost if the local sales tax is 8.675%?
func.questionBlock(2)

beforeTax = 128
afterTax = func.addTax(beforeTax)
print("Sneakers before tax: $ %.2f\nSneakers after tax: $ %.2f"%(beforeTax, afterTax))

# 3. It takes 27338 minutes to clean the king's mansion. How many days, hours, and minutesdoes it take to complete this task.
func.questionBlock(3)

amtMins = 27338
amtDays = func.minsToDays(amtMins)
amtHrs = func.minsToHr(amtMins)
print("%d minutes is %.2f days or %d total days" % (amtMins, amtDays, round(amtDays)))
print("%d minutes is %.2f hrs or %d total hrs" % (amtMins, amtHrs, round(amtHrs)))


# 4. In Toronto, it was 18° C this morning. What is the temperature in Fahrenheit (nearesttenth of a degree).
func.questionBlock(4)

celsius = 18
fahrenheit = func.celsiusToFahrenheit(celsius)
print("%.1f degrees C is %.1f degrees F" % (celsius, fahrenheit))


# 5.Create a list of apple names- use the variable 'apples'. Start with the typoes: 'rome','delicious', 'empire', and 'fuji'.
#   a.Add 'gala' and 'macintosh' to the List
#    b.Insert 'honeycrisp' in the 2nd position
#    c.Add the integers 43, 54, 18 to the list
#    d.Create a new list - nums  with the values 35.4, 99, and 'golden'
#    e.COmbine the apples and nums list → into a single list named - fnnl - (for final list)
func.questionBlock(5)

apples = ['rome','delicious', 'empire','fuji']
# ['rome','delicious', 'empire','fuji']
apples.extend(['gala', 'macintosh'])
# ['rome', 'delicious', 'empire', 'fuji', 'gala', 'macintosh']
apples.insert(1, 'honeycrisp')
# ['rome', 'honeycrisp', 'delicious', 'empire', 'fuji', 'gala', 'macintosh']
apples.extend([43,54,18])
# ['rome', 'honeycrisp', 'delicious', 'empire', 'fuji', 'gala', 'macintosh', 43 ,54 ,18]
nums = [35.4, 99, 'golden']
apples.extend(nums)
print("Final list: ", apples)

# 6.Prompt a customer for 5 integers. Once they are entered, print the 5 numbers (on a singleline).
func.questionBlock(6)
intList = [0,0,0,0,0]
for i in range(1, 6):
    try:
        intList.append(int(input("Enter integer %d: " % i)))
    except:
        print("Input must be an integer..")
print("Integer list: ", intList)
print('Sum of all elements: %d | Average of elements %.2f'%  (sum(intList), func.average(intList)))

# 7.You invest $342 into a savings account, which returns 4.3%, compounded annually. Whatis the balance (rounded to the nearest cent) after 7 years?
#   a.** What would the balance be if interest was compounded quarterly??
func.questionBlock(7)
    
amtInvested = 342
interest = .043
years = 7


annual_finalBalance = func.compoundInterestAnnual(amtInvested, interest, years)
quarterly_finalBalance = func.compoundInterestQuarterly(amtInvested, interest, years)
print("With an inital balance amount of %.2f, annual interest of %.1f%% after %d year(s) is: %.2f" % (amtInvested, interest*100, years, annual_finalBalance))
print("With an inital balance amount of %.2f, quarterly interest of %.1f%% after %d year(s) is: %.2f" % (amtInvested, interest*100, years, quarterly_finalBalance))

# 8. Find the average velocity of the Voyager I spacecraft, as of this class session. (Go online,Nasa site - Voyager page - get its distance from Earth, 
# and elapsed mission time.) (pleaseuse kilometers per hour - rounded to the nearest hundredth).
func.questionBlock(8)

# displacement in meters
displacement = 21972730312 * 1000
seconds = func.secondsSinceVoyagerLaunch()
print("With Voyager I %d meters away at time %d (seconds):\n The voyager has an average velocity of %.3f (m/s)" % (displacement, seconds, func.averageVelocity(displacement, seconds)))

# 9. You have a circular pool; its surface area is 720 square feet. If you wish to install a fencearound the pool, how much fence do you need to buy?  to the 
# nearest foot). (You have tobe sure you enclose the pool area! Round up to the nearest foot.)
func.questionBlock(9)

#square feet
surface_area = 720
circumference = func.getCircumference(func.getRadius(surface_area))
print("If you were to build a fence around a pool with a surface area of %d you would need %d feet of fencing" % (surface_area, round(circumference)))

# 10. In President Lincoln's Gettysburg Address, how many times is the letter 'e' used? Howmany vowels in total are used? (Challenge: how many a, e, i, o, and u's were used?)
func.questionBlock(10)

gettysburg = open('gettysburg.txt', "r")
countE = 0
vowels = ['a','e','i','o','u']
countVowels = 0
for line in gettysburg:
    for char in line:
        if(char == "e"):
            countE += 1
        if char in vowels:
            countVowels += 1

print(f"There are {countE} Es in the gettyburg address")
print(f"There are {countVowels} vowels in the gettyburg address")