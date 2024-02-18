# AirBnB clone
**About:** In this project, we created an AirBnb clone which is a copy of the [AirBnb website](https://www.airbnb.com/)

### The application is composed by:

- A [console](#Console) to manipulate data without a visual interface.
- A website(the front-end) that shows the final product.
- A database or files that store data.
- An API that provides a communication interface between the frontend your data. 

### Console
The console is responsible for:
- creating the data model.
- managing objects via the console.
- storing and persisting objects to a file(JSON file).

## Usage(interactive mode):
	$ ./console.py
	(hbnb) help

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit

	(hbnb)
	(hbnb)
	(hbnb) quit

	$

## Alternatively(non-interactive mode):

	
	$ echo "help" | ./console.py

	(hbnb)
	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	
	(hbnb)
	$
	$ cat test_help
	help
	$
	$ cat test_help | ./console.py

	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit

	(hbnb)

	$
