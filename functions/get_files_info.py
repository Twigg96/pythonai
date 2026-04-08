import os
def get_files_info(working_directory, directory="."):
    working_directory = os.path.abspath("/home/twigg/workspace/pythonai")
    target_dir = os.path.normpath(os.path.join(working_directory, directory))
    valid_target_dir = os.path.commonpath([working_directory, target_dir]) == working_directory:
    if valid_target_dir == False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if os.path.isdir(directory) == False:
        return f'Error: "{directory}" is not a directory'
