men = {
    "Name" : "Rajalingam",
    "Age"  : 24,
    "Gender":"Male"
}

men2 = dict(name = "Manivel",Age= 28)

#
# print(men2["name"])
# print(type(men))
#
# print(len(men))
#
# print(men["Name"])

# Access items
print(men.get("Age"))


print(men.get("Name"))

name = men.get("Name")

print("Name is " + name)

print(men)



# print(name)

# list the keys and values

print(men.keys())
print('')
print(men.values())
print('')
print(men.items())

# verify a key exists
print("Name" in men)

# CHANGE THE VALUES
men["Name"] = "Lingam"
print(men["Name"])

print('')
men.update({"Own_House":"No","Own_Trans":"No"})
print(men)





