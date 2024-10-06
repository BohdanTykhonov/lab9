def create_file_tf20_1():
    content = """Систематизація знань дозволяє підвищити продуктивність та ефективність.
    Автоматизовані процеси сприяють оптимізації виробництва і підвищенню якості продуктів.
    Інтеграція технологій дозволяє масштабувати рішення і зменшити витрати.
    Розробники постійно працюють над вдосконаленням систем, підвищуючи їхню надійність.
    Систематизація знань дозволяє підвищити продуктивність та ефективність.
    Автоматизовані процеси сприяють оптимізації виробництва і підвищенню якості продуктів.
    Інтеграція технологій дозволяє масштабувати рішення і зменшити витрати.
    Розробники постійно працюють над вдосконаленням систем, підвищуючи їхню надійність."""

    with open("TF20_1.txt", "w", encoding="utf-8") as f:
        f.write(content)

def find_longest_words():
    with open("TF20_1.txt", "r", encoding="utf-8") as f:
        content = f.read()

    import string
    translator = str.maketrans("", "", string.punctuation)
    words = content.translate(translator).split()

    max_length = max(len(word) for word in words)

    longest_words = [word for word in words if len(word) == max_length]

    with open("TF20_2.txt", "w", encoding="utf-8") as f:
        f.write(" ".join(longest_words))


def print_words_from_tf20_2():
    with open("TF20_2.txt", "r", encoding="utf-8") as f:
        words = f.read().split()

    for i in range(0, len(words), 5):
        print(" ".join(words[i:i + 5]))


create_file_tf20_1()
find_longest_words()
print_words_from_tf20_2()
