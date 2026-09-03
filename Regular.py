import re

print("--Task 1--")

text = "Email:maksim@gmail.com"
pattern = r"\w+\@\w+\.\w+"

Email = re.findall(pattern, text)
print(Email)

print("--Task 2--")

number = "Number:123-456-7890"
pattern2 = r"\d{3}-\d{3}-\d{4}"

newNumber = re.findall(pattern2, number)
print(newNumber)

print("--Task 3--")

year = "Year:10.05.2006"
pattern3 = r"(\d{2})\.(\d{2})\.(\d{4})"

date = re.search(pattern3, year)

newDate = re.sub(pattern3, r"\3.\2.\1", year)

print(newDate)