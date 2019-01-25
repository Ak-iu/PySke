from pyske.errors import NotEqualSizeError, EmptyError, TestFailure
from pyske.test.run import run_tests
from pyske.slist import SList


# -------------------------- #

def test_head_empty():
	sl = SList()
	exp = None
	res = sl.head()
	assert res == exp


def test_head_one():
	sl = SList()
	exp = 1
	sl.append(exp)
	res = sl.head()
	assert res == exp


def test_head_several():
	sl = SList()
	exp = 1
	sl.append(exp)
	sl.append(exp + 1)
	res = sl.head()
	assert res == exp


tests_head = [test_head_empty, test_head_one, test_head_several]

# -------------------------- #

def test_tail_empty():
	sl = SList()
	exp = SList()
	res = sl.tail()
	assert res == exp


def test_tail_one():
	sl = SList([1])
	exp = SList()
	res = sl.tail()
	assert res == exp


def test_tail_several():
	sl = SList([1, 2, 3])
	exp = SList([2, 3])
	res = sl.tail()
	assert res == exp


tests_tail = [test_tail_empty, test_tail_one, test_tail_several]

# -------------------------- #

def test_length_nil():
	sl = SList()
	exp = 0
	res = sl.length()
	assert res == exp


def test_length_cons():
	sl = SList([1, 2, 3])
	exp = 3
	res = sl.length()
	assert res == exp


tests_length = [test_length_nil, test_length_cons]

# -------------------------- #

def test_filter():
	sl = SList([1, 2, 3, 4, 5, 6, 7, 8])
	p = lambda x : x%2 == 0
	res = sl.filter(p)
	for r in res:
		assert p(r)

tests_filter = [test_filter]

# -------------------------- #

def test_empty_true():
	sl = SList()
	exp = True
	res = sl.empty()
	assert res == exp


def test_empty_false():
	sl = SList([1, 2, 3])
	exp = False
	res = sl.empty()
	assert res == exp

tests_empty = [test_empty_true, test_empty_false]

# -------------------------- #

def test_reverse_nil():
	sl = SList()
	exp = SList()
	res = sl.reverse()
	assert res == exp


def test_reverse_cons():
	sl = SList([1, 2, 3])
	exp = SList([3, 2, 1])
	res = sl.reverse()
	assert res == exp


tests_reverse = [test_reverse_nil, test_reverse_cons]

# -------------------------- #

def test_map_empty():
	sl = SList()
	exp = SList()
	f = lambda x: x
	res = sl.map(f)
	assert res == exp


def test_map_inc():
	sl = SList([1, 2, 3])
	exp = SList([2, 3, 4])
	f = lambda x: x + 1
	res = sl.map(f)
	assert res == exp


def test_map_id():
	sl = SList([1, 2, 3])
	exp = SList([1, 2, 3])
	f = lambda x: x
	res = sl.map(f)
	assert res == exp


tests_map = [test_map_empty, test_map_inc, test_map_id]

# -------------------------- #

def test_flat_map_empty():
	sl = SList()
	f = lambda x : range(0, x+1)
	res = sl.flat_map(f)
	exp = SList()
	assert res == exp

def test_flat_map_range():
	sl = SList([1, 2, 3])
	f = lambda x : range(0,x+1)
	res = sl.flat_map(f)
	exp = SList([0, 1, 0, 1, 2, 0, 1, 2, 3])
	assert res == exp

tests_flat_map = [test_flat_map_empty, test_flat_map_range]

# -------------------------- #

def test_reduce_nil():
	sl = SList()
	f = lambda x,y : x + y
	try:
		res = sl.reduce(f)
		raise TestFailure()
	except EmptyError as e:
		assert True


def test_reduce_cons():
	sl = SList([1, 2, 3, 4])
	f = lambda x,y : x + y
	res = sl.reduce(f)
	exp = 10
	assert res == exp

tests_reduce = [test_reduce_nil, test_reduce_cons]

# -------------------------- #

def test_scan_nil():
	c = 0
	sl = SList()
	f = lambda x,y : x + y
	res = sl.scan(f, c)
	exp = SList([0])
	assert res == exp


def test_scan_cons():
	c = 0
	sl = SList([1, 2, 3, 4])
	f = lambda x,y : x + y
	res = sl.scan(f, c)
	exp = SList([0, 1, 3, 6])
	assert res == exp

tests_scan = [test_scan_nil, test_scan_cons]

# -------------------------- #

def test_scan2_nil():
	c = 0
	sl = SList()
	f = lambda x,y : x + y
	res = sl.scan2(f, c)
	exp = SList([0])
	assert res == exp


def test_scan2_cons():
	c = 0
	sl = SList([1, 2, 3, 4])
	f = lambda x,y : x + y
	res = sl.scan2(f, c)
	exp = SList([9, 7, 4, 0])
	assert res == exp

tests_scan2 = [test_scan2_nil, test_scan2_cons]

# -------------------------- #

def test_zip_nil():
	sl1 = SList()
	sl2 = SList()
	res = sl1.zip(sl2)
	exp = SList()
	assert res == exp


def test_zip_cons():
	sl1 = SList([1, 2, 3])
	sl2 = SList([2, 3, 4])
	res = sl1.zip(sl2)
	exp = SList([(1,2),(2,3),(3,4)])
	assert res == exp


def test_zip_one_gt():
	sl1 = SList([1, 2, 3])
	sl2 = SList([2, 3])
	try:
		res = sl1.zip(sl2)
		raise TestFailure()
	except NotEqualSizeError as e:
		assert True


def test_zip_one_lt():
	sl1 = SList([2, 3])
	sl2 = SList([2, 3, 4])
	try:
		res = sl1.zip(sl2)
		raise TestFailure()
	except NotEqualSizeError as e:
		assert True

tests_zip = [test_zip_nil, test_zip_cons, test_zip_one_gt, test_zip_one_lt]

# -------------------------- #

def test_zipwith_nil():
	sl1 = SList()
	sl2 = SList()
	f = lambda x,y : x + y
	res = sl1.zipwith(sl2, f)
	exp = SList()
	assert res == exp


def test_zipwith_cons():
	sl1 = SList([1, 2, 3])
	sl2 = SList([2, 3, 4])
	f = lambda x,y : x + y
	res = sl1.zipwith(sl2,f)
	exp = SList([3,5,7])
	assert res == exp


def test_zipwith_one_gt():
	sl1 = SList([1, 2, 3])
	sl2 = SList([2, 3])
	f = lambda x,y : x + y
	try:
		res = sl1.zipwith(sl2,f)
		raise TestFailure()
	except NotEqualSizeError as e:
		assert True


def test_zipwith_one_lt():
	sl1 = SList([2, 3])
	sl2 = SList([2, 3, 4])
	f = lambda x,y : x + y
	try:
		res = sl1.zipwith(sl2,f)
		raise TestFailure()
	except NotEqualSizeError as e:
		assert True

tests_zipwith = [test_zipwith_nil, test_zipwith_cons, test_zipwith_one_gt, test_zipwith_one_lt]

# -------------------------- #

fcts = tests_head + tests_tail + tests_length + \
	tests_filter + tests_empty + tests_reverse + \
	tests_map + tests_flat_map + tests_reduce + \
	tests_scan + tests_scan2 + tests_zip + tests_zipwith

run_tests(fcts, "slist")
	

