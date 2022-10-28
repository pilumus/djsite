# def adder(x,y,z):
#     print("sum:", x+y+z)

# adder(10,12,13,14,15) #TypeError

def adder(*num):
    sum = 0

    for n in num:
        sum = sum + n

    print('Sum:', sum)

# adder(3,5)
# adder(4,5,6,7)
# adder(1,2,3,4,5,6)

def intro(**data):
    print('Data type of argument:', type(data))
    print(data.items())

    for key, value in data.items():

        print("{} is {}".format(key, value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)
