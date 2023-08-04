
with open("books/frankenstein.txt") as f:

    file_content = f.read()

    total_words = file_content.split()

    letter_count = { "a": 0 }

    for word in total_words:
        for i in word:
            lower_case_letter = i.lower()
            if lower_case_letter in letter_count:
                letter_count[lower_case_letter] += 1
            else:
                letter_count[lower_case_letter] = 1

    print("--- An analysis of Frankenstein's text ---")
    print(f"There are {len(total_words)} in Frankenstein")
    for letter in letter_count:
        print(f"The letter {letter} was found {letter_count[letter]} times")
    print("--- End of report ---")