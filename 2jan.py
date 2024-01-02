#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Animal:

    
    name = ""
    
    def eat(self):
        print("I can eat")

# inherit from Animal
class Dog(Animal):

    
    def display(self):
        print("My name is ", self.name)


labrador = Dog()
labrador.name = "Rohu"
labrador.eat()
labrador.display()


# # Types of inheritance
#         

# In[9]:


#single inheritance(when class inherits from single parent class)
class Parent:
    def parent_method(self):
        print("this is parent method")
        
class child(Parent):
    def child_method(self):
        print("This is child method")


# In[12]:


obj=child()
obj.parent_method()
obj.child_method()


# In[14]:


#multiple inheritance(when inherits from more then one parent class)
class parent1:
    def parent1_method(self):
        print('this is parent1 method')
        
class parent2:
    def parent2_method(self):
        print('this is parent2 method')
        
class child(parent1,parent2):
     def child_method(self):
        print("this is child method")


# In[15]:


obj=child()
obj.parent1_method()
obj.parent2_method()
obj.child_method()


# In[18]:


#mulrilevel inheeritance(here one parent class inherits from another parent class)
class grandparent:
    def grandparent_method(self):
        print('This is grandparent method')
    
class parent(grandparent):
    def parent_method(self):
        print("this is parent class")
    
class child(parent):
    def child_method(self):
        print("this is child class")
         


# In[19]:


obj=child()
obj.grandparent_method()
obj.parent_method()
obj.child_method()


# In[30]:


#hierarchical inheritance(base class inherited by multiple derived classes)
# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")
 
 
class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")
 
 
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")


# In[31]:


object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()


# In[33]:


#hybrid inheritace(combination of single,multiple,multilevel)
 
class School:
    def func1(self):
        print("This function is in school.")
 
 
class Student1(School):
    def func2(self):
        print("This function is in student 1. ")
 
 
class Student2(School):
    def func3(self):
        print("This function is in student 2.")
 
 
class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")


# In[34]:


object = Student3()
object.func1()
object.func2()


# In[ ]:




