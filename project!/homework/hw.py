def calculate_debt(principal, annual_rate, years, commission_rate=0):
    """
    მარტივი პროცენტის ფორმულით საერთო დავალიანების გამოთვლა, საკომისიოს გამოკლებით.
    """
    interest = principal * (annual_rate / 100) * years       # გამოთვლილი სარგებელი (მარტივი პროცენტის ფორმულით)
    total_debt = principal + interest                         # დავალიანება = ძირითადი თანხა + სარგებელი
    commission = total_debt * (commission_rate / 100)         # საკომისიოს გამოთვლა საერთო დავალიანებიდან
    total_debt -= commission                                  # საკომისიოს გამოკლება საბოლოო დავალიანებიდან
    return total_debt                                         # საბოლოო დავალიანების დაბრუნება

def calculate_credit(principal, annual_rate, years, commission_rate=0):
    """
    მარტივი პროცენტის ფორმულით კრედიტის გადახდის საერთო თანხის გამოთვლა, საკომისიოს გამოკლებით.
    """
    interest = principal * (annual_rate / 100) * years        # გამოთვლილი პროცენტი კრედიტისთვის
    total_payment = principal + interest                      # გადახდადი თანხა = ძირითადი + სარგებელი
    commission = total_payment * (commission_rate / 100)      # საკომისიოს გამოთვლა მთლიან გადახდადი თანხიდან
    total_payment -= commission                               # საკომისიოს გამოკლება გადახდადი თანხიდან
    return total_payment                                      # საბოლოო გადასახდელი თანხის დაბრუნება

if __name__ == "__main__":                                      # პროგრამა იწყება აქ, თუ პირდაპირ გაუშვეს
    while True:                                                 # დაუსრულებელი ციკლი — მუშაობს მანამ, სანამ მომხმარებელი არ შეწყვეტს
        choice = input("აირჩიეთ ოპერაცია (დავალიანება/კრედიტი): ").strip().lower()  # მომხმარებლის არჩევანი

        if choice == "დავალიანება":                             # თუ არჩეულია "დავალიანება"
            principal = float(input("შეიყვანეთ საერთო თანხა: "))              # ძირითადი თანხა (ლარში)
            annual_rate = float(input("შეიყვანეთ წლიური პროცენტი: "))         # წლიური პროცენტის რიცხვი
            years = int(input("შეიყვანეთ წლიური რაოდენობა: "))               # სესხის პერიოდი წლებში
            commission_rate = float(input("შეიყვანეთ საკომისიო (%): "))      # საკომისიოს პროცენტული მნიშვნელობა

            debt = calculate_debt(principal, annual_rate, years, commission_rate)  # ფუნქციის გამოძახება
            print(f"საბოლოო დავალიანება (საკომისიოს გამოკლებით): {debt:.2f} ლარი")  # შედეგის დაბეჭდვა

        elif choice == "კრედიტი":                               # თუ არჩეულია "კრედიტი"
            principal = float(input("შეიყვანეთ კრედიტის ძირითადი თანხა: "))          # ძირითადი კრედიტის თანხა
            annual_rate = float(input("შეიყვანეთ წლიური საპროცენტო განაკვეთი: "))    # პროცენტი
            years = int(input("შეიყვანეთ სესხის ვადა (წლებში): "))                 # ვადა წლებით
            commission_rate = float(input("შეიყვანეთ საკომისიო (%): "))             # საკომისიო პროცენტში

            payment = calculate_credit(principal, annual_rate, years, commission_rate)  # ფუნქციის გამოძახება
            print(f"სესხის გადახდის საერთო თანხა (საკომისიოს გამოკლებით): {payment:.2f} ლარი")  # შედეგი

        else:
            print("არასწორი არჩევანი. სცადეთ თავიდან.")          # თუ შეტანილი არჩევანი არასწორია

        change = input("გსურთ მონაცემების შეცვლა და თავიდან გამოთვლა? : ").strip().lower()  # ხელახალი გამოთვლის კითხვა
        if change != "დიახ":                                    # თუ პასუხი არაა "დიახ", ციკლი წყდება
            print("ტრანზაქცია დასრულდა, ნახვამდის!")           # დასრულების მესიჯი
            break                                                # ციკლიდან გასვლა
