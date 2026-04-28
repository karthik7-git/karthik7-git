import time

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def main_menu():
    print("\n" + "="*50)
    print("🇺🇸  2026 ELECTION PROCESS ASSISTANT  🇺🇸")
    print("="*50)
    print("1. Overview of the 2026 Midterm Cycle")
    print("2. Current Timeline (Where are we now?)")
    print("3. How Primaries Work")
    print("4. Election Day & Post-Election")
    print("5. Exit")
    print("="*50)

def show_overview():
    print("\n--- 📝 OVERVIEW: THE 2026 MIDTERMS ---")
    slow_print("Unlike Presidential years, Midterms focus on Congress.")
    print("* House of Representatives: All 435 seats are up for election.")
    print("* Senate: About 1/3 of the seats (Class 2) are up for election.")
    print("* Governors/Local: Many states elect governors and local officials.")
    input("\nPress Enter to return to menu...")

def show_timeline():
    print("\n--- 📅 2026 KEY DATES ---")
    print("[NOW] April 2026: Primary season is in full swing.")
    print("• March - Sept 2026: State Primaries and Caucuses.")
    print("• Nov 3, 2026:       ELECTION DAY.")
    print("• Jan 3, 2027:       120th Congress Convenes.")
    input("\nPress Enter to return to menu...")

def show_primaries():
    print("\n--- 🗳️ STEP 1: THE PRIMARIES ---")
    slow_print("Before the big election in November, parties must choose ONE candidate.")
    print("1. Candidates from the same party run against each other.")
    print("2. Voters (you!) cast ballots to decide the winner.")
    print("3. The winner advances to the General Election.")
    input("\nPress Enter to return to menu...")

def show_election_day():
    print("\n--- 🏁 STEP 2: GENERAL ELECTION ---")
    print("Date: Tuesday, November 3, 2026")
    slow_print("This is the final round. Winners here take office in January.")
    print("* Certification: States verify the math (can take days/weeks).")
    print("* Transition: Winners prepare to move to D.C. or state capitals.")
    input("\nPress Enter to return to menu...")

# Main Logic Loop
if __name__ == "__main__":
    while True:
        main_menu()
        choice = input("Select an option (1-5): ")
        
        if choice == '1':
            show_overview()
        elif choice == '2':
            show_timeline()
        elif choice == '3':
            show_primaries()
        elif choice == '4':
            show_election_day()
        elif choice == '5':
            print("Thank you for being an informed voter! Goodbye.")
            break
        else:
            print("Invalid choice, please try again.")
