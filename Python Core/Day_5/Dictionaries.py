
## Declaring dictionaries

student = {}

student = {
    "id":"S101",
    "name":"Rakesh",
    "gpa":3.8
}

point = dict(x=3,y=7)
# print(point)

subject_students = [("CS101", 45), ("MATH102", 30), ("PHY101", 25)]
enrollment = dict(subject_students)
# print(enrollment)


## Accessing Dictionaries
grades = {"Ram": 85, "Hari": 92, "Chandra": 78}

# 1. Direct access by key
print(grades["Ram"])  # 85

# 2. Safe access with .get()
print(grades.get("Hari"))        # None

# 3. Safe access with a default value
print(grades.get("Dev", 0))     # 0

# 4. Membership testing (checks KEYS, not values)
if "Bob" in grades:
    print("Bob is enrolled.")



## Nested Dictionary values
catalog = {
    "CS101": {
        "title": "Intro to Python",
        "credits": 3,
        "students": ["Ram", "Hari"]
    },
    "MATH201": {
        "title": "Linear Algebra",
        "credits": 4,
        "students": ["Chandra"]
    }
}
print(catalog["CS101"])



## Looping through Dicts:
wifi_signal = {
    "Library": 45,
    "Cafeteria": 62,
    "Lab-301": 50
}
# 1. Loop over keys (default behavior)
for location in wifi_signal:
    print(location)
# 2. Explicitly loop over keys
for location in wifi_signal.keys():
    print(location)
# 3. Loop over values only
for signal in wifi_signal.values():
    print(signal)

# 4. Loop over both keys and values (most common)
# Unpacking the tuple returned by .items()!
for location, signal in wifi_signal.items():
    print(f"{location}: {signal} dBm")

# 5. Building a new list from a dictionary
strong_zones = []
for loc, sig in wifi_signal.items():
    if sig > 55:
        strong_zones.append(loc)


## Updating dictionary values
inventory = {"apple": 30, "banana": 15}

# Overwriting value of an existing record
inventory["cherry"] = 50

# Adds new record (key and value) if not found in dict
inventory["apple"] = 15

# Using the update() method to change multiple items
inventory.update({"date": 10, "banana": 20})

# Removing a key
del inventory["apple"]


# Dict doesn't allow duplicate values
student = {
    "id" : 5,
    "name" : "May",
    "id" : 10,
}

print(student)
print(student["id"])

## Counter pattern in dictionary
word = "hello"
counts = {}
for ch in word:
    if ch in counts:
        counts[ch] += 1
    else:
        counts[ch] = 1
print(counts)

# Using get() method with default value
word = "hello"
counts = {}
for ch in word:
    counts[ch] = counts.get(ch, 0) + 1
print(counts)


## Grouping pattern
enrollments = [
    ("Alice", "CS101"),
    ("Bob", "CS102"),
    ("Carl", "CS101"),
    ("Dave", "CS103"),
    ("Ethan", "CS102")
    ]
groups = {}
for name, course in enrollments:
    if course not in groups:
        groups[course] = []
    groups[course].append(name)

print(groups)

## Exercises

# Making a dictionary out of word frequencies
def word_frequency(sentence):
    words = sentence.split()
    freq = {}
    
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    
    return freq
text = "the quick brown fox jumps over the lazy dog the"
print(word_frequency(text))


# Grouping words by their first letters
def group_by_letter(words):
    groups = {}
    
    for word in words:
        first = word[0]
        if first not in groups:
            groups[first] = []      
        groups[first].append(word)
    
    return groups

names = ["apple", "apricot", "banana", "cherry", "avocado", "blueberry"]
print(group_by_letter(names))


# Inverting a dictionary
def invert_dict(original):
    inverted = {}
    for key, value in original.items():
        inverted[value] = key
    return inverted
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
print(invert_dict(scores))


# Merging Dictionaries
def merge_sales(day1, day2):
    total = {}
    
    for product, count in day1.items():
        total[product] = count
    
    for product, count in day2.items():
        if product in total:
            total[product] += count
        else:
            total[product] = count
    
    return total

monday = {"apple": 30, "banana": 20}
tuesday = {"banana": 15, "cherry": 40}

print(merge_sales(monday, tuesday))


# Memoization
cache = {}
def factorial(n):
    if n in cache:
        return cache[n]
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    cache[n] = result
    return result

print(factorial(5))   
print(factorial(5))   
print(cache)