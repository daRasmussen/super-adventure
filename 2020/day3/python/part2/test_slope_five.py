import main


def test_slope_five():
    slope = [1, 2]
    number_of_trees = 2
    res = main.fill_re([slope], [])
    assert number_of_trees == res[0]
