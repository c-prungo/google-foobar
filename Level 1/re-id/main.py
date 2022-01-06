from solution import solution

def main():

    # test cases
    test_cases = {
        0: '23571',
        3: '71113',
        10000: '02192',
        435: '79119',
        1978: '33929',
        7777: '87157'
    }

    for case in test_cases:
        sol = solution(case)
        print(f"{case} -> {sol} : {sol == test_cases[case]}", )

if __name__ == "__main__":
    main()