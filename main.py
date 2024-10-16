def create_file_tf20_1():
    content = """Систематизація знань дозволяє підвищити продуктивність та ефективність.
    Автоматизовані процеси сприяють оптимізації виробництва і підвищенню якості продуктів.
    Інтеграція технологій дозволяє масштабувати рішення і зменшити витрати.
    Розробники постійно працюють над вдосконаленням систем, підвищуючи їхню надійність.
    Систематизація знань дозволяє підвищити продуктивність та ефективність.
    Автоматизовані процеси сприяють оптимізації виробництва і підвищенню якості продуктів.
    Інтеграція технологій дозволяє масштабувати рішення і зменшити витрати.
    Розробники постійно працюють над вдосконаленням систем, підвищуючи їхню надійність."""

    try:
        with open("TF20_1.txt", "w", encoding="utf-8") as f:
            f.write(content)
    except IOError:
        print("Помилка при створенні або записі файлу TF20_1.txt")


def find_longest_words():
    try:
        with open("TF20_1.txt", "r", encoding="utf-8") as f:
            content = f.read()
    except IOError:
        print("Помилка при відкритті файлу TF20_1.txt")
        return

    import string
    translator = str.maketrans("", "", string.punctuation)
    words = content.translate(translator).split()

    max_length = max(len(word) for word in words)

    longest_words = [word for word in words if len(word) == max_length]

    try:
        with open("TF20_2.txt", "w", encoding="utf-8") as f:
            f.write(" ".join(longest_words))
    except IOError:
        print("Помилка при створенні або записі файлу TF20_2.txt")


def print_words_from_tf20_2():
    try:
        with open("TF20_2.txt", "r", encoding="utf-8") as f:
            words = f.read().split()
    except IOError:
        print("Помилка при відкритті файлу TF20_2.txt")
        return

    for i in range(0, len(words), 5):
        print(" ".join(words[i:i + 5]))


create_file_tf20_1()
find_longest_words()
print_words_from_tf20_2()
