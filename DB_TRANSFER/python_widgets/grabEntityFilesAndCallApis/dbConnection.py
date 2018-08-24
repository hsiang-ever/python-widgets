#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pyodbc
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def newDbConnection():
	driver = config['NEW_DB']['DRIVER']
	server_ip = config['NEW_DB']['SERVER_IP']
	database = config['NEW_DB']['DATABASE']
	username = config['NEW_DB']['USERNAME']
	password = config['NEW_DB']['PASSWORD']
	con = pyodbc.connect(driver=driver,server=server_ip,database=database,uid=username,pwd=password)
	return con

def oldDbConnection():
	driver = config['OLD_DB']['DRIVER']
	server_ip = config['OLD_DB']['SERVER_IP']
	database = config['OLD_DB']['DATABASE']
	username = config['OLD_DB']['USERNAME']
	password = config['OLD_DB']['PASSWORD']
	con = pyodbc.connect(driver=driver,server=server_ip,database=database,uid=username,pwd=password)
	return con