import os
from config import *

def get_file_content(working_directory, file_path):
  abs_working_dir = os.path.abspath(working_directory)
  target_file=os.path.abspath(os.path.join(working_directory, file_path))
  if not target_file.startswith(abs_working_dir):
    return f"Error: Cannot read \"{file_path}\" as it is outside the permitted working directory"

  if not os.path.isfile(target_file):
    return f"Error: File not found or is not a regular file: \"{file_path}\""

  try:
    with open(target_file, "r") as f:
      file_content_string = f.read(FILE_CHARACTER_LIMIT)
      next_char = f.read(1)
      if next_char:
        file_content_string += f"[...File \"{target_file}\" truncated at 10000 characters]"
      return file_content_string
  except Exception as e:
    return f"Error: could not read file \"{e}\""
