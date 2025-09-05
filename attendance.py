"""
TASK: Create an AttendanceRegister class.

Requirements:
1. The class should allow marking a student as present or absent.
2. Store attendance records in a dictionary where the student's name is the key.
3. Provide a method to check if a student was present or absent.
4. Provide a method to display the full register.

Example Usage:
    register = AttendanceRegister()
    register.mark_present("John")
    register.mark_absent("Mary")
    print(register.get_status("John"))   # "Present"
    print(register.show_register())      # {"John": "Present", "Mary": "Absent"}
"""
class AttendanceRegister: # class variable

	def __init__(self):
		self.attendance = {} # empty dictionary to store student record
	
	def mark_present(self, name):
		self.attendance[name] = "present"

	def mark_absent(self, name):
		self.attendance[name] = "absent"

	def register(self):
		return self.attendance
	def get_status(self, name):
		return self.attendance.get(name)
	def show_register(self):
		return self.attendance

register = AttendanceRegister()
register.mark_present("Moses")
register.mark_absent("Grace")
print(register.get_status("Moses")) # output 'present'
print(register.show_register())
