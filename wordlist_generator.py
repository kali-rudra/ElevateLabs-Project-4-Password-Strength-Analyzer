MAX_CANDIDATES = 10_000

SUFFIX_OPTIONS = {
    "1": "!",
    "2": "@",
    "3": "#",
    "4": "123",
    "5": "123!",
    "6": "!123",
}


def read_items(prompt):
    """Read comma-separated inputs and remove duplicates."""
    raw = input(prompt).strip()

    return list(dict.fromkeys(
        item.strip()
        for item in raw.split(",")
        if item.strip()
    ))

def case_variants(word):
    """Return common case variations without duplicates."""
    return list(dict.fromkeys([
        word,
        word.lower(),
        word.upper(),
        word.title(),
    ]))

LEET_MAP = {
    "a": "4",
    "e": "3",
    "i": "1",
    "o": "0",
    "s": "$",
    "t": "7",
}


def leet_variants(word):
    """Return limited leetspeak variants."""
    variants = []

    for index, character in enumerate(word):
        replacement = LEET_MAP.get(character.lower())

        if replacement:
            variants.append(
                word[:index] + replacement + word[index + 1:]
            )

    fully_converted = "".join(
        LEET_MAP.get(character.lower(), character)
        for character in word
    )

    if fully_converted != word:
        variants.append(fully_converted)

    return list(dict.fromkeys(variants))


def build_candidates(words, years, suffixes, use_leet):
    """Build unique candidates, stopping at the configured limit."""
    candidates = []
    seen = set()
    truncated = False

    def add(candidate):
        nonlocal truncated

        if candidate in seen:
            return True

        if len(candidates) >= MAX_CANDIDATES:
            truncated = True
            return False

        seen.add(candidate)
        candidates.append(candidate)
        return True

    for word in words:
        bases = case_variants(word)

        if use_leet:
            for variant in leet_variants(word):
                bases.extend(case_variants(variant))

        bases = list(dict.fromkeys(bases))

        for base in bases:
            if not add(base):
                return candidates, True

            for suffix in suffixes:
                if not add(base + suffix):
                    return candidates, True

            for year in years:
                if not add(base + year):
                    return candidates, True

                for suffix in suffixes:
                    if not add(base + suffix + year):
                        return candidates, True

    return candidates, truncated

def generate_wordlist():
    """Collect inputs and generate custom wordlist candidates."""
    words = read_items(
        "Enter names or words (comma-separated): "
    )

    if not words:
        print("At least one word is required.")
        return

    years = read_items(
        "Enter years (comma-separated, or press Enter to skip): "
    )

    print("\nChoose suffixes:")
    for key, suffix in SUFFIX_OPTIONS.items():
        print(f"{key}. {suffix}")

    print("0. No suffixes")

    while True:
        choices = read_items(
            "Enter choices separated by commas (e.g. 1,4), or 0: "
        )

        if choices == ["0"] or (
            choices and all(choice in SUFFIX_OPTIONS for choice in choices)
        ):
            break

        print("Enter valid input.")

        print("\nChoose suffixes:")
        for key, suffix in SUFFIX_OPTIONS.items():
            print(f"{key}. {suffix}")
        print("0. No suffixes")

    if choices == ["0"]:
        suffixes = []
    else:
        suffixes = [
            SUFFIX_OPTIONS[choice]
            for choice in choices
        ]

    leet_answer = input(
        "Include limited leetspeak variants? (y/n): "
    ).strip().lower()

    use_leet = leet_answer == "y"
    candidates, truncated = build_candidates(
        words, years, suffixes, use_leet
    )

    if not candidates:
        print("No candidates were generated.")
        return

    print(f"\nGenerated {len(candidates)} unique candidates.")

    if truncated:
        print(f"Warning: Generation stopped at {MAX_CANDIDATES} candidates.")

    output_path = input(
        "Output filename (default: custom_wordlist.txt): "
    ).strip()

    if not output_path:
        output_path = "custom_wordlist.txt"

    import os

    if os.path.exists(output_path):
        confirm = input(
            "File already exists. Overwrite it? (y/n): "
        ).strip().lower()

        if confirm != "y":
            print("Export cancelled.")
            return

    try:
        with open(output_path, "w", encoding="utf-8") as file:
            file.write("\n".join(candidates) + "\n")

        print(f"Wordlist saved to: {output_path}")

    except OSError as error:
        print(f"Could not save the wordlist: {error}")
