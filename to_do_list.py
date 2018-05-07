class ToDoList:
	def __init__(self):
		self.saved_tasks = ["test", "testing"]

	def view_tasks(self):
		for item in self.saved_tasks:
			print(item)

	def add_task(self, task_to_add):
		self.saved_tasks.append(task_to_add)

	def remove_task(self, task_to_remove):
		for item in self.saved_tasks:
			if str(item) == str(task_to_remove):
				self.saved_tasks.remove(task_to_remove)
				self.view_tasks()
				return self.saved_tasks
			else:
				print(f"{task_to_remove} was not found on the current to-do list")
				print("Here is the current to-do list: ")
				self.view_tasks()

new_list = ToDoList()

while True:

	print("\nWhat would you like to do?")
	print("Type 'options' to view options")
	user_input = input("Type 'q' to quit: ")

	if user_input.lower()[0] == 'q':
		break

	elif user_input.lower() == "add":
		new_task = str(input("What task would you like to add: "))
		new_list.add_task(new_task)

	elif user_input.lower() == "view":
		print("\n")
		new_list.view_tasks()

	elif user_input.lower() == "remove":
		task_to_remove = input("What task would you like to remove: ")
		new_list.remove_task(task_to_remove)

	elif user_input.lower() == "options":
		print("\n\nadd - add new tasks")
		print("view - view all current saved tasks")
		print("remove - remove task on list")
		print("q - quit the program\n")
		# user_input = input("What would you like to do? ")