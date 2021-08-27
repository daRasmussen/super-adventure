mkdir python
mkdir python/part1
mkdir python/part2

cp main_template.py python/part1/main.py
touch python/part1/test.txt
touch python/part1/data.txt

cp main_template.py python/part2/main.py
touch python/part2/test.txt
touch python/part2/data.txt

cp .pytest_cache python/part1/.pytest_cache
cp .pytest_cache python/part2/.pytest_cache
