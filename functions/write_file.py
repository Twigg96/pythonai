import os
def write_file(working_directory, file_path, content):
    current = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(current, file_path))
    valid_target_dir = os.path.commonpath([current, target_dir]) == current
    if not valid_target_dir:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(target_dir):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    try:
        os.makedirs(os.path.dirname(target_dir), exist_ok=True)
        with open(target_dir, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {str(e)}"
