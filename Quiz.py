questions = {
    "What is the capital of India?": "c",
    "Who discovered gravity?": "a",
    "Which language is used for AI?": "b"
}

options = [
    ["a) Mumbai", "b) Kolkata", "c) Delhi", "d) Chennai"],
    ["a) Newton", "b) Einstein", "c) Galileo", "d) Tesla"],
    ["a) HTML", "b) Python", "c) CSS", "d) Bootstrap"]
]

score = 0
qno = 0

for question in questions:
    print("\n" + question)
    for opt in options[qno]:
        print(opt)

    ans = input("Enter option (a/b/c/d): ").lower()

    if ans == questions[question]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

    qno += 1

print("\nYour Total Score:", score)
