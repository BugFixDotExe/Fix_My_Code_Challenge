#!/usr/bin/python3
"""
A User class
"""


class User():
    """ A Class that defines the properties of a user """

    def __init__(self):
        """ The constructor of the class """
        self.__email = None

    @property
    def email(self):
        """ The getter method for the class """
        return self.__email

    @email.setter
    def email(self, value):
        """ The setter method of the class """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
