#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import json
import configparser
from apiRequest import callImportAddFolderApi, callImportAddFileApi

config = configparser.ConfigParser()
config.read('config.ini')

def getAbsDir(dir_path):
	path = config['ENTITY_FILES']['PATH']
	BASE_DIR = os.getcwd()
	for pathDir in path.split("/"):
		BASE_DIR = os.path.abspath(os.path.join(BASE_DIR, pathDir))
	for dirName in dir_path[1:].split("/"):
		BASE_DIR = os.path.abspath(os.path.join(BASE_DIR, dirName))
	print(BASE_DIR)
	return BASE_DIR

def importFilesAndSubfolderInFolder(dir_path, organization, folder_path):
	print('--------------------------------------------------------------')
	root, dirs, files = os.walk(dir_path, topdown=True).__next__()
	print("路徑：", root)
	print("目錄：", dirs)
	print("檔案：", files)
	for file in files:
		print()
		print('Insert File: ' + os.path.abspath(os.path.join(root, file)))
		payload = {
			'org': organization,
			'folder_path': folder_path,
			'file_name': file,
			'group_type': 'department'
		}
		print("path: " + os.path.abspath(os.path.join(root, file)))
		print("Req payload: " + json.dumps(payload, ensure_ascii=False))
		callImportAddFileApi(os.path.abspath(os.path.join(root, file)), payload)
	for one_dir in dirs:
		print()
		if one_dir == 'Forms':
			print('Ignore' + os.path.abspath(os.path.join(root, one_dir)) + ' Dir')
			continue
		print('Insert Folder: ' + os.path.abspath(os.path.join(root, one_dir)))
		payload = {
			'org': organization,
			'folder_name': one_dir,
			'folder_path': folder_path,
			'group_type': 'department'
		}
		print("path: " + os.path.abspath(os.path.join(root, one_dir)))
		print("Req payload: " + json.dumps(payload, ensure_ascii=False))
		new_folder_path = callImportAddFolderApi(payload)
		if new_folder_path == -1:
			print(os.path.abspath(os.path.join(root, one_dir)) + ' folder fail to create')
		else:
			print(os.path.abspath(os.path.join(root, one_dir)) + ' is created')
		print('new_folder_path: {}'.format(new_folder_path))
		importFilesAndSubfolderInFolder(os.path.abspath(os.path.join(root, one_dir)), organization, new_folder_path)
