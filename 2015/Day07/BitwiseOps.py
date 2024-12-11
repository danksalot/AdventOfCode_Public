from collections import defaultdict

wires = defaultdict(None)

def getValue(token):
	try:
		return int(token)
	except:
		try:
			return int(wires[token])
		except:
			return token

def Resolve(value, key):
	wires[key] = value

def Reset():
	wires.clear()

class Assignment:
	left = None
	right = None

	def __init__(self, left):
	    self.left = left

	def result(self):
		if (isinstance(getValue(self.left), int)):
			return getValue(self.left)
		else:
			return None

class AndGate:
	left = None
	right = None
	def __init__(self, left, right):
	    self.left = left
	    self.right = right

	def result(self):
		if (isinstance(getValue(self.left), int) and isinstance(getValue(self.right), int)):
			return getValue(self.left) & getValue(self.right)
		else:
			return None

class OrGate:
	left = None
	right = None
	def __init__(self, left, right):
	    self.left = left
	    self.right = right

	def result(self):
		if (isinstance(getValue(self.left), int) and isinstance(getValue(self.right), int)):
			return getValue(self.left) | getValue(self.right)
		else:
			return None
			
class NotGate:
	left = None
	right = None
	def __init__(self, left):
	    self.left = left

	def result(self):
		if (isinstance(getValue(self.left), int)):
			return ~ getValue(self.left)
		else:
			return None

class LShift:
	left = None
	right = None
	def __init__(self, left, right):
	    self.left = left
	    self.right = right

	def result(self):
		if (isinstance(getValue(self.left), int) and isinstance(getValue(self.right), int)):
			return getValue(self.left) << getValue(self.right)
		else:
			return None

class RShift:
	left = None
	right = None
	def __init__(self, left, right):
	    self.left = left
	    self.right = right

	def result(self):
		if (isinstance(getValue(self.left), int) and isinstance(getValue(self.right), int)):
			return getValue(self.left) >> getValue(self.right)
		else:
			return None
