import main


def test_slope_one():
    slope = [1, 1]
    number_of_trees = 2
    res = main.fill_re([slope], [])
    assert number_of_trees == res[0]
