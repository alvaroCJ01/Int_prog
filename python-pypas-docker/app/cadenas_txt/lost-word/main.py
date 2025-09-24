def run(text: str, target_word: str, replace_word: str) -> str:
    # TODO
    mtext = text.replace(target_word,replace_word)

    return mtext


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
