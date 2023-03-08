from fractions import Fraction


class TdPwOrA:
    number_of_inputs = int(input("Enter number of inputs : "))

    for i in range(number_of_inputs):
        true_discount = Fraction(input("Enter True discount amount (RS) : "))
        present_worth_or_amount = input("select between '1.present worth' or '2.Amount' as input: ")
        if present_worth_or_amount == "1":
            present_worth = Fraction(input("Enter present worth amount (Rs): "))
            print("To find Bankers Gain(BG) we use :")
            print("Bankers Gain = ((true discount)**2)/present worth")
            bankers_gain = round(float((true_discount ** 2) / present_worth), 2)
            print("To find Bankers Discount(BD) we use :")
            print("Bankers Discount(B.D) = Bankers Gain(B.G) + True Discount(T.D)")
            print(" ")
            bankers_discount = round(float(bankers_gain + true_discount), 2)
            enter_you_want_to_find = input("Enter to find between '1.bankers gain' or 'bankers discount': ")
            if enter_you_want_to_find == "1":
                if bankers_gain >= 0:

                    print("Bankers Gain : RS." + str(bankers_gain) + "  ---------- " + str(i + 1))
                    print(" ")
                else:
                    print("Enter Valid Details")
                print(" ")

            if enter_you_want_to_find == "2":
                if bankers_discount >= 0:

                    print("Bankers discount : RS. " + str(bankers_discount) + "  ---------- " + str(i + 1))
                    print(" ")
                else:
                    print("Enter Valid Details")

        elif present_worth_or_amount == "2":
            amount = Fraction(input("Enter  amount (Rs): "))
            print("present worth = amount - true discount")
            present_worth = round(float(amount - true_discount), 2)
            print("Bankers Discount(B.D) = (true discount/(present worth))*amount")
            bankers_discount = round(float((true_discount / present_worth) * amount))
            print("Bankers gain = bankers discount-true discount")
            bankers_gain = round(float(bankers_discount - true_discount), 2)
            enter_you_want_to_find = input("Enter you want to find '1.present worth' '2.banker discount' '3.bankers gain': ")
            if enter_you_want_to_find == "1":
                if present_worth >= 0:

                    print("Present worth : RS. " + str(present_worth) + "  ---------- " + str(i + 1))
                    print(" ")
                else:
                    print("enter valid details")

            if enter_you_want_to_find == "2":
                if bankers_discount >= 0:

                    print("Bankers Discount : RS. " + str(bankers_discount) + "  ---------- " + str(i + 1))
                    print(" ")
                else:
                    print("Enter valid details")

            if enter_you_want_to_find =="3":
                if bankers_gain >= 0:

                    print("Bankers gain : RS, " + str(bankers_gain) + "  ---------- " + str(i + 1))
                    print(" ")
                else:
                    print("Enter valid details")
