## get_all_image.py
#### Modules
 - pyodbc==4.0.23
#### Features
 - Access the SQL Server database through the module 'pyodbc'
 - Make the responding directory
 - Get and write the binary code, turning back into files stored in the responding directory

## grabEntityFilesAndCallApis/*
#### Modules
 - pyodbc==4.0.23
 - requests==2.19.1
#### Features
 - Utilize the external configuration file (config.ini)
 - Grab the conf.ini info by built-in module 'configparser' (*.py)
 - Build the db connection (dbConnection.py)
 - Get the absolute path with the given relative path (filesFolderAccess.py)
 - Utilize 'os.walk(dir_path, topdown=True).__next__()' to get the first layer structure ('os.walk' return an iterator for directory tree including the subdirectory) (filesFolderAccess.py)
 - Call different APIs based on 'ENV' variable (apiRequest.py)
 - Dumps python data structure to json with Chinese output supported (apiRequest.py)
