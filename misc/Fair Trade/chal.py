print('Welcome to my Environment')

while True:
    a=input('>>> ')
    try:
        print(exec(a))
    except:
        print('BAD '*20)
        exit()