print("=================================")
print(" STONE PAPER SCISSORS GAME ")
print("=================================")

p1_count = 0
p2_count = 0


while True:

    print("\n1. Stone 🪨")
    print("2. Paper 📄")
    print("3. Scissors ✂️")

    p1 = int(input("👦 Player 1 Choice: "))
    p2 = int(input("👧 Player 2 Choice: "))

    print("\n⚔️ RESULT ⚔️")

    if p1 == p2:
        print("🤝 Match Draw!")

    elif p1 == 1 and p2 == 3:
        print("🏆 Player 1 Wins!")
        p1_count += 1

    elif p1 == 2 and p2 == 1:
        print("🏆 Player 1 Wins!")
        p1_count += 1

    elif p1 == 3 and p2 == 2:
        print("🏆 Player 1 Wins!")
        p1_count += 1

    elif p2 == 1 and p1 == 3:
        print("🏆 Player 2 Wins!")
        p2_count += 1

    elif p2 == 2 and p1 == 1:
        print("🏆 Player 2 Wins!")
        p2_count += 1

    elif p2 == 3 and p1 == 2:
        print("🏆 Player 2 Wins!")
        p2_count += 1

    else:
        print("❌ Invalid Choice!")

    print("\n📊 SCOREBOARD")
    print("👦 Player 1:", p1_count)
    print("👧 Player 2:", p2_count)

    ch = input("\n🔁 Play Again? (yes/no): ").lower()

    if ch == "no":

        print("\n=================================")
        print("🏁 FINAL RESULT")
        print("=================================")

        print("👦 Player 1:", p1_count)
        print("👧 Player 2:", p2_count)

        if p1_count > p2_count:
            print("🏆 OVERALL WINNER: PLAYER 1")
        elif p2_count > p1_count:
            print("🏆 OVERALL WINNER: PLAYER 2")
        else:
            print("🤝 MATCH DRAW!")

        print("\n🙏 Thanks for Playing!")
        break