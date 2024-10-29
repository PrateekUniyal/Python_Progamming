def stolen_lunch(note):
    ans = ""
    for s in note:
        if s in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if s == '0':
                ans = ans + 'a'
            elif s == '1':
                ans = ans + 'b'
            elif s == '2':
                ans = ans + 'c'
            elif s == '3':
                ans = ans + 'd'
            elif s == '4':
                ans = ans + 'e'
            elif s == '5':
                ans = ans + 'f'
            elif s == '6':
                ans = ans + 'g'
            elif s == '7':
                ans = ans + 'h'
            elif s == '8':
                ans = ans + 'i'
            elif s == '9':
                ans = ans + 'j'

        elif s in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']:
            if s == 'a':
                ans = ans + '0'
            elif s == 'b':
                ans = ans + '1'
            elif s == 'c':
                ans = ans + '2'
            elif s == 'd':
                ans = ans + '3'
            elif s == 'e':
                ans = ans + '4'
            elif s == 'f':
                ans = ans + '5'
            elif s == 'g':
                ans = ans + '6'
            elif s == 'h':
                ans = ans + '7'
            elif s == 'i':
                ans = ans + '8'
            elif s == 'j':
                ans = ans + '9'

        else:
            ans = ans + s

    return ans

note =input("PLease enter your note: ")
print(f"The encoded message genrated is : {stolen_lunch(note)}")