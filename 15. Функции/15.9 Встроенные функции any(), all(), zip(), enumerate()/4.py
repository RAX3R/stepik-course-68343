print(all(map(lambda x: x.isdigit() and int(x) <= 255, input().split('.'))))
