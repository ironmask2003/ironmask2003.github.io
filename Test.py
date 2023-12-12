import main as m

# Test

class color:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"

def print_test_passed(user_result_1, user_result_2, result_1, result_2):
    print(color.BOLD + color.PURPLE + "------------------------------------------------------------------------------------------------------------------------------------")
    print(color.BOLD + color.GREEN + "Your result " + str(user_result_1) + " == " + color.BOLD + color.GREEN + "Correct Result " + str(result_1))
    print(color.BOLD + color.GREEN + "Your result " + str(user_result_2) + " == " + color.BOLD + color.GREEN + "Correct Result " + str(result_2))
    print(color.BOLD + color.PURPLE + "------------------------------------------------------------------------------------------------------------------------------------")
    print(color.BOLD + color.GREEN + "Test Passed")
    return

def print_test_error(user_result_1, user_result_2, result_1, result_2):
    print(color.BOLD + color.PURPLE + "------------------------------------------------------------------------------------------------------------------------------------")
    print(color.BOLD + color.RED + "Your result " + str(user_result_1) + " != " + color.BOLD + color.GREEN + "Correct Result " + str(result_1))
    print(color.BOLD + color.RED + "Your result " + str(user_result_2) + " != " + color.BOLD + color.GREEN + "Correct Result " + str(result_2))
    print(color.BOLD + color.PURPLE + "------------------------------------------------------------------------------------------------------------------------------------")
    print(color.BOLD + color.RED + "Test ERROR")
    return

# Test 1
################################################################
def Test_1():
    r = "A,B,C,D,E,G,H"
    global R 
    R = r.split(",")
    F = [(["A", "B"], ["C", "D"]), (["E", "H"], "D"), ("D", "H")]
    K = [["A", "B", "E", "G"]]
    chiusura_K, keys = m.prova(R, F, K)
    if test_equal_test_1(chiusura_K, keys): print_test_passed(chiusura_K, keys, [R], [["A", "B", "E", "G"]])
    else: print_test_error(chiusura_K, keys, [R], [["A", "B", "E", "G"]])
    return 

def test_equal_test_1(chiusura_K: list, keys: list) -> bool:
    if sorted(chiusura_K) == [R] and keys == [["A", "B", "E", "G"]] : return True
    return False

# Test 2
################################################################
def Test_2():
    r = "A,B,C,D,E"
    global R
    R = r.split(",")
    F = [(["A", "B"], "C"), (["A", "C"], "B"), ("D", "E")]
    K = [["A", "B", "D"], ["A", "C", "D"]]
    chiusura_K, keys = m.prova(R, F, K)
    if test_equal_test_2(chiusura_K, keys): print_test_passed(chiusura_K, keys, [[R], [R]], [["A", "B", "D"], ["A", "C", "D"]])
    else: print_test_error(chiusura_K, keys, [[R], [R]], [["A", "B", "D"], ["A", "C", "D"]])
    return

def test_equal_test_2(chiusura_K: list, keys: list) -> bool:
    if sorted(chiusura_K) == [[R], [R]] and keys == [["A", "B", "D"], ["A", "C", "D"]]: return True
    return False

print("\n")
Test_1()
Test_2()
print("\n")