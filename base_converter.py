def hex_to_dec(n):
    return int(str(n), 16)

def dec_to_hex(n):
    return hex(n)[2:].upper()

def bin_to_hex(n):
    return hex(int(str(n), 2))[2:].upper()

def hex_to_bin(n):
    return bin(int(str(n), 16))[2:]

def dec_to_bin(n):
    return bin(n)[2:]

def bin_to_dec(n):
    return int(str(n), 2)


while True:
    sr = int(input("시작 진수(2 or 10 or 16):"))
    er = int(input("변환할 진수(2 or 10 or 16):"))
    obj = input("변환할 숫자:")

    if sr == 2:
        if er == 2:
            print("다른 진수를 골라주세요")
        elif er == 10:
            print(bin_to_dec(obj))
        elif er == 16:
            print(bin_to_hex(obj))

    elif sr == 10:
        if er == 2:
            print(dec_to_bin(int(obj)))
        elif er == 10:
            print("다른 진수를 골라주세요")
        elif er == 16:
            print(dec_to_hex(int(obj)))

    elif sr == 16:
        if er == 2:
            print(hex_to_bin(obj))
        elif er == 10:
            print(hex_to_dec(obj))
        elif er == 16:
            print("다른 진수를 골라주세요")      
