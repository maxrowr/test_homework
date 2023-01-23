def cat_in_hats(cats: int, laps: int) -> list:
    
    hat_state = [False for i in range(cats)]
    for i in range(1, laps+1):
        for j in range(i, cats+1, i):
            hat_state[j-1] = not hat_state[j-1]

    hat_cats = []
    for i in range(cats):
        if hat_state[i]:
            hat_cats.append(i+1)
    return hat_cats

print(cat_in_hats(100, 100))