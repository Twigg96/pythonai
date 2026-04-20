import os
def get_files_info(working_directory, directory="."):
    lines= []
    current = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(current, directory))
    valid_target_dir = os.path.commonpath([current, target_dir]) == current
    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if os.path.isdir(target_dir) == False:
        return f'Error: "{directory}" is not a directory'
    try:
        for item in os.listdir(target_dir):
            full_path = os.path.join(target_dir, item)
            file_size = os.path.getsize(full_path)
            is_dir = os.path.isdir(full_path)
            lines.append(f"- {item}: file_size={file_size} bytes, is_dir={is_dir}")
        return "\n".join(lines)
    except Exception as e:
        return f"Error: {str(e)}"
