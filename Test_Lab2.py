import lab2

def test_min_max():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 90]
    result = lab2.find_min_max(input_arr)

    assert (result == test_arr)

def test_average():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = 36.857142857142854
    result = lab2.calc_average(input_arr)

    assert (result == test_arr)

def test_median_temperature():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = 25
    result = lab2.calc_median_temperature(input_arr)

    assert (result == test_arr)
