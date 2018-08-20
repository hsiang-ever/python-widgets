#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pyodbc
import os
import time, datetime
# record the processing time
start_time = time.time()
# Create connection
con = pyodbc.connect(driver="{SQL Server}",server="localhost",database="dename",uid="root",pwd="12346578")
cur = con.cursor()
db_cmd = "SELECT TOP (1000) LeafName,Content,DirName FROM dbo.Docs"
cur.execute(db_cmd)

def downloadImage(row):
	# Create dir by the 'DirName' in the table
	BASE_DIR = os.path.abspath(os.path.join(os.getcwd(), "TEST"))
	print('Object loc: {}'.format(BASE_DIR))
	for dirName in row.DirName.split("/"):
		BASE_DIR = os.path.abspath(os.path.join(BASE_DIR, dirName))
	print('BASE_DIR: {}'.format(BASE_DIR))
	if not os.path.isdir(BASE_DIR):
		os.makedirs(BASE_DIR)
	# Write image(binary) into the file and save it in the 'DirName'
	file = os.path.abspath(os.path.join(BASE_DIR, row.LeafName))
	print('file: {}'.format(file))
	with open(file, 'wb') as f:
		if row.Content:
			f.write(row.Content)
			# print(row.Content)
	print('{} is donwloaded'.format(file))

# count total content
total = 0
# count null content
cn = 0
# count non null content
cnn = 0

row = cur.fetchone()
while row is not None:
	total += 1
	if row.Content is None:
		cn += 1
	else:
		cnn += 1
		# Download the image(binary) to file
		downloadImage(row)
	print('Content null: {}'.format(cn))
	print('Content not null: {}'.format(cnn))
	print('Total filtered rows: {}'.format(total))
	print("Current time: {}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
	print("--- {} seconds ---".format(time.time() - start_time))
	print('--------------------------------------------------------------')
	# Get next row
	row = cur.fetchone()
