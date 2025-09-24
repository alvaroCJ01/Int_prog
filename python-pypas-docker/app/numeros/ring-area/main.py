def run(z: float) -> float:
    # TODO
    import math
    pi = round(math.pi,2)
    aext = pi * ((3 * z) / 2 ) ** 2
    aint = pi * ( z / 2 ) ** 2
    area = aext - aint
    gray_area = round(area,2)
    return gray_area


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
