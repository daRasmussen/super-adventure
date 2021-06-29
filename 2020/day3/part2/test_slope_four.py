import main


def test_slope_four():
    slope = [7, 1]
    number_of_trees = 4
    res = main.fill_re([slope], [])
    assert number_of_trees == res[0]
