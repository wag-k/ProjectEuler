def get_first_triangle_number_over_given_divisors(divisors_count: int) -> int:
    triangular_index = 0
    while(True):
        triangular_number = (triangular_index+1)*(triangular_index+2)//2
        current_divisors_count = get_triangular_number_divisors_count(triangular_index)
        # print(f"{triangular_number}:{current_divisors_count}")
        if(divisors_count <= current_divisors_count):
            return triangular_number
        triangular_index += 1

def get_triangular_number_divisors_count(triangular_number_index: int) -> int:
    """指定インデックス(0始まり)の三角数が持つ約数の個数を数えます

    Args:
        triangular_number_index (int): 三角数のインデックス

    Returns:
        int: 約数の個数
    """
    small_factor = triangular_number_index+1
    greater_factor = triangular_number_index+2
    if(small_factor % 2 == 0):
        small_factor //= 2
    else:
        greater_factor //= 2
    smaller_visiors_count = len([divisor for divisor in get_divisors_generator(small_factor)])
    greater_visiors_count = len([divisor for divisor in get_divisors_generator(greater_factor)])
    return smaller_visiors_count*greater_visiors_count

def get_divisors_generator(number: int) -> iter:
    """約数を取得します

    Args:
        number (int): 約数を知りたい数

    Returns:
        iter: 約数を小さい順に出力
    """
    for current_number in range(1, number+1):
        if(number%current_number == 0):
            yield current_number

def solve_priblem12():
    divisours_cnt = 500
    return get_first_triangle_number_over_given_divisors(divisours_cnt)

if __name__ == "__main__":
    print(solve_priblem12())