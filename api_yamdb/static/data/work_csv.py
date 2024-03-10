print('script run')
import csv
from pathlib import Path
import os
import json

'''
print(__file__)
BASE_DIR = Path(__file__).resolve().parent.parent
print(Path(__file__).resolve())
# new: Path.cwd() old: os.getcwd()
# os.makedirs  Path().mkdir()
# p.exists()   is_file  is_dir

print('BASE_DIR:', BASE_DIR)
print(Path.cwd())
print(Path.home())
p = Path.cwd()
print(p.anchor)
print(p.parent)
print(p.name)
print('*'*30)
print(os.listdir(Path.home()))
print(os.listdir(Path(__file__).resolve().parent))
print('+'*30)
print(Path.cwd().glob('*'))
'''

with open('category.csv', encoding='utf-8') as file_csv:
    example_dict  = csv.DictReader(file_csv)
    for i in example_dict:
        j = json.dumps(i)
        print(j)