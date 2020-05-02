'''
Creating a Class is essentially building your own Object.
What is an Object? It's anything, very literally.
Python is an interpreted, procedural, OOP and functional language.
For comparision sake, R is functional language and C++/Java is OOP. NON EXHAUSTIVE.
If you wise, you can compare Python to JavaScript but JS is a VERY messy language (experienced it)
'''

'''
I will create a Student Object to show you the basics
'''

class Student(): # Parentheses are optional, I just put it to look cool
    def __init__(self, name, gender, major, school): # In the parentheses, put in the attributes/properties you want your Student class to have
        self.name = name
        self.gender = gender
        self.major = major
        self.school = school
# Basics of init function, this creates an instance of the class
# For more advanced form of init, you can pass in functions in functions in functions, loops in loops in loops, learn Data Structures you will understand what I mean (I have these codes on my github)

    def __str__(self):
        return f'Hi, my name is {self.name} and I am a {self.gender}. I am reading {self.major} at {self.school}!'

# To look pro, I usually call the str function. This returns properties (defined) as a string, NOT object memory (like: <__main__.Student object at 0x030BE1C0>).
#__str__ makes is readable to non programming people!
# Optional, but I recommend

    def sum(self, x, y):
        return x + y
# This is basic, a sum function! I am only doing this to show you that you can define whatever functions you want the student class to take (basically instructions, like any normal functions)

# Student Class/Object created! Terms are interchangable!

# Instantiate the Object (Make it exist)
student_1 = Student('Jillese', 'Female', 'MSc. Mech Eng', 'NTU') # Remember to input the attributes as arguement into the parentheses

# Print the student
print(student_1)

# Comment out the def str and see the difference for yourself!
print(student_1)



'''
Why are classes good?

You can define ANYTHING, literally ANYTHING!!!!!!

If you haven't already notice, classes objects are similar to methods/functions (ie to say: int(), print(), sum() etc etc you get me).
All these methods/functions (int() blah blah) are pre-defined classes by the creator of python! If you want to understand the pain, do Java. 
EVERYTHING you do, even calling print(), will need to have a class object created for it!
'''
