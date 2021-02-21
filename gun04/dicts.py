car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x)

dictionary = {'george': 16, 'amber': 19, 'zeki': 16}
search_age = input("Provide age")
for name, age in dictionary.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
    if age == search_age:
        print(name)