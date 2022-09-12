# import persinator
# from persinator.person_generator import PersonGenerator
from persinator import PersonGenerator


def main():
  pg = PersonGenerator()
  persons = pg.get_persons()
  print(persons)

if __name__ == '__main__':
  main()