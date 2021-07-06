import main


def slope_one():
    slope = [1, 1]
    number_of_trees = 2
    res = main.fill_re([slope], [])
    assert number_of_trees == res[0]


def slope_two():
    slope = [3, 1]
    number_of_trees = 7
    res = main.fill_re([slope], [])
    assert number_of_trees == res[0]


def slope_three():
    slope = [5, 1]
    number_of_trees = 3
    res = main.fill_re([slope], [])
    assert number_of_trees == res[0]


def slope_four():
    slope = [7, 1]
    number_of_trees = 4
    res = main.fill_re([slope], [])
    assert number_of_trees == res[0]


def slope_five():
    slope = [1, 2]
    number_of_trees = 2
    res = main.fill_re([slope], [])
    assert number_of_trees == res[0]


def all_slopes():
    slope_one()
    slope_two()
    slope_three()
    slope_four()
    slope_five()
