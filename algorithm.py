control = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]

cnpInitial = '196062120'
cnp = '196062120'
password3 = cnp[5] + cnp[6] + '-' + cnp[3] + cnp[4] + '-' + '1' + '9' + cnp[1] + cnp[2]

last = 0

for a in range(0, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            cnp += (str(a) + str(b) + str(c))
            cnpInt = [int(i) for i in cnp]

            for z in range(0, 12):
                last += cnpInt[z] * control[z]

            if last % 11 == 10:
                last = 1
            else:
                last = last % 11
            cnp += str(last)

            print cnp

            cnp = cnpInitial
            last = 0
