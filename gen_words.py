from sys import argv
import random
import json


def main():
    with open(argv[1], "rw") as f:
        lines = f.readlines()
    results = []
    title = "Переклади слова рівня А1"
    while input("one more?:") == "y":
        line_to_remove = random.randint(0, len(lines))
        new_line = lines.pop(line_to_remove)
        eng_word = new_line.split(" : ")[0]
        uk_word = input("translate " + new_line.split(" : ")[1] + ":")
        results.append(
            {
                "q-en": eng_word,
                "a-uk": uk_word,
            }
        )
    chunk_size = 3
    results = [results[i : i + chunk_size] for i in range(0, len(results), chunk_size)]

    for i, r in enumerate(results):
        print({"title": f"{title} ч. {i}", "parts": r})


if __name__ == "__main__":
    main()
