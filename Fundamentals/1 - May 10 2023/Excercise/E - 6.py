cycles = int(input())
symbols = [",", ".", "_"]

for i in range(cycles):
    word = input()
    for s in symbols:
        if s in word:
            print(f'{word} is not pure!')
            break
    else:
        print(f'{word} is pure.')

