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

## auto_clockin_periodically.py
#### Environment & Requirements
 - OS: Windows 10
 - Driver: [ChromeDriver 2.41](https://sites.google.com/a/chromium.org/chromedriver/downloads) (e.g. "chromedriver.exe")
#### Modules
 - selenium==3.14.0 ([Intro](https://selenium-python.readthedocs.io/index.html))
 - schedule==0.5.0 ([Intro](https://schedule.readthedocs.io/en/stable/))
#### Features
 - Open browser, go to specific website, login in, and clock in automatically (**selenium**)
 - Schedule the above automation task (**schedule**)
