import dotenv
import os

def get_path():
    current_directory = os.getcwd()
    # return os.path.dirname(current_directory)
    return current_directory

def get_env_var(key):
    return dotenv.get_variable(get_path(), key)