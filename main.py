def init():  # Initialization
    import random
    a = random.choice([
        "hypnosis", "baguette", "chandelier", "pharaoh", "kaleidoscope",
        "eccentric", "chimera", "photosynthesis", "hologram", "atmosphere",
        "millennium", "circumference", "electromagnetism", "archaeology",
        "zephyr", "raspberry", "obsidian", "thunderbolt", "perpendicular",
        "monolith", "labyrinth"
    ])  # From Internet
    return a


def check_win(d):  # Check if user wins
    if "_" not in d:
        return True
    else:
        return False


def play():
    while True:
        print("Let’s play hangman!")  # to get point
        
        ans = init()  # Initialization
        disp = ["_"] * len(ans)
        used = []
        lives = 6
        
        while (lives > 0) and (not check_win(disp)):  # Only loop when lives>0 and not win (before guessing)
            print(f"\n: {' '.join(disp)}")
            print(f"Lives left: {lives}")

            p = input("Guess a letter and ONLY ONE LETTER then press ENTER: ").strip().lower()  # Input
            if len(p) != 1 or not p.isalpha():  #check if input is single letter and is not special character.
                print("What did I say? GUESS ONLY ONE VALID LETTER!")
                continue
            used.append(p)  # Add to "used letter list"
            if p in ans:  # Check if letter is in answer word
                for i in range(len(ans)):
                    if ans[i] == p:
                        disp[i] = p
            else:
                lives -= 1
                print("Letter not found!")  # to get point

        user_win = check_win(disp)  #check if user win again (after guessing)

        if user_win:
            print("Victory!")
        else:
            print("Out of lives, game over! You loser!")  # to get point
        
        while True: # Dare user to play again.
            play_again = input(
                "Play again? (yes/no): ").strip().lower()  # to get point
            if play_again == "yes":
                break
            elif play_again == "no":
                print("EXITING...")  # End the game
                return
            else:
                print("Invalid input. Play again? (yes/no)")  # to get point

if __name__ == "__main__":
    play()
