import os

def get_path():
    current_directory = os.getcwd()
    # return os.path.dirname(current_directory)
    return current_directory

def get_env_var(key):
    return os.getenv(get_path(), key)