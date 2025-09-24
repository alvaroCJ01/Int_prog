def run(source_char: str, offset: int) -> str:
    # TODO
    num_char=ord(source_char)
    a=int(num_char)+offset
    target_char= chr(a)
    return target_char


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
