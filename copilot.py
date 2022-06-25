

# Given a function add, that takes in two numbers and outputs their sum, create a test function that will test the function add.
def add(a, b): 
    return a + b

# test the add function
def test_add():
    assert add(1, 2) == 3
    assert add(2, 3) == 5
    assert add(3, 4) == 7
    assert add(4, 5) == 9
    assert add(5, 6) == 11
    assert add(6, 7) == 13
    assert add(7, 8) == 15
    assert add(8, 9) == 17
    assert add(9, 10) == 19
    assert add(10, 11) == 21
    assert add(11, 12) == 23
    assert add(12, 13) == 25
    assert add(13, 14) == 27
    assert add(14, 15) == 29
    assert add(15, 16) == 31
    assert add(16, 17) == 33
    assert add(17, 18) == 35
    assert add(18, 19) == 37
    assert add(19, 20) == 39
    assert add(20, 21) == 41
    assert add(21, 22) == 43
    assert add(22, 23) == 45
    assert add(23, 24) == 47
    assert add(24, 25) == 49
    assert add(25, 26) == 51
    assert add(26, 27) == 53
    assert add(27, 28) == 55
    assert add(28, 29) == 57
    assert add(29, 30) == 59
    assert add(30, 31) == 61
    assert add(31, 32) == 63
    assert add(32, 33) == 65
    assert add(33, 34) == 67
    assert add(34, 35) == 69
    assert add(35, 36) == 71
    assert add(36, 37) == 73
    assert add(37, 38) == 75
    assert add(38, 39) == 77
    assert add(39, 40) == 79
    assert add(40, 41) == 81
    assert add(41, 42) == 83
    assert add(42, 43) == 85
    assert add(43, 44) == 87
    assert add(44, 45) == 89
    assert add(45, 46) == 91
    assert add(46, 47) == 93

# create a main function

def main():
    test_add()
    print("All tests passed!")

# run the main function
if __name__ == "__main__":
    main()