def main():
  name = "Professor Nedd"
  print("This Will be a way for you to introduce yourself to me!")
  print("what is your name?")
  UsersName = input()
  print("what college did you attend?")
  University = input()
  print("what High School did you attend")
  School = input()
  print("Great! You said {}?".format(School))
  print("do you like high school or college more?")
  HighSchoolOrCollege = input()
  print("Thanks for the information! today i learned that you went to {}".format(University))
  print("i also learned that you attended {}".format(School))
  print("Lastly i learned that you said you liked {} the most".format(HighSchoolOrCollege))

if __name__ == "__main__":
  main()
