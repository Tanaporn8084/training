score = int(input("ใส่คะแนนของคุณ : "))

if score >= 0 and score <= 100:

    if score >= 80:
        print("เกรด A")

    elif score >= 70:
        print("เกรด B")

    elif score >= 60:
        print("เกรด C")

    elif score >= 50:
        print("เกรด D")

    else:
        print("เกรด F")