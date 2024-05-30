def reverse(self, x: int) -> int:
    # convert x to string 
    converted_num = str(x)

    if x < 0:
        # splice the negative sign and converts it to int 
        reverse_str = converted_num[1:][::-1]
        reverse_int = -int(reverse_str)
    else:
        reverse_str = converted_num[::-1]
        reverse_int = int(reverse_str)

    if reverse_int <= -2 ** 31 or reverse_int >= 2 ** 31 - 1: 
            print(0)
            return 0 

    print(reverse_int)
    return reverse_int



