print("str.isalpha")
text = "Sodonotfear"
print(text.isalpha())
text = "So do not fear"
print(text.isalpha())


print("str.isdigit")
text = "4110"
print(text.isdigit())
text = "41:10"
print(text.isdigit())


print("str.isalnum")
text = "Isaiah4110"
print(text.isalnum())
text = "Isaiah 41:10"
print(text.isalnum())


print("str.isspace")
text = " \t "
print(text.isspace())
text = "Isaiah 41:10 \n So do not fear, for I am with you"
print(text.isspace())