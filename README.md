0x00. AirBnB clone - The console team project

This project has the aim of building console
It is a team of two students project

The first step here is creating data model and managing it through different commands like
	#create
	#show
	#quit
	#EOF
	#update
	#all

example 

import cmd
import datetime
from base model import BaseModel

class class HBNBCommand(cmd.Cmd):
	
	prompt = '(hbnb)'
	
	def do_EOF(self, line):
		return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()


