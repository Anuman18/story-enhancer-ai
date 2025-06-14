def change_tone(text, to_formal=True):
    if to_formal:
        return text.replace("wanna", "want to").replace("gonna", "going to").replace("u", "you")
    else:
        return text.replace("you", "u").replace("do not", "don't").replace("will not", "won't")
