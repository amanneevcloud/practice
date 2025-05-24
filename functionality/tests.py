digit = "23"
my_list = []
mapping = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

my_list = [mapping[d] for d in digit]

print_list = []

for c1 in my_list[0]:
    for c2 in my_list[1]:
        print_list.append(c1 + c2)

print(print_list)