while True:
    word = input()
    if word == 'SoftUni':
        continue
    elif word == 'End':
        break
    final_word = ""
    for i in word:
        final_word += i * 2
    print(final_word)