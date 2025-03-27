text = "Good morning, Fellow classmates and beloved instructor."


print(text.startswith("Good morning"))
print(text.startswith("Python"))
print(text.startswith("Fellow", 14))
print(text.startswith(" ", 4))


print(text.endswith("classmates"))
print(text.endswith("instructor."))
print(text.endswith("instructor.", 33))
print(text.endswith("morning,", 12))