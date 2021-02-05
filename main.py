from dataclasses import dataclass
import csv, os
from typing import Tuple, List


@dataclass
class User:
    """
    Represent user in system
    """
    first_name: str
    last_name: str
    phone_number: str

    def __eq__(self, other: "User"):
        if not isinstance(other, User):
            return False
        return other.first_name == self.first_name and \
               other.last_name == self.last_name and \
               other.phone_number == self.phone_number

    def __str__(self):
        return f"[USER] {self.first_name} " \
               f"{self.last_name} - {self.phone_number}"

def is_valid_name(name: str) -> bool:
    if name.isalpha():
        return True
    else:
        return False

def is_valid_number(number: str) -> bool:
    if number.isdecimal():
        return True
    else:
        return False

def is_valid_user(user: list) -> List[bool]:
    result = []
    for name in user[:2]:
        result.append(is_valid_name(name))
    result.append(is_valid_number(user[2]))
    return result


def load_csv(path: str) -> List[List[str]]:
    cwd = os.path.dirname(__file__)
    f = open(os.path.join(cwd, path), 'r+', newline='')
    reader = csv.reader(f)
    f.seek(0)
    data = list(reader)
    return data

def error_constructor(idx: int, validity: list) -> str:
    error_message = f"[ERROR - row {idx}]"
    is_added = False

    if not validity[0]:
        error_message += " invalid first name"
        is_added = True
    if not validity[1]:
        if is_added:
            error_message += ","
        else:
            is_added = True
        error_message += " invalid last name"
    if not validity[2]:
        if is_added:
            error_message += ","
        error_message += " invalid phone number"

    return error_message

def process_csv(path: str) -> Tuple[List[User], List[str]]:
    data = load_csv(path)
    users, errors = [],[]

    for idx,user in enumerate(data[1:]):
        validity = is_valid_user(user)
        if validity[0] and validity[1] and validity [2]:
            valid_user = User(user[0],user[1],user[2])
            users.append(valid_user)
        else:
            error_message = error_constructor(idx,validity)
            errors.append(error_message)
    return users, errors

def is_correct(users: [User], errors: [str]):
    assert users[0] == User("John", "Doe", "777777777")
    assert users[1] == User("Foo", "Bar", "123456789")
    assert users[2] == User("Jane", "Doe", "888888888")
    assert users[3] == User("Bar", "Foo", "123456789")
    assert users[4] == User("Jason", "Doe", "999999999")

    assert errors[0] == "[ERROR - row 2] invalid first name, invalid last name"
    assert errors[1] == "[ERROR - row 5] invalid phone number"

    return True

users, errors = process_csv("users.csv")

if is_correct(users, errors):
    print("This solution is correct")


# The goal is to finish process_csv function to return valid User classes
# from CSV with valid data and a list of errors.
# with valid data and list of errors.
# Users should be returned as list of instances of User class
# Validation rules are simple:
# First and last name can contain only alphabet letter
# Phone number can contain only numbers
# Errors should be returned as list of strings in format
# (one string for each invalid row)
# [ERROR - row {row_number}] invalid {field name}, invalid {field name}, ....
# You are allowed manipulate everything but function is_correct
# You can check if your solution is correct
# by executing `python process_csv.py`.
