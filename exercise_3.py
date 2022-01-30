def letter_counter(s: str) -> dict[str, int]:
    s = s.lower()
    return {c: s.count(c) for c in s if c != " "}


inp = input("Enter a string: ")

print(letter_counter(inp))
