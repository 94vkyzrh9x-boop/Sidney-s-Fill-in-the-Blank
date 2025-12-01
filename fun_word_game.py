# fun word game- create silly combinations of words!
""" Author: Sidney Brann
Title: Fill In The Blank"""
STORY = (
    "Hello %s, welcome to %sville! Here, the weather is always %s and the people are %s. "
    "Don't forget to visit the %s and try the %s! The happy %s of %s always have a %s on their face, "
    "and soon, you will too! Step right up at the %s store and see all they have to offer. "
    "On your way home, stop in at Mt.%s and wave goodbye! We hope we see you soon!"
)


def main():
    print("Welcome to Sidney's Fill in The Blank Game! Prepare to laugh...")
    input("Press Enter to begin!")

    prompts = [
        ("name", "Enter a name: "),
        ("town", "Enter an object: "),
        ("weather", "Enter an adjective (e.g. happy): "),
        ("people", "Enter a plural noun: "),
        ("attraction", "Enter a place to visit (e.g. park): "),
        ("food", "Enter a food or treat: "),
        ("group", "Enter a plural group (e.g. residents): "),
        ("place", "Enter a place or region name: "),
        ("face_thing", "Enter something on a face (e.g. smile): "),
        ("store", "Enter a store type (e.g. candy): "),
        ("mountain", "Enter a mountain name (without 'Mt.'): "),
    ]

    answers = []
    for key, prompt in prompts:
        ans = input(prompt).strip()
        if ans == "":
            ans = "[unknown]"
        answers.append(ans)

    story_text = STORY % tuple(answers)
    print("\nHere's your story:\n")
    print(story_text)


if __name__ == "__main__":
    main()
