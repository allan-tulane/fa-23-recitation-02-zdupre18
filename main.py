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
        return 1  # Base case

    # Recursive step
    return a * simple_work_calc(n // b, a, b) + n

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
        return f(1)  

    total_work = f(n)  
    for i in range(1, b + 1):
        total_work += a * work_calc(n // b, a, b, f)

    return total_work

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
    total_work = f(n)  # Work done at the current node
    for i in range(1, b + 1):
        total_work += a * work_calc(n // b, a, b, f)

    return total_work



def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in input_sizes:
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
        work1 = work_calc(work_fn1, n)
        work2 = work_calc(work_fn2, n)

        print(f"n = {n}: Work Function 1 = {work1}, Work Function 2 = {work2}")
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work
    
	# create work_fn1
	# create work_fn2

    res = compare_work(work_fn1, work_fn2)
	print(res)
n_values = [1, 10, 100, 1000, 10000]
test_compare_work(n_values)

def test_compare_span(n_values):
    a = 2  # Number of processors

    for n in n_values:
        span_1 = span_calc(a, work_function_1, n)
        span_n_squared = span_calc(a, work_function_n_squared, n)
        span_n_log_n = span_calc(a, work_function_n_log_n, n)

        print(f"n = {n}: Span (Constant Work) = {span_1}")
        print(f"n = {n}: Span (Quadratic Work) = {span_n_squared}")
        print(f"n = {n}: Span (Linearithmic Work) = {span_n_log_n}")

            # Add more test cases as needed
        n_values = [1, 10, 100, 1000, 10000]
test_compare_span(n_values)

