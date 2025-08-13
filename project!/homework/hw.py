def calculate_debt(principal, annual_rate, years, commission_rate=0):
    """
    მარტივი პროცენტის ფორმულით საერთო დავალიანების გამოთვლა, საკომისიოს გამოკლებით.
    :param principal: ძირითადი თანხა (ლარი)
    :param annual_rate: წლიური საპროცენტო განაკვეთი (%)
    :param years: წლების რაოდენობა
    :param commission_rate: საკომისიო (%)
    :return: საერთო დავალიანება მითითებული წლების შემდეგ
    """
    interest = principal * (annual_rate / 100) * years
    total_debt = principal + interest
    commission = total_debt * (commission_rate / 100)
    total_debt -= commission
    return total_debt

def calculate_credit(principal, annual_rate, years, commission_rate=0):
    """
    მარტივი პროცენტის ფორმულით კრედიტის გადახდის საერთო თანხის გამოთვლა, საკომისიოს გამოკლებით.
    :param principal: კრედიტის ძირითადი თანხა (ლარი)
    :param annual_rate: წლიური საპროცენტო განაკვეთი (%)
    :param years: წლების რაოდენობა
    :param commission_rate: საკომისიო (%)
    :return: გადასახდელი საერთო თანხა მითითებული წლების შემდეგ
    """
    interest = principal * (annual_rate / 100) * years
    total_payment = principal + interest
    commission = total_payment * (commission_rate / 100)
    total_payment -= commission
    return total_payment

if __name__ == "__main__":
    while True:
        choice = input("აირჩიეთ ოპერაცია (დავალიანება/კრედიტი): ").strip().lower()

        if choice == "დავალიანება":
            principal = float(input("შეიყვანეთ საერთო თანხა: "))
            annual_rate = float(input("შეიყვანეთ წლიური პროცენტი: "))
            years = int(input("შეიყვანეთ წლიური რაოდენობა: "))
            commission_rate = float(input("შეიყვანეთ საკომისიო (%): "))

            debt = calculate_debt(principal, annual_rate, years, commission_rate)
            print(f"საბოლოო დავალიანება (საკომისიოს გამოკლებით): {debt:.2f} ლარი")

        elif choice == "კრედიტი":
            principal = float(input("შეიყვანეთ კრედიტის ძირითადი თანხა: "))
            annual_rate = float(input("შეიყვანეთ წლიური საპროცენტო განაკვეთი: "))
            years = int(input("შეიყვანეთ სესხის ვადა (წლებში): "))
            commission_rate = float(input("შეიყვანეთ საკომისიო (%): "))

            payment = calculate_credit(principal, annual_rate, years, commission_rate)
            print(f"სესხის გადახდის საერთო თანხა (საკომისიოს გამოკლებით): {payment:.2f} ლარი")

        else:
            print("არასწორი არჩევანი. სცადეთ თავიდან.")

        change = input("გსურთ მონაცემების შეცვლა და თავიდან გამოთვლა? : ").strip().lower()
        if change != "დიახ":
            print("ტრანზაქცია დასრულდა, ნახვამდის!")
            break
