# module required

import sys
import datetime


# help function

def help():
    system_architecture = """Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics"""
    sys.stdout.buffer.write(system_architecture.encode('utf8'))


x = 'looked'


def basic_me(age, name):
    # This prints out "John is 23 years old."
    print("I am %d, and my name is %s" % (age, name))


basic_me(26,"Williams Sidis")