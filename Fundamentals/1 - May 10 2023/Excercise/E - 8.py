final_points = 0
lower_list = ["coding", "cat", "dog", "movie"]
upper_list = ["CODING", "CAT", "DOG", "MOVIE"]

while True:
    event = input()
    if event == "END":
        print(final_points)
        break
    if event in lower_list:
        final_points += 1
    if event in upper_list:
        final_points += 2
    if final_points > 5:
        print("You need extra sleep")
        break
