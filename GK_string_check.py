total = 0

have_hyp = input("do you have the hyp? ")
if have_hyp == "yes":
    total += 1

have_opp = input("do you have the hyp? ")
if have_opp == "yes":
    total += 1

have_adj = input("do you have the hyp? ")
if have_adj == "yes":
    total += 1


if total == 1:
    print("do stuff")
elif total == 0:
    print("oh no")


