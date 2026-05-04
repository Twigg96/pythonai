from google.genai import types
from functions import write_file
from functions import run_python_file
from functions import get_file_content
from functions import get_files_info
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file

available_functions = types.Tool(
    function_declarations=[schema_get_files_info, schema_write_file, schema_run_python_file, schema_get_file_content],
)

def call_function(function_call, verbose=False):
    if verbose is not None:
        print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print(f" - Calling function: {function_call.name}")

    function_map = {
              "get_file_content": get_file_content,
              "write_file":write_file,
              "get_files_info":get_files_info,
              "run_python_file":run_python_file
              }
    function_name = function_call.name or ""

    if function_name not in function_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                name=function_name,
                response={"error": f"Unknown function: {function_name}"},
        )
    ],
)

    args = dict(function_call.args) if function_call.args else {}
    args["working_directory"]="./calculator/"
    return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"result": function_result},
                    )
                ],
            )


