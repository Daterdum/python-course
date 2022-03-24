for letter in "Hello":
    print(letter)

print("\n")

###

for i in [1, 2, 3, 4, 5]:
    print(i)

print("\n")

###

for i in range(5):  # same as (0, 5, 1)
    print(i)

print("\n")

###

for i in range(5, 0, -1):  # (start, stop, step), step can be negative
    print(i)

print("\n")

###

for index, val in enumerate(["a", "b", "c", "d", "e"]):  #
    print(f"{index=}, {val=}")

print("\n")

###

# Doesn't print "Finished iteration"
for i in [1, 2, 3, 4, 5]:
    print(i)
    if i == 3:
        break

else:
    print("Finished iteration")

print("\n")

###

# Prints Finished iteration
for i in [1, 2, 3, 4, 5]:
    print(i)

else:
    print("Finished iteration")

print("\n")

###
# Skips 3
for i in [1, 2, 3, 4, 5]:
    if i == 3:
        continue

    print(i)
