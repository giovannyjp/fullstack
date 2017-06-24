# Renaming files 
file_name = "48test.jpg"
print(file_name)

# How to delete numbers from file name tag
file_name.translate(None, "0123456789")

print("Old name - " + file_name)
print("New name - " + file_name.translate(None, "0123456789"))