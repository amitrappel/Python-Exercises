from __future__ import with_statement
from itertools import groupby
import sys
import os


def is_full_range(lg, l_prefix):
    """
    Returns True if lg contains all the numbers starting
    with the same l_prefix digits. See examples below.
    :param lg: iterable of integers AS STRINGS
    :param l_prefix: suggested length of common prefix
    :return: Boolean
    """
    return len(lg) == 10**(len(lg[0])-(l_prefix))


def find_prefixes(g_nums, l_prefix=1, prefixes=[]):
	"""
	Returns a list of unique prefixes
	:param g_nums: list of integers AS STRINGS
	:param l_prefix: suggested length of common prefix
	:param prefixes: list of unique prefixes, gradually collected by the function
	:return: list of unique prefixes
	"""
	"""
	:param g_nums:
	:param l_prefix:
	:return:
	"""

	#print len(g_nums), g_nums
	#if len(g_nums) == 0:
	#	prefixes=[]
	#	return prefixes

	n_digits = len(g_nums[0])
	for k, g in groupby(g_nums, lambda x: x[:l_prefix]):
		lg = list(g)
		if is_full_range(lg, l_prefix):
			prefixes.append(k)
			#if len(k) < n_digits:
			#    prefixes.append(k + '*')
			#else:
			#    prefixes.append(k)
		else:
			find_prefixes(lg, len(k)+1, prefixes)
	return prefixes


def examples():
    print is_full_range([str(x) for x in range(100, 200)], 1)
    # >>> True

    print is_full_range([str(x) for x in range(120, 130)], 1)
    # >>> False

    print is_full_range([str(x) for x in range(120, 130)], 2)
    # >>> True

def main():
    # examples()
    #nums = sorted([str(num) for num in range(1157, 4773)])
    #nums = sorted([str(num) for num in range(9100, 9499+1)])
    #print nums
    #prefixes = find_prefixes(nums)
    #print prefixes

    #print find_prefixes(sorted([str(num) for num in range(93709100000, 93709499999 + 1)]))
    #print find_prefixes(sorted([str(num) for num in range(int(sys.argv[1]), int(sys.argv[2]) + 1)]))

	if len(sys.argv) == 1:
		print "Usage:"
		print sys.argv[0] + " <from> <to>"
		print "or"
		print sys.argv[0] + " <filename>"
		print "Example of input file:"
		print "RBNO,381610110000,381610139999"
		print "YUGTS,381650050000,381650059999"
		print "INXIX,870777010000,870777099999"
		return

	if (len(sys.argv) == 3):
		for prefix in find_prefixes(sorted([str(num) for num in range(int(sys.argv[1]), int(sys.argv[2]) + 1)])):
			print prefix
	else:
		#work with file
		if sys.argv[1][0] == "." or sys.argv[1][0:2] == ".." or  sys.argv[1][0] != "/":
			filename = os.getcwd() + "/" + sys.argv[1]
		else:
			filename = sys.argv[1]
		print filename
		try :
			with open(filename) as f:
				for line in f:
					print line,
					if line[0]=="#":
						continue
					if len(line) <= 5:
						continue
					fields = line.split(",")
					if fields[1] == "Start":
						continue
					if int(fields[2]) < int(fields[1]):
						print "error in fields[0] : TO < FROM :: " + line,
					#print fields
					try:
						for prefix in find_prefixes(sorted([str(num) for num in range(int(fields[1]), int(fields[2]) + 1)])):
							print fields[0], prefix
							#print prefixes
							#nums = sorted([str(num) for num in range(1157, 1161)])
							#nums = sorted([str(num) for num in range(9100, 9499+1)])
							#print nums
							#prefixes = find_prefixes(nums)
							#print prefixes
							#find_prefixes([])

							#for prefix in prefixes:
								#print fields[0], prefix
					except:
						print "parsing error"
		except:
			print "cannot open file " + sys.argv[1]

if __name__ == '__main__':
    main()


