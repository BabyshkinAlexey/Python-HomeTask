def same_by(characteristics, objects):
    characteristics_list = [characteristics(x) for x in objects]
    for i in range(len(characteristics_list) - 1):
        if characteristics_list[i] != characteristics_list[i+1]:
            return False
    return True

values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print("same")
else:
    print("different")