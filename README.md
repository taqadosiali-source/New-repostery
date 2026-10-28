def binary_translation(a, x):
    if x.lower() == "binary":
         binary = True
    else:
         binary = False
    if not binary:
            return ("the number transltes to {}").format(int(a, 2))
    if binary:
        return ("the number translates to {:b} in binary").format(int(a))
print(binary_translation("101", " not Binary"))
