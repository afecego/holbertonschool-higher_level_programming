def islower(c):
    for i in range(65, 123):
        if (ord(c) > 96 and ord(c) < 123):
            return True
        else:
            return False
