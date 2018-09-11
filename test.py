# Write your function below!
def fizz_count(fizz_list):
    count = 0
    for x in fizz_list:
        if x == "fizz": count += 1
    else:
        if x != "fizz": count = 0
    return count

fizz_listing = ["fizz", "stupid", "fucking", "fizz"]
fizz_do = fizz_count(fizz_listing)
print(fizz_do)