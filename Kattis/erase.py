n = int(input())
x = input()
y = input()

if n % 2 == 0:
    print('Deletion succeeded' if x == y else 'Deletion failed')
else:
    for i in range(len(x)):
        if (x[i] == y[i]):
            print('Deletion failed')
            quit()
    print('Deletion succeeded')
