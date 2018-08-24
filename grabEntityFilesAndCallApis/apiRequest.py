#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def callImportAddFolderApi(payload):
	ap_server_ip = config['AP_SERVER']['SERVER_IP']
	env = config['ENV']['VERSION']
	api = 'http://' + ap_server_ip + '/public/api/organization/import-add-folder'
	if env=='dev':
		r = requests.get(api, params=payload)
	else:
		auth_account = config['AP_SERVER']['AUTH_USER'], config['AP_SERVER']['AUTH_PWS']
		r = requests.get(api, params=payload, auth=auth_account)
	print("Response payload: " + r.text)
	if r.status_code == 200:
		jsonRes = json.loads(r.text)
		if jsonRes['code'] == 200:
			return jsonRes['payload']['new_folder_path']
		else:
			with open('FailImport.txt', 'a', encoding='utf8') as fi:
				fi.write(r.text)
				fi.write("\n")
				data = json.dumps(payload, ensure_ascii=False)
				fi.write(data)
				fi.write("\n-----------------------------------------------------------\n")
			return -1
	else:
		return -1

def callImportAddFileApi(filePath, payload):
	ap_server_ip = config['AP_SERVER']['SERVER_IP']
	env = config['ENV']['VERSION']
	api = 'http://' + ap_server_ip + '/public/api/organization/import-add'
	if env=='dev':
		r = requests.post(api, data=payload, files={'source_file': ('1', open(filePath, 'rb'))})
	else:
		auth_account = config['AP_SERVER']['AUTH_USER'], config['AP_SERVER']['AUTH_PWS']
		r = requests.post(api, data=payload, files={'source_file': ('1', open(filePath, 'rb'))}, auth=auth_account)
	print("Response payload: " + r.text)
	if r.status_code != 200:
		with open('debug.html', 'w') as f:
			f.write(r.text)
	else:
		jsonRes = json.loads(r.text)
		if jsonRes['code'] != 200:
			print(filePath + ' fail to insert')
			with open('FailImport.txt', 'a', encoding='utf8') as fi:
				fi.write(r.text)
				fi.write("\n")
				data = json.dumps(payload, ensure_ascii=False)
				fi.write(data)
				fi.write("\n-----------------------------------------------------------\n")
		elif jsonRes['code'] == 200:
			print(filePath + ' is inserted')