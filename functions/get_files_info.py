import os
from google.genai import types

def get_files_info(working_directory, directory="."):
  full_path = os.path.join(working_directory, directory)
  target_dir = os.path.abspath(full_path)
  dir_content = []

  if not target_dir.startswith(os.path.abspath(working_directory)):
    return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory"

  if not os.path.exists(full_path):
    return f"Error: directory does not exist"

  if not os.path.isdir(full_path):
    return f"Error: \"{directory}\" is not a directory"

  try:
    for content in os.listdir(full_path):
      target_path=os.path.join(target_dir, content)
      file_size=os.path.getsize(target_path)
      is_dir=os.path.isdir(target_path)

      dir_content.append(f"- {content}: file_size={file_size} bytes, is_dir={is_dir}")
    return "\n".join(dir_content)
  except Exception as e:
    return f"Error listing directory: {e}"

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
