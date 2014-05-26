def stamps(pence):
    fives = pence / 5
    remainder_after_fives = pence % 5
    if remainder_after_fives == 0:
        twos = 0
        last_remainder = 0
    else:
        twos = remainder_after_fives / 2
        last_remainder = remainder_after_fives % 2

    return (fives, twos, last_remainder)
