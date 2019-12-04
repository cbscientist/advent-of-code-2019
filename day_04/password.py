import re
# input range 145852-616942
def is_six_digits(password):
    if len(password) == 6:
        return True
    else:
        return False


def has_two_duplicate_digits(password):
    two_of_a_kind = re.findall('(\d)\\1{1}', password)
    three_of_a_kind = re.findall('(\d)\\1{2}', password)
    if len(set(two_of_a_kind) - set(three_of_a_kind)) > 0:
        return True

    else:
        return False

def is_always_increasing(password):
    if password[0] <= password[1] <= password[2] <= password[3] <= password[4] <= password[5]:
        return True
    else:
        return False


if __name__=="__main__":
    count = 0
    for password in range(145852,616942+1,1):
        password = str(password)
        if is_six_digits(password) and has_two_duplicate_digits(password) and is_always_increasing(password):
            count += 1
        else:
            pass

    print("This is the number of matching passwords: {}".format(count))


