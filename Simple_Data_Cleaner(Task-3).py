names = [" Alice ", "bob", " CHARLIE "]  # Raw user names

cleaned_names = []  # List to store cleaned names

# Cleaning each name
for name in names:
    name = name.strip()        # Remove extra spaces
    name = name.lower()        # Convert to lowercase
    cleaned_names.append(name)

# Printing results
print("Original Names List :", names)
print("Cleaned Names List  :", cleaned_names)
