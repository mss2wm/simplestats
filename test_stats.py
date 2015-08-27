from stats import mean, std
from nose.tools import assert_equal, assert_almost_equal

def test_mean():
	assert_equal(mean([2,4]), 3)
#test_mean()

def test_float_mean():
	assert_equal(mean([1.0,2]), 1.5)
#test-float_mean()

def test_neg_mean():
	assert_almost_equal(mean([-2,2,4]), 1.333, places=3)
#test_neg_mean()

def test_std():
	obs = std([0.0, 2.0])
	exp = 1.0
	assert_equal(obs,exp)