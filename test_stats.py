from stats import mean

def test_mean():
	assert(mean([2,4]) ==3)
test_mean()

def test_float_mean():
	assert(mean(2,4]) ==1.5)
test-float_mean()