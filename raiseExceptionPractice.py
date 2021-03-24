from timeit import timeit
# raising exceptions take longer and are more complicated
# try using if statements unless you really have to, this will save on performance in large scale applications.
code1 = """
def calculate_facter(age):
    if age <= 0:
        raise ValueError("Age cannont be 0 or less.")
    return 10/age


try:
    calculate_facter(-1)
except ValueError as error:
    pass
"""

code2 = """
def calculate_facter(age):
    if age <= 0:
        return None
    return 10/age



xfactor = calculate_facter(-1)
if xfactor == None:
    pass
"""
print(timeit(code1, number=10000))
print(timeit(code2, number=10000))
