def run(n: int) -> int:
    # TODO
    n2 = str(n)*2
    n3 = str(n)*3
    result = n + int(n2) + int(n3)
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
