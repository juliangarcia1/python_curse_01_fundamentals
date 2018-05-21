import sys

def my_function(param):
	print("Hello {}!!".format(param))

if __name__ == '__main__':
	my_function(sys.argv[1:])