class Person():

    def __init__(self,name):
        self.name = name
        print("Human created")

class Employee(Person):

    def __init__(self, job_title):
        Person.__init__(self)
        self.job_title = job_title
        print("Employee created")

class Customer(Person):

    def __init__(self, email):
        Person.__init__(self)
        self.email = email
        print("Customer created")

johnSmith = Person("John Smith")
janeEmployee = Employee("Jane","nurse")
bobCustomer = Customer("Bob","bob@gmail.ru")