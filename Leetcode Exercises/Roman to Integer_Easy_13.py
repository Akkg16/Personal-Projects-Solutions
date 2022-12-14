roman = str(input("Enter Roman number: "))
j = 0;
roman_list = list(roman)
print(roman_list)
int_number = []
for i in range(len(roman_list)):
    match roman_list[j]:
        case 'I':
            int_number.append('1')
        case 'X':
            int_number.append('10')         
        case 'V':
            int_number.append('5')  
        case 'L':
            int_number.append('50')
        case 'C':
            int_number.append('100')
        case 'D':
            int_number.append('500')         
        case 'M':
            int_number.append('1000')
    j = j + 1
S = 0
x = 0
print(int_number)
for i in range(len(int_number)):
    S = S + int(int_number[x])
    x = x + 1
print(S)