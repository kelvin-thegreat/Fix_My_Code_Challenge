#!/usr/bin/python3

class User:
    """User class represents a user object."""

    def __init__(self):
        """Initialize a User object."""
        self.__email = None

    @property
    def email(self):
        """Getter method for the email attribute."""
        return self.__email

    @email.setter
    def email(self, value):
        """Setter method for the email attribute.

        Args:
            value (str): The email address to set.

        Raises:
            TypeError: If the value is not a string.

        """
        if not isinstance(value, str):
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":
    u = User()
    u.email = "john@snow.com"
    print(u.email)

