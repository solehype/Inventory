'''
Removes duplicate rows by looping though a csv and 
saving a cell in a cache of the last row looped then checking 
the next row vs the cache continually.

Note: The duplicate column index & doc delimeter can be 
adjusted with variables.

Last Edit - 3/13/15
'''

import csv, re, time

#Returns current date str
def date():
	return time.strftime("%m-%d-%Y")

#CSV Delimeter 
delimiter = ','
#Index to search for duplicates in
duplicateIndex = 1

#open csv files
inputCSV = open('6pm-NewInventory-4-27-15.csv', 'rb')
reader = csv.reader(inputCSV, delimiter=delimiter)
outputCSV = open(time.strftime("%I.%M.%S")+'_NewInventoryCleaned_'+date()+'.csv', "wb")
writer = csv.writer(outputCSV, delimiter=delimiter)

#cache to store possible duplicate
cachedIndex = 'INIT-STRING'
#array to store rows to write
csvArray = []
#csv row count
loopCount = 1

#loop through csv rows
for csvRow in reader:

	#check for cache in row
	if cachedIndex in csvRow:
		print "Duplicate removed: "+csvRow[0]
		continue
	elif not cachedIndex in csvRow:
		#store csv row into array
		csvArray.append(csvRow)

	#Store duplicateIndex in cache
	cachedIndex = csvRow[duplicateIndex]


	
#write cleaned rows to new csv
for row in csvArray:
	writer.writerow(row)