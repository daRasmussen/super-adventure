import getopt
import sys
import os
from pathlib import Path

argv = sys.argv[1:]

def get_template(day, year):
    lines = [
        "from aocd import submit, get_data\n",
        "\n",
        f"data = get_data(day={day}, year={year})\n",
        "print(data)\n"
        "\n",
        "ans = ''\n",
        "\n",
        f"# submit(ans, part='a', day={day}, year={year})\n",
        f"# submit(ans, part='b', day={day}, year={year})\n",
    ]
    return "".join(lines) 

try:
    year = ""
    options, args = getopt.getopt(argv, "y:")
    for name, value in options:
        if name in ["-y"]:
            year = value
            os.mkdir(year)
            for nbr in range(26):
                day = f"day{nbr}"
                # create dir
                target = Path(year) / Path(day)
                os.mkdir(target)
                # create file main.py
                main = target / Path("main.py")
                f = open(main, "x")
                # write template to file
                template = get_template(nbr, year)
                f.write(template)
                #print(template)

except:
    print("Error Message")

