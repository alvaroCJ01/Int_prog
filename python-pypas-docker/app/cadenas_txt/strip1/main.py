def run(text: str) -> str:
    # TODO
    final=len(text)-1
    stext=f'{text[1:final]}'
    return stext


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
