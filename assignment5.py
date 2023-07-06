import sys

donor_db = [("William Gates, III", [653784.49, 100000]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1660.23, 4300.87, 10432.0]),
            ]

prompt = "\n".join(("Welcome to the charity mail room!",
                    "Please choose from below options:",
                    "1 - Send a Thank You",
                    "2 - Create a Report",
                    "3 - Quit",
                    ">>> "))
def send_thank_you():
    name = input("Enter the Full Name of the donor (or 'quit' to exit): ")
    if name.lower() == "quit":
        return
    elif name.lower() == "list":
        print("\n".join([donor[0] for donor in donor_db]))
        name = input("\nEnter the Full Name of the donor (or 'quit' to exit): ")
        if name.lower() == "quit":
            return

    donation = input("Enter the donation amount (or 'quit' to exit): ")
    if donation.lower() == "quit":
        return
    donation = float(donation)

    for donor in donor_db:
        if name == donor[0]:
            donor[1].append(donation)
            break
    else:
        donor_db.append((name, [donation]))

    print(f"\nDear {name},\nThank you for your generous donation of ${donation:.2f}.\nBest,\nYour Local Charity")


def create_report():
    print("\nDonor Name                | Total Given | Num Gifts | Average Gift")
    print("-"*66)
    for donor in sorted(donor_db, key=lambda x: sum(x[1]), reverse=True):
        name, donations = donor
        total = sum(donations)
        num = len(donations)
        average = total / num
        print(f"{name:<26} $ {total:>11.2f} {num:>11d}  $ {average:>11.2f}")


def quit_program():
    print("Bye!")
    sys.exit()


def main():
    while True:
        response = input(prompt)
        if response == "1":
            send_thank_you()
        elif response == "2":
            create_report()
        elif response == "3":
            quit_program()
        else:
            print("Not a valid option!")

if __name__ == "__main__":
    main()
