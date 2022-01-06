from solution import solution

def main():

    # test cases
    test_cases = [
        [[4, 30, 50], [12, 1]],
        [[4, 20, 38, 50], [20, 3]],
        [[4, 14], [20, 3]],
        [[1, 3], [4, 3]],
        [[1, 31, 51, 71, 91], [20, 1]],
        [[4, 9, 17, 31, 40], [4, 1]],
        [[4, 17, 50], [-1, -1]],
        [[5], [-1, -1]]
    ]

    for case in test_cases:
        sol = solution(case[0])
        print(f"{case[0]} -> {sol} : {sol == case[1]}")

if __name__ == "__main__":
    main()