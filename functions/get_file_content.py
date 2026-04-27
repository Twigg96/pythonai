import os
def get_file_content(working_directory, file_path):
    current = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(current, file_path))
    valid_target_dir = os.path.commonpath([current, target_dir]) == current
    if not valid_target_dir:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    if os.path.isdir(target_dir) == False:
        return f'Error: File not found or is not a regular file: "{file_path}"'
    max_chars = 10000
    with open(file_path, "r") as f:
        file_content_string = f.read(max_chars)
    try:
        if f.read(1):
            content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    except Exception as e:
        return f"Error: {str(e)}"


