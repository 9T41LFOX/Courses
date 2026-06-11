#
from datetime import date

# Using 2023 as a representative non-leap year
year = 2023

birthday = date(year, 7, 2)
christmas = date(year, 12, 25)

# 1. Days from your birthday (July 02) to Christmas (December 25) in the same year
days_same_year = (christmas - birthday).days

# 2. Days from Christmas (December 25) to your birthday (July 02) the next year
# (Using 2022 to 2023, both of which are non-leap years)
christmas_prior = date(2022, 12, 25)
days_next_year = (birthday - christmas_prior).days

print(f"Days from July 02 to December 25: {days_same_year} days")
print(f"Days from Christmas (Dec 25) to July 02 next year: {days_next_year} days")
