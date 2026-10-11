import random
import time

books = {
    "Fantasy": [
        "The Poppy War - R. F. Kuang",
        "Throne of Glass - Sarah J. Maas"
    ],
    "Mystery": [
        "A Good Girl's Guide to Murder - Holly Jackson",
        "And Then There Were None - Agatha Christie"
    ],
    "Science Fiction": [
        "Planet of the Apes - Pierre Boulle",
        "The Time Machine - H. G. Wells"
    ],
    "Horror": [
        "The Shining - Stephen King",
        "Pet Sematary - Stephen King"
    ],
    "Thriller": [
        "Misery - Stephen King",
        "Strange Pictures - Uketsu"
    ],
    "Psychology": [
        "Thinking, Fast and Slow - Daniel Kahneman",
        "The Man Who Mistook His Wife for a Hat - Oliver Sacks"
    ],
    "Classics": [
        "Pride and Prejudice - Jane Austen",
        "Crime and Punishment - Fyodor Dostoevsky"
    ]
}

print("Welcome to the Book Recommendation Program!")

while True:
    print("\nAvailable genres:")
    for genre in books:
        print("-", genre)

    choice = input("\nChoose a genre (or type 'q' to quit): ").strip().title()

    if choice == "Q":
        print("Thank you for using the program. Goodbye!")
        break

    if choice not in books:
        print("Invalid genre. Please choose from the list.")
        continue

    print("\nFinding a book for you...")
    time.sleep(1)

    recommended_book = random.choice(books[choice])
    print("Your recommended book is:", recommended_book)

    again = input("\nWould you like another recommendation? (yes/no): ").strip().lower()

    if again == "no":
        print("Happy reading! Goodbye!")
        break
    elif again == "yes":
        continue
    else:
        print("I did not understand your answer. Let's choose a genre again.")