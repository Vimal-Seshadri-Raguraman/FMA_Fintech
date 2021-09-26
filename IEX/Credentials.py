import os

def add_env_var():
    attribute = input("Enter the attribute name: ")
    value = input(f"Enter {attribute} value: ")
    set_env_var(attribute, value)

def set_env_var(attribute, value):
    os.environ[attribute] = value

def get_env_var(attribute):
    os.environ.get(attribute)
