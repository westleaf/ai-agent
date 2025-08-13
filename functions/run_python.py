import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
  abs_working_dir = os.path.abspath(working_directory)
  target_file=os.path.abspath(os.path.join(working_directory, file_path))

  if not target_file.startswith(abs_working_dir):
    return f"Error: Cannot write to \"{file_path}\" as it is outside the permitted working directory"

  if not os.path.exists(target_file):
    return f"Error: File \"{target_file}\" not found"

  if not target_file.endswith(".py"):
    return f"Error: \"{file_path}\" is not a Python file."

  try:
    completed = subprocess.run(
      ["python3", target_file] + args,
      capture_output=True,
      text=True,
      timeout=30
    )
    returncode=""
    output=""
    if not completed.stdout:
      output += f"No output produced"
    else:
      output += completed.stdout
    if completed.returncode != 0:
      returncode += f", Process exited with code {completed.returncode}"
    return f"STDOUT:{output}, STDERR: {completed.stderr}{returncode}"
  except Exception as e:
    return f"Error: executing Python file: {e}"
