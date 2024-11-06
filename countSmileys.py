def count_smileys(arr):
    count = 0
    for face in arr:
            if len(face) == 2:
                if face[0] == ':' or face[0] == ";":
                    print(face[0])
                    if face[1] == '-'or face[1] == "~" or face[1] == ")" or face[1] == "D":
                        print(face[1])
                        count += 1
            elif len(face) == 3:
                if face[0] == ':' or face[0] == ";":
                    print(face[0])
                    if face[1] == '-'or face[1] == "~":
                        print(face[1])
                        if face[2] == ")" or face[2] == "D":
                            print(face[2])
                            count += 1
    return count

arr = [':D',':~)',';~D',':)']
print(f"The number of smiling faces in the provided test case is {count_smileys(arr)}.")