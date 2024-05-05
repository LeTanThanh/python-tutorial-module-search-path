if __name__ == "__main__":
  # Introduction to Python module search path

  """
  When you import a module in a program:

  import module

  Python will search for the module.py file from the following sources:

  - The current folder from which the program executes.

  - A list of folders specified in the PYTHONPATH environment variable, if you set it before/

  - An installation-dependent list of folders that you configured when you installed Python.

  Python stores the resulting search path in the sys.path variable that comes from the sys module.

  The following program shows the current module search path:
  """

  import sys

  for path in sys.path:
    print(path)

  """
  To make sure Python can always find the module.py, you need to:

  - Place module.py in the folder where the program will execute.

  - Include the folder that contains the module.py in the PYTHONPATH environment variable.
  Or you can place the module.py in one of the folders included in the PYTHONPATH variable.

  - Place the module.py in one of the installation-dependent folders.
  """

  # Modifying the Python module search path at runtime

  """
  Python allows you to modify the module search path at runtime by modifying the sys.path variable.
  This allows you to store module files in any folder of your choice.

  Since the sys.path is a list, you can append a search-path to it.

  The following examples adds the d:\module to the search path and use the recruitment module stored in this folder:

  import sys

  sys.path.append("d:\modules)

  import recruitment

  recruitment.hire()
  """
