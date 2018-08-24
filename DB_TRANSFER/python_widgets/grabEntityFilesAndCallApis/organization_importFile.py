#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import time, datetime
from dbConnection import newDbConnection, oldDbConnection
from filesFolderAccess import getAbsDir, importFilesAndSubfolderInFolder

start_time = time.time()

con = oldDbConnection()
cur = con.cursor()

db_cmd = "SELECT * FROM dbo.DocLib WHERE Site_Id=0 ORDER BY Site_Id, DocLib_Id"
cur.execute(db_cmd)

new_db_con = newDbConnection()
new_db_cur = new_db_con.cursor()

row = cur.fetchone()
while row is not None:
	select_cmd = "SELECT * FROM dbo.organization WHERE group_type='department' AND \
	title LIKE '%" + str(row.Title) + "'"
	new_db_cur.execute(select_cmd)
	new_db_row = new_db_cur.fetchone()
	dir_name = getAbsDir(row.URL)
	org = new_db_row.organization
	folder_path = (str)(new_db_row.folder_path) + '-' + (str)(new_db_row.sno)
	importFilesAndSubfolderInFolder(dir_name, org, folder_path)
	row = cur.fetchone()

print("Current time: {}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
print("--- {} seconds ---".format(time.time() - start_time))
print('--------------------------------------------------------------')


