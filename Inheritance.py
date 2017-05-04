# Learning-Python- 
"""inheritance between Parent and Child 

class Parent():
    def __init__(self, last_name, eye_color):
        print ("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

class Child(Parent):
# this means child will use everything in Parent
    def __init__(self, last_name, eye_color, number_of_toys):
        print ("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys


steve_jobs = Child("Jobs", "Blue", 5)
print (steve_jobs.last_name)
print (steve_jobs.number_of_toys)
