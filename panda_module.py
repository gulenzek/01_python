# panda module kullanımı ile ilgili bir örnek..

import pandas
visitors = [1234, 3423, 3567, 2345, 6523]
errors = [12, 23, 34, 23, 79]
df = pandas.DataFrame({"visitors":visitors, "errors":errors}, index=["Mon", "Tues", "Wed", "Thu", "Fri"])
print(df)

print(df["errors"].median())
