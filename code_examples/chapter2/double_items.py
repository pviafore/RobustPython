def double_value(value):
    return value + value

assert double_value(5) == 10
assert double_value("abc") == "abcabc"
assert double_value([1,2,3]) == [1,2,3,1,2,3]
