~Python week 2~
#ANATOMY OF A FUNCTION

*args
There is a rule when using this keyword in Python i.e. they must come after the positional arguments.
If we want to allow users to pass in any number of variables, use the asterisk symbol before the argument name to create a pointer to the inputted variables.

**kwargs (keyword argument)
kwargs are used to handle keyword arguments.
Print kwargs to see that the keyword arguments are now stored as a dictionary instead of a tuple.

locals()
Variable names are only accessible locally within a function.

globals()
Defined outside the function in the main code block.

message = 'Some global data'
def function1(varA, varB):
    print(message)
    print(locals())

def function2(varC, varB):
    print(message)
    print(locals())

function1(1, 2)
function2(3, 4)
//if there is an attempt to print varA in function2, an error will occur since varA is defined in function1's local scope.


_code_

The "code" attribute of Python function objets can be used to confirm that functions are just variables in Python.

LAMBDA FUNCTION
These are a way to represent a function without giving it a variable name.
For example: x:x+3 is a lambda function that takes a single parameter x and returns x plus 3.
You do not need to use the return keyword in lambda functions since its implied.


~ANATOMY OF A CLASS~

#Instance Attributes

class: Dog
    def _init_(self, name):
    self.name = name
    self.legs = 4
    
    def speak(self)
    print(self.name + 'says: Bark!')

myDog = Dog('Rover')
print(myDog.name)
print(myDog.legs)

//This class has 2 instance attributes, name and legs, which are attributes that every instance of a dog possesses. When we create a new instance, such as 'Rover", we can print its name and legs using "my_dog.name" and "my_dog.legs" respectively.

#Static Attributes

class: Dog
  legs = 4
  def _init_(self, name)
  self.name = name

  def speak(self):
  print(self.name + 'says: Bark!')

myDog = Dog('Rover')
print(myDog.name)
print(myDog.legs)

//Instead of keeping 'legs' in the constructor, we define it as a static variable outside a constructor, This means that each instance of the class will have the same value for legs.
These varibles are called static because they dont change with each instance and are commonly used to hold constants or fundamental business logic.

#ERRORS AND EXCEPTIONS
In python you will find that exceptions are determined during runtime and can be retried, whereas errors cannot be retried.

#TRY/ EXCEPTION
try:
    1/0
except Exception as e:
   print(type(e))
