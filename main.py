"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
###

def simple_work_calc(n, a, b):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + n

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor

	Returns: the value of W(n).
	"""
	# TODO
	if n == 1:
		return 1
	elif n == 0:
		return 0
	return a*simple_work_calc(n//b, a, b) + n
def test_simple_work():
	""" done. """
	assert simple_work_calc(8, 2, 2) == 32
	assert simple_work_calc(8, 3, 2) == 65  
	assert simple_work_calc(9, 2, 3) == 19  
def work_calc(n, a, b, f):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	# TODO
	if n == 1:
		return 1
	elif n == 0:
		return 0
	return a*work_calc(n//b, a, b, f) + f(n)

def span_calc(n, a, b, f):
	"""Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	# TODO
	 if n == 1:
        return f(1)  # Base case

    # Recursive step
   if n == 1:
		return 1
	elif n == 0:
		return 0
	return span_calc(n//b, a, b, f) + f(n)


def test_work():
	""" done. """
	assert work_calc(8, 2, 2,lambda n: n) == 32 
	assert work_calc(8, 1, 2, lambda n: n*n) == 85 
	assert work_calc(8, 3, 2, lambda n: 1) == 40   

def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((
			n,
			work_fn1(n),
			work_fn2(n)
			))
	return result

def span_calc(a, W, n):
def work_function_constant(n):
    return 1

def work_function_logarithmic(n):
    return int(math.log(n, 2))

def work_function_linear(n):
    return n


def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))

def work_fn1(n):
    # Define the first work function
    return n**2

def work_fn2(n):
    # Define the second work function
    return n * (n-1)

def test_compare_work(n_values):
    for n in n_values:
        # Compare work functions using compare_work
       def curry_work(a,b,f):
		return lambda n: work_calc(n, a, b, f)

	res = compare_work(curry_work(2, 2, lambda n: 1),
			  		   curry_work(2, 2, lambda n: n))
	print_work_results(res)

	res = compare_work(curry_work(2, 2, lambda n: n),
			  		   curry_work(2, 2, lambda n: n*n))
	print_work_results(res)

	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work
    
	# create work_fn1
	# create work_fn2

  
def test_compare_span(n_values):
   def curry_span(a,b,f):
		return lambda n: span_calc(n, a, b, f)

	res = compare_span(curry_span(2, 2, lambda n: 1),
			  		   curry_span(2, 2, lambda n: n))
	print_span_results(res)

	res = compare_span(curry_span(2, 2, lambda n: n),
			  		   curry_span(2, 2, lambda n: n*n))
	print_span_results(res)


