def raise_to_power (num, power):
    result = 1
    for i in range(power):
        result = result * num
    return result

print("2^3:", raise_to_power(2, 3))
