class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.num_unique_people_greeted = 0
        self.unique_greeting = []

    def __repr__(self):
    	return ('(%s, %s, %s)' % (self.name, self.email, self.phone))

    def greet(self, other_person):
        print ('Hello %s, I am %s!' % (other_person.name, self.name))
        self.greeting_count += 1
        if other_person.name not in self.unique_greeting:
        	self.unique_greeting.append(str(other_person.name))
        	self.num_unique_people_greeted += 1

    def print_contact_info(self):
    	print(f"\n{self.name}'s email: {self.email}")
    	print(f"{self.name}'s phone number: {self.phone}\n")

    def add_friend(self, friend):
    	self.friends.append(friend)

    def num_friends(self):
    	print("You have " + str(len(self.friends)) + " friend(s) in your friends list")

    def greeting_count(self):
    	return self.greeting_count
    
    def num_unique_people_greeted(self):
    	return self.num_unique_people_greeted




sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

jordan.add_friend(sonny)
print(jordan.friends)
jordan.num_friends()

sonny.greet(jordan)
jordan.greet(sonny)

sonny.print_contact_info()
jordan.print_contact_info()

print(sonny.email + " " + sonny.phone)

print(jordan.email + " " + jordan.phone)


print(sonny.greeting_count)
sonny.greet(jordan)
print(sonny.greeting_count)


class Vehicle:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
	def print_info(self):
		print(self.make, self.model, self.year)
car = Vehicle('Honda', 'Accord', 2001)

car.print_info()