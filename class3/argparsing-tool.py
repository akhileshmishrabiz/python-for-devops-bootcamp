import sys

import argparse # parsng the argumnets



# initialize the parser
parser = argparse.ArgumentParser(description="A simple argument parser example")

# add arguments
parser.add_argument("-n", "--name", type=str, required=True, help="Your name")
parser.add_argument("-a", "--age", type=int, required=True, help="Your age")
parser.add_argument("-c", "--city", type=str, required=False, help="Your city")

# print a help function if no argument is passed 
def print_help_if_no_args():
    print(
       """
      You need to provide your name with -n or --name - mantodatiory,
      You need tp nprovide your age with -a or --age - mandatory,
      You can provide your city with -c or --city - optional
       """
    )

print(f" Len of args {len(sys.argv)}")

if len(sys.argv) == 1:
    print_help_if_no_args()
    parser.print_help()
    sys.exit(1)

# Learn the vscode shortcut to comment and uncomment multiple lines at once
# ctrl + /  or cmd + / -> comment the code block and uncommet it again
# to move the code block left or right use ->  "cmd + [" ," cmd + ]" 


# print("Parsing the arguments now...")
# # parse the arguments
# args = parser.parse_args()
# name = args.name
# age = args.age
# city = args.city 

# message = f"Hello, {name}! You are {age} years old."

# if city:
#     message += f" You live in {city}."

# print(message)