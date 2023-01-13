__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import zipfile
import os

# create path
current_directory = os.getcwd() #os.curdir
#path = r"C:\Winc\files\cache"
path = os.path.join(current_directory, 'cache')

# clean_cache: takes no arguments and creates an empty folder named cache in the current directory. 
# If it already exists, it deletes everything in the cache folder.
def clean_cache():   
    exist = os.path.exists(path)
    if exist != True:
        # create new folder
        os.mkdir(path)
    else:
        # get all files in folder
        for file in os.listdir(path):
            #print(file)
            file_path = os.path.join(path, file)
            #print(file_path)

            # delete file
            os.remove(file_path)
            #print("file deleted")
    return
clean_cache()

# cache_zip: takes a zip file path (str) and a cache dir path (str) as arguments, in that order. 
# The function then unpacks the indicated zip file into a clean cache folder.
def cache_zip(zip_file_path,cache_dir_path):
    # first get an empty cache folder
    clean_cache()
    
    # get zip
    with zipfile.ZipFile(zip_file_path, 'r') as zObject:
        # extract files
        zObject.extractall(path=cache_dir_path)

cache_zip(r"C:\Winc\files\data.zip",r"C:\Winc\cache")

# cached_files: takes no arguments and returns a list of all the files in the cache. 
# The file paths should be specified in absolute terms. 
# Search the web for what this means! No folders should be included in the list. 
# You do not have to account for files within folders within the cache directory.

def cached_files():
    # create new list
    all_files = []

    # get files in folder
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        # add to list
        all_files.append(file_path)
    return all_files

cached_files()

# find_password: takes the list of file paths from cached_files as an argument. 
# This function should read the text in each one to see if the password is in there. 
# Surely there should be a word in there to indicate the presence of the password? 
# Once found, find_password should return this password string

def find_password(file_paths):
    for x in file_paths:
        file = open(x)
        content = file.read()
        if content.find('password') != -1:
            part1 = content[content.find(':')+2:]
            password = part1[:part1.find("\n")]
            return password

print(find_password(cached_files()))
