#countries = ["America", "Canada", "Australia", "China", "Chile"]
#for c in countries:
#    if c.startswith("C"):
#        countries.remove(c)
#print(countries)

# Output: ['America', 'Australia', 'Chile']


countries = ["America", "Canada", "Australia", "China", "Chile"]
countries = [c for c in countries if not c.startswith("C")]
print(countries)

# Output: ['America', 'Australia']

"""
The key lesson: Never modify a list while iterating over it directly — 
iterate over a copy instead, or use alternatives like list comprehension.
"""