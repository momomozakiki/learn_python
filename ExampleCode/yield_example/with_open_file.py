from contextlib import contextmanager

# https://stackoverflow.com/questions/4015417/why-do-python-classes-inherit-object
# class MessageWriter(object): # Something related to old and new style of python 2 and 3
class MessageWriter:
	def __init__(self, filename):
		self.file_name = filename

	@contextmanager
	def open_file(self):
		try:
			file = open(self.file_name, 'w')
			yield file
		finally:
			file.close()


# usage
message_writer = MessageWriter('hello.txt')
with message_writer.open_file() as my_file:
	my_file.write('Shit\n')
	my_file.write('Hello\t')
	my_file.write('Hello\n')
	my_file.write('Hello\n')
	my_file.write('Hello\n')

