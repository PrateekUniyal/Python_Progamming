def accum(st):
    index = 0
    s = []

    for i in st:
        patch = ""
        print(f"The current element index is {index} the element is {i} should be printed {index + 1} times")
        for j in range(index + 1):
            patch = patch + i
        print(f"The current patch is: {patch}")
        if patch.isupper():
            patch_final = patch[0] + patch[1:].lower()
            s.append(patch_final)
        else:
            patch_final = patch[0].upper()+patch[1:]
            s.append(patch_final)
        index += 1
    return ("-".join(s))


st = input("Please enter the string to mumble: ")
print(accum(st))