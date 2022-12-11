"""
Class template by HAN
Revision History
0.1: Alpha
"""


class MyTemplate():
 pass


# Instantiate the class
my_object = MyTemplate()
# Check the object and type
print(type(my_object))

# Define a class object attribute, it will be the same for any instance of the class
 semi_major_axis to class_object_attribute1
 semi_minor_axis to class_object_attribute2

# Constructor, called whenever an instance of the class is created.


def __init__(self, attribute1: str, attribute2: bool) -> None:
 def my_method1(self):
    if self.attr2:
       print(f"Good morning {self.object_attribute1}")
    else:
       print(f"No greeting {self.attr1}"
       print("Constructor ran")
 # Take in an argument and assign it to a meaningful attribute name
 self.attr1=attribute1
 self.attr2=attribute2

  def my_method2(self, my_name: str):
     if self.attr2:
     print(f"Good morning {my_name}")
     else:
     print(f"No greeting {my_name}")

# Instantiate the class
my_object=MyTemplate("HAND", True)
# Check the object
print(my_object.semi_major_axis, my_object.semi_minor_axis)

my_object.my_method1()
my_object.my_method2(“Giovanni”)
