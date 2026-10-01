import random

# 🐍 Snake Positions
snake = {
    32: 9,
    66: 26,
    77: 37,
    93: 73,
    96: 76,
    99: 2
}

# 🪜 Ladder Positions
ladder = {
    3: 43,
    16: 45,
    34: 67,
    49: 91
}

# ------------------ BOARD ------------------
def board(p1, p2):

    print("\n🎲🐍 SNAKE & LADDER BOARD 🪜🎲\n")

    for i in range(100, 0, -10):

        if (i // 10) % 2 == 0:
            nums = range(i - 9, i + 1)
        else:
            nums = range(i, i - 10, -1)

        for j in nums:

            # Both players
            if p1 == j and p2 == j:
                cell = "⭐"

            # Player 1
            elif p1 == j:
                cell = "👦"

            # Player 2
            elif p2 == j:
                cell = "👧"

            # Snake Head
            elif j in snake:
                cell = "🐍"

            # Ladder Start
            elif j in ladder:
                cell = "🪜"

            else:
                cell = str(j)

            print(f"{cell:^5}", end="")

        print("\n")

    print("🐍 = Snake Head")
    print("🪜 = Ladder Start")
    print("👦 = Player 1")
    print("👧 = Player 2")
    print("⭐ = Both Players")


# ------------------ GAME START ------------------

turn = 1
p1 = 0
p2 = 0

print("=" * 60)
print("🎲🐍      WELCOME TO SNAKE & LADDER      🪜🎲")
print("=" * 60)

board(p1, p2)

while p1 < 100 and p2 < 100:

    print("\n" + "-" * 60)

    if turn % 2 == 1:

        print("👦 Player 1 Turn")
        input("Press Enter to Roll Dice...")

        dice = random.randint(1, 6)
        print("🎲 Dice =", dice)

        p1 = p1 + dice

        if p1 > 100:
            p1 = p1 - dice
            print("❌ Need exact number to reach 100!")

        if p1 in ladder:
            print("🪜 Wow! Ladder Found!")
            p1 = ladder[p1]

        if p1 in snake:
            print("🐍 Oops! Snake Bit You!")
            p1 = snake[p1]

        print("📍 Player 1 Position =", p1)

    else:

        print("👧 Player 2 Turn")
        input("Press Enter to Roll Dice...")

        dice = random.randint(1, 6)
        print("🎲 Dice =", dice)

        p2 = p2 + dice

        if p2 > 100:
            p2 = p2 - dice
            print("❌ Need exact number to reach 100!")

        if p2 in ladder:
            print("🪜 Wow! Ladder Found!")
            p2 = ladder[p2]

        if p2 in snake:
            print("🐍 Oops! Snake Bit You!")
            p2 = snake[p2]

        print("📍 Player 2 Position =", p2)

    print("\n📊 CURRENT SCORE")
    print("👦 Player 1 :", p1)
    print("👧 Player 2 :", p2)

    board(p1, p2)

    turn = turn + 1

# ------------------ WINNER ------------------

print("\n" + "=" * 60)

if p1 >= 100:
    print("🏆🎉 CONGRATULATIONS! PLAYER 1 WINS 🎉🏆")
else:
    print("🏆🎉 CONGRATULATIONS! PLAYER 2 WINS 🎉🏆")

print("=" * 60)