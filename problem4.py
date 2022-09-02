from tkinter.tix import Tree


def solve_problem4() -> int:
    palindrome_products = find_palindrome_products(999, 100)
    print(palindrome_products)
    return max(palindrome_products)

def find_palindrome_products(max_number: int, min_number: int) -> list:
    palindrome_products = list()
    for left in range(max_number, min_number, -1):
        for right in range(left, min_number, -1):
            product = left * right
            # print(f"{left} * {right} = {product}")
            mods = list()
            maxDigit = get_digit(product)

            mod = product 
            for digit in range(maxDigit, 0, -1):
                devider = 10 ** (digit -1 )
                digitNumber = mod // devider
                mods.append(digitNumber)
                mod = mod % devider

            if(is_palindrome_number(mods)):
                palindrome_products.append(product)
            else:
                continue
    return palindrome_products

def get_digit(number: int) -> int:
    """桁数を数えます

    Args:
        number (int): 求めたい数

    Returns:
        int: 桁数
    """
    digit = 1
    while(True):
        devider = 10 ** digit
        mod = number % devider
        if(mod == number):
            return digit
        else:
            digit+=1
            continue

def is_palindrome_number(number) -> bool:
    """回文数かどうか判定します。
    
    Args:
        number (_type_): 判定したい数

    Returns:
        bool: 回文数ならTrue
    """
    totalCheckTimes = len(number) // 2
    for index in range(0, totalCheckTimes, 1):
        if(number[index] != number[len(number) - 1 - index]):
            return False
    return True

if __name__ == "__main__":
    print(solve_problem4())