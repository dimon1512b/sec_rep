"""
Work with big data
Operative: 1.6MB (3.2MB was before NamedTuple)
Main memory: 606KB
Finished
"""

import logging
import os
from random import randint
from typing import NamedTuple

from pympler import asizeof

logging.basicConfig(filename='log.log', level=logging.DEBUG)
my_list = []


def size(num, suffix='B'):
	for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
		if abs(num) < 1024.0:
			return "%3.1f%s%s" % (num, unit, suffix)
		num /= 1024.0
	return "%.1f%s%s" % (num, 'Yi', suffix)


class RecordNamedTuple(NamedTuple):
	int1: int
	int2: int
	int3: int


for i in range(10000):
	my_list.append(RecordNamedTuple(
		int1=randint(1, 10000),
		int2=randint(1, 10000),
		int3=randint(1, 10000)
	))
	logging.info(f'{my_list[i]}')

print(f'Operative: {size(asizeof.asizeof(my_list))}')
print(f'Main memory: {(os.stat("log.log").st_size) // 1000}KB')
print('Finished')
