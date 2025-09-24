def run(intcolor: int) -> str:
    # TODO

    a=hex(intcolor)
    hexcolor=f"#{a[0:1]}{a[2:]}" 
    return hexcolor


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
