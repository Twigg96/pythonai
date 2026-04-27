import os
import subprocess
def run_python_file(working_directory, file_path, args=None):
    current = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(current, file_path))
    valid_target_dir = os.path.commonpath([current, target_dir]) == current
    if not valid_target_dir:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if  not os.path.isfile(target_dir):
        return f'Error: "{file_path}" does not exist or is not a regular file'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'
    try:
        command = ["python", target_dir]
        if args != None:
            command.extend(args)
        finished = subprocess.run(
                command,
                capture_output=True,
                cwd=current,
                text=True,
                timeout=30)
        output = []
        if finished.returncode !=0:
            output.append(f"Process exited with code {finished.returncode}")
        has_stdout = bool(finished.stdout.strip())
        has_stderr = bool(finished.stderr.strip())

        if not has_stdout and not has_stderr:
            output.append("No output produced")
        else:
            if has_stdout:
                output.append(f"STDOUT: {finished.stdout.strip()}")
            if has_stderr:
                output.append(f"STDERR: {finished.stderr.strip()}")

        return "\n".join(output)
                
    except Exception as e:
        return f"Error: executing Python file: {e}"
