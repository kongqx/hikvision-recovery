import argparse

def rshift(val, n):
    return (val % 0x100000000) >> n

def char_shift(char):
    c = ord(char)
    shifts = {
        range(0, 51): 33,
        range(51, 53): 62,
        range(53, 55): 47,
        range(55, 57): 66
    }

    for r, value in shifts.items():
        if c in r:
            return chr(c + value)
    else:
        return char


def get_code(serial, year, month, day):
    serial = serial + year + month + day
    magic_number = sum(ord(char) * index ^ index for index, char in enumerate(serial, 1))
    magic_number *= 1751873395
    magic_number = rshift(magic_number, 0)
    recovery_code = ''.join(char_shift(digit) for digit in str(magic_word))

    return recovery_code


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generates recovery key for Hikvision cameras')
    parser.add_argument('serial', help='Camera Serial Number')
    parser.add_argument('year', help='4 digit year of current camera time')
    parser.add_argument('month', help='2 digit month of current camera time')
    parser.add_argument('day', help='2 digit day of current camera time')
    args = parser.parse_args()

    recovery_code = get_code(args.serial, args.year, args.month, args.day)
    print(recovery_code)