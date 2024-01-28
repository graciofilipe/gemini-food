import os
import json


## list all files in a directory
def list_files(directory):
    for entry in os.listdir(directory):
        full_path = os.path.join(directory, entry)
        if os.path.isfile(full_path):
            yield full_path


## import json file as dictionary
def import_json(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


def singularize(noun):
  """Converts a noun to its singular form.

  Args:
    noun: The noun to singularize.

  Returns:
    The singular form of the noun.
  """

  # Check if the noun is a plural form that ends in "es".
  if noun[-2:] == "es":
    return noun[:-2]

  # Check if the noun is a plural form that ends in "ies".
  if noun[-3:] == "ies":
    return noun[:-3] + "y"

  # Check if the noun is a plural form that ends in "ves".
  if noun[-3:] == "ves":
    return noun[:-3] + "f"

  # Check if the noun is a plural form that ends in "oes".
  if noun[-3:] == "oes":
    return noun[:-3] + "o"

  # Check if the noun is a plural form that ends in "s".
  if noun[-1] == "s":
    return noun[:-1]

  # Otherwise, the noun is already singular.
  return noun

