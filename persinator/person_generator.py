from json import load, dumps
from os import path
class PersonGenerator:
  '''
  Exposes 3 helpfull methods:
  => get_persons(ammount: int = 20) => returns ammount of persons
  => get_all() => get entire person_list
  => pp_persons(ammount: int = 5, indent: int = 2) => pretty-prints ammount of persons with given indentation.
  '''
  def __init__(self) -> None:
    this_dir, this_filename = path.split(__file__)
    data_path = path.join(this_dir, "data", "MOCK_DATA.json")
    with open(data_path) as mock_data:
      self.person_list = load(mock_data)
  
  def get_persons(self, ammount: int = 20):
    '''
    Returns the given ammount of persons.
    Must be an integer between 1-1000.
    '''
    if ammount > 0 and ammount <= 1000:
      return self.person_list[0:ammount]
    else: return self.person_list[0]

  def get_all(self):
    '''
    Returns all the persons in the mock_data.json (currently 1000).
    '''
    return self.person_list
  
  def pp_persons(self, ammount: int = 5, indent: int = 2):
    '''
    Pretty-Prints the ammount of persons given by the "ammount"-Argument.
    Optionally accepts a second arg for the indent-level.
    '''
    print(dumps(self.get_persons(ammount), indent=indent))
