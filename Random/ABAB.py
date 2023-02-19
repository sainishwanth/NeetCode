#    A
#    B
#    BA
#    BAB
#    BABBA
# Find for nth

Str = "A"
n = 10
for i in range(n):
    print(Str)
    if Str[-1] == "A":
        Str = Str[:-1]
        Str += "B"
    else:
        Str += "A"


print(Str)
