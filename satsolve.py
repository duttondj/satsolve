# Danny Dutton
# satsolve.py: This program takes in a CNF text file and determines a solution

import logic
import csv
import time

def is_int(string):
    ''' Check if a string consists of an integer'''
    try: 
        int(string)
        return True
    except ValueError:
        return False

def satsolve(filename, maxflips):
	''' Parse CNF formated text file and create clauses. Find the solution
		to the clauses and display it along with the number of flips needed
		by WalkSAT to determine that solution.'''
	clauses = []
	f = open(filename, 'rb')
	try:
		reader = csv.reader(f, delimiter=' ')
		for row in reader: 
			if row[0] == 'p':
				numliterals = int(row[2])
			if is_int(row[0]):
				while '' in row:	# remove any ''
					row.remove('')
				while '0' in row:	# remove '0'
					row.remove('0')
					
				# Convert row to integers once we've removed junk
				row = [int(i) for i in row]

				# Convert each literal to a clause of either itself or the negation
				for n,i in enumerate(row):
					if i < 0:
						row[n] = logic.expr('~' + "X" +str(-1*i))
					elif i > 0:
						row[n] = logic.expr("X" + str(i))
				
				# OR each literal clause together within the main clause
				clause = row[0]
				for n,i in enumerate(row):
					if n > 0:
						clause = clause | row[n]

				# Put all the clauses into a list for WalkSat
				clauses.append(clause)

		# Start the clock
		start = time.clock()

		# Get the result and stats
		(result, bestflips, besttry) = logic.WalkSAT(clauses, 0.5, maxflips)

		# Stop the clock
		end = time.clock()

		#Need to convert the literal to an actual string before sort.
		kv = []
		for key,value in result.items():
			kv.append([str(key), value])

		# Sort the result by literal number
		sortkv = sorted(kv, key=lambda tup: tup[0])
		
		# Create string of 0s and 1s
		resultstr = ''
		for key,value in sortkv:
			if value == True:
				resultstr = resultstr + '1'
			elif value == False:
				resultstr = resultstr + '0'

		# Display the solution and flips needed based
		if besttry == 1:
			print("Solution not found")
			print("Best solution found: \t\t" + resultstr)
			print("Flips needed to find solution: \t" + str(bestflips))
			print("Time to find solution (s): \t" + str(end-start))
		elif besttry == 0:
			print("Solution found: \t\t" + resultstr)
			print("Flips needed to find solution: \t" + str(bestflips))
			print("Time to find solution (s): \t" + str(end-start))

	finally:
		f.close()

if __name__ == "__main__":
	satsolve('testcase1.txt', 2000)