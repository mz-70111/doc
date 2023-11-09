a = {'name': 'muoaz', 'age': 33}

my = {'y1': 'one', 'y2': 'tow', 'y3': 'three'}


def h(**y):
    for i, o in y.items():
        print(f"{i} : {o}")


h(**my)
