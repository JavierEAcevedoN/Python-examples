def mat_design(height: int, length: int) -> None:
    pattern = '.|.'
    message = 'WELCOME'
    if height%2 == 0 or length != 3 * height:
        return
    for i in range(height // 2):
        print(f'{(1 + (i * 2)) * pattern:-^{length}}')
    print(f'{message:-^{length}}')
    for i in range(height // 2, 0, -1):
        print(f'{((i * 2) - 1) * pattern:-^{length}}')
input_data = input().split()
mat_design(*map(int, input_data))