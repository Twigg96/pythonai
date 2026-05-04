import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes to the given file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path","content"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="lists the path to the file",
            ),
            "content":types.Schema(
                type=types.Type.STRING,
                description="Content to write into the file"),

        },
    ),
)


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
