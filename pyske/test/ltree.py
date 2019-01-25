from pyske.test.run import run_tests
from pyske.ltree import LTree, Segment, TaggedValue
from pyske.slist import SList
from pyske.errors import IllFormedError, EmptyError, TestFailure


# -------------------------- #

#TODO

tests_serialization = []

# -------------------------- #

#TODO

tests_deserialization = []

# -------------------------- #

def test_map_empty():
	lt = LTree()
	id_f = lambda x : x
	try:
		res = lt.map(id_f, id_f)
		assert False
	except EmptyError as e:
		assert True


def test_map_not_empty():
	seg1 = Segment([TaggedValue(13, "C")])
	seg2 = Segment([TaggedValue(31, "N"),TaggedValue(47, "L"),TaggedValue(32, "L")])
	seg3 = Segment([TaggedValue(72, "N"),TaggedValue(92, "L"),TaggedValue(42, "L")])
	lt = LTree([seg1, seg2, seg3])

	plus1 = lambda x : x + 1
	minus1 = lambda x : x - 1
	
	res = lt.map(plus1, minus1)

	seg1_exp = Segment([TaggedValue(12, "C")])
	seg2_exp = Segment([TaggedValue(30, "N"),TaggedValue(48, "L"),TaggedValue(33, "L")])
	seg3_exp = Segment([TaggedValue(71, "N"),TaggedValue(93, "L"),TaggedValue(43, "L")])

	exp = LTree([seg1_exp,seg2_exp,seg3_exp])
	assert res == exp

tests_map = [test_map_empty,test_map_not_empty]

# -------------------------- #

def test_reduce_empty():
	lt = LTree()
	id_f = lambda x : x
	sum3 = lambda x,y,z : x + y + z
	try:
		lt.reduce(sum3, id_f, sum3, sum3, sum3)
		raise TestFailure()
	except EmptyError as e:
		assert True


def test_reduce_illformed():
	seg1 = Segment([TaggedValue(13, "C")])
	seg3 = Segment([TaggedValue(72, "N"),TaggedValue(92, "L"),TaggedValue(42, "L")])
	lt = LTree([seg1, seg3])
	id_f = lambda x : x
	sum3 = lambda x,y,z : x + y + z
	try:
		lt.reduce(sum3, id_f, sum3, sum3, sum3)
		raise TestFailure()
	except IllFormedError as e:
		assert True


def test_reduce():
	seg1 = Segment([TaggedValue(13, "C")])
	seg2 = Segment([TaggedValue(31, "N"),TaggedValue(47, "L"),TaggedValue(32, "L")])
	seg3 = Segment([TaggedValue(72, "N"),TaggedValue(92, "L"),TaggedValue(42, "L")])
	lt = LTree([seg1, seg2, seg3])
	id_f = lambda x : x
	sum3 = lambda x,y,z : x + y + z
	res = lt.reduce(sum3, id_f, sum3, sum3, sum3)
	exp = 13 + 31 + 47 + 32 + 72 + 92 + 42
	assert res == exp

tests_reduce  = [test_reduce_empty, test_reduce_illformed, test_reduce]

# -------------------------- #

def test_uacc_empty():
	lt = LTree()
	id_f = lambda x : x
	sum3 = lambda x,y,z : x + y + z
	try:
		lt.uacc(sum3, id_f, sum3, sum3, sum3)
		raise TestFailure()
	except EmptyError as e:
		assert True

def test_uacc_illformed():
	seg1 = Segment([TaggedValue(13, "C")])
	seg3 = Segment([TaggedValue(72, "N"),TaggedValue(92, "L"),TaggedValue(42, "L")])
	lt = LTree([seg1, seg3])
	id_f = lambda x : x
	sum3 = lambda x,y,z : x + y + z
	try:
		lt.uacc(sum3, id_f, sum3, sum3, sum3)
		raise TestFailure()
	except IllFormedError as e:
		assert True

def test_uacc():
	seg1 = Segment([TaggedValue(13, "C")])
	seg2 = Segment([TaggedValue(31, "N"),TaggedValue(47, "L"),TaggedValue(32, "L")])
	seg3 = Segment([TaggedValue(72, "N"),TaggedValue(92, "L"),TaggedValue(42, "L")])
	lt = LTree([seg1, seg2, seg3])
	id_f = lambda x : x
	sum3 = lambda x,y,z : x + y + z
	res = lt.uacc(sum3, id_f, sum3, sum3, sum3)

	seg1_exp = Segment([TaggedValue(13+31+47+32+72+92+42, "C")])
	seg2_exp = Segment([TaggedValue(31+47+32, "N"),TaggedValue(47, "L"),TaggedValue(32, "L")])
	seg3_exp = Segment([TaggedValue(72+92+42, "N"),TaggedValue(92, "L"),TaggedValue(42, "L")])
	exp = LTree([seg1_exp, seg2_exp, seg3_exp])


tests_uacc = [test_uacc_empty, test_uacc_illformed, test_uacc]

# -------------------------- #

def test_dacc_empty():
	sum2 = lambda x,y : x + y
	c = 0
	id_f = lambda x : x
	lt = LTree()
	try:
		lt.dacc(sum2, sum2, c, id_f, id_f, sum2, sum2)
		raise TestFailure()
	except EmptyError as e:
		assert True


def test_dacc():
	sum2 = lambda x,y : x + y
	c = 0
	id_f = lambda x : x
	seg1 = Segment([TaggedValue(13, "C")])
	seg2 = Segment([TaggedValue(31, "N"),TaggedValue(47, "L"),TaggedValue(32, "L")])
	seg3 = Segment([TaggedValue(72, "N"),TaggedValue(92, "L"),TaggedValue(42, "L")])
	lt = LTree([seg1, seg2, seg3])
	res = lt.dacc(sum2, sum2, c, id_f, id_f, sum2, sum2)

	seg1_exp = Segment([TaggedValue(0, "C")]) 
	seg2_exp = Segment([TaggedValue(13, "N"),TaggedValue(13 + 31, "L"),TaggedValue(13 + 31, "L")])
	seg3_exp = Segment([TaggedValue(13, "N"),TaggedValue(13 + 72, "L"),TaggedValue(13 + 72, "L")])
	exp = LTree([seg1_exp, seg2_exp, seg3_exp])

	assert res == exp


tests_dacc = [test_dacc_empty, test_dacc]

# -------------------------- #


fcts = tests_deserialization + tests_serialization + tests_map + \
		tests_reduce + tests_uacc + tests_dacc

run_tests(fcts, "ltree")
