# 41-45
roy = [3, 6, 9]
print(list(filter(lambda x: x != 6, roy)))

roy = ["aa", "bbb", "cccc"]
print(list(filter(lambda x: len(x) >= 3, roy)))

roy = [50, 60, 70]
print(list(filter(lambda x: x > 55, roy)))

roy = ["python", "js"]
print(list(filter(lambda x: len(x) > 2, roy)))

roy = [2, 3, 4, 5]
print(list(filter(lambda x: x % 2 == 0, roy)))
