import main


def test_slope_three():
    slope = [5, 1]
    number_of_trees = 3
    res = main.fill_re([slope], [])
    assert number_of_trees == res[0]
