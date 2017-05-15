print "Hello World"

print "Hens," , 25 + 30 / 6
print "Rooster", 100 - 25 * 3 % 4
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
print 3 + 5 > 5 + 2


cars = 100
space_in_a_car = 4.0
drivers = 304
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

x = "there are %d types of people" %10
binary = "binary"
do_not = "don't"
y ="Those who know %s and those who %s " % (binary, do_not)

print x, y

print "I said: %r" %x
print "I also said '%s' " %y

hilarious = False
joke_evaluation = "Isn't that joke so funny? ! %r"

print joke_evaluation % hilarious

w = "Vinay"
e = " Jain"

print w + e,
print w + e

formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)
print formatter %("one","two","three","four")

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print days
print months

