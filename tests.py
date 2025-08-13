# Not actual unittests as per the instructions on the assignment...

from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

def test_get_files_info():
  print("Results for current directory:")
  print(get_files_info("calculator", "."))

  print("Results for 'pkg' directory:")
  print(get_files_info("calculator", "pkg"))

  print("Results for '/bin' directory:")
  print(get_files_info("calculaot", "/bin"))

  print("Result for '../' directory:")
  print(get_files_info("calculator", "../"))

def test_get_file_content():
  print("Result for calculator, main.py:")
  print(get_file_content("calculator", "main.py"))

  print("Result for calculator, pkg/calculator.py:")
  print(get_file_content("calculator", "pkg/calculator.py"))

  print("Result for calculator, /bin/cat:")
  print(get_file_content("calculator", "/bin/cat"))

  print("Result for calculator, pkg/does_not_exists.py:")
  print(get_file_content("calculator", "pkg/does_not_exists.py"))

def test_write_file():
  print("Result for test one:")
  print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

  print("Result for test two:")
  print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolar sit amet"))

  print("Result for test three:")
  print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

def test_run_python_file():
  print(run_python_file("calculator", "main.py"))

  print(run_python_file("calculator", "main.py", ["3 + 5"]))

  print(run_python_file("calculator", "tests.py"))

  print(run_python_file("calculator", "../main.py"))

  print(run_python_file("calculator", "nonexistent.py"))

if __name__ == "__main__":
  #test_get_files_info()
  #test_get_file_content()
  #test_write_file()
  test_run_python_file()
