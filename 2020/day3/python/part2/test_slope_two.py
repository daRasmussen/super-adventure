import main


def test_slope_two():
    slope = [3, 1]
    number_of_trees = 7
    res = main.fill_re([slope], [])
    assert number_of_trees == res[0]
