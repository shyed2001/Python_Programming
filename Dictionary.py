students1={"Eric":14, "Bob":12, "Cris":15, "Todd":16}
print(""" students1={"Eric":14, "Bob":12, "Cris":15, "Todd":16} """)
print("""len(students1) = """, len(students1))

print(len(students1))

print("""students1.keys(), # which will show the keys of the dictionary
 = """, students1.keys())
print("""students1.values(), # which will show the values of the dictionary
 = """, students1.values())

students2={"Bric":24, "sob":32, "Cristen":25, "Lodd":26}
print(""" students2={"Bric":24, "sob":32, "Cristen":25, "Lodd":26} """)


print("""students1.update(students2) = """ , students1.update(students2))
print(students1.update(students2))