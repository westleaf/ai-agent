# Not actual unittests as per the instructions on the assignment...

from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

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
  #print("Result for calculator lipsum.txt:")
  #print(get_file_content("calculator", "lipsum.txt"))

  print("Result for calculator, main.py:")
  print(get_file_content("calculator", "main.py"))

  print("Result for calculator, pkg/calculator.py:")
  print(get_file_content("calculator", "pkg/calculator.py"))

  print("Result for calculator, /bin/cat:")
  print(get_file_content("calculator", "/bin/cat"))

  print("Result for calculator, pkg/does_not_exists.py:")
  print(get_file_content("calculator", "pkg/does_not_exists.py"))

if __name__ == "__main__":
  #test_get_files_info()
  test_get_file_content()
