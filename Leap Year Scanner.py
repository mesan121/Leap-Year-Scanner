print("Hello and welcome!")
print("")
print("This is completely for fun. So all you have to do is input a year and the program will say if it's a leap year or just any regular year.")
print("")

input_year = input("Input a year to check if it is a leap year: ")
input_year = int(input_year)

def leap_year(year):
  if year % 4 == 0:
    return (year, "is indeed a leap year")
  else:
    return (year, "is not a leap year")
print(leap_year(input_year))