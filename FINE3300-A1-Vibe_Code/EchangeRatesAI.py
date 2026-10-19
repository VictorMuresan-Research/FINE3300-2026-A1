import csv


class ExchangeRates:
    def __init__(self, file_name):
        self.usd_to_cad= 0

        # Read the CSV and keep the rate from the last data row.
        with open(file_name, "r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            for row in reader:
                self.usd_to_cad = float(row["FXAUSDCAD"])

    def convert(self, amount, from_currency, to_currency):
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency == to_currency:
            return amount
        elif from_currency == "USD":
            return amount * self.usd_to_cad
        else:  # CAD to USD
            return amount / self.usd_to_cad


if __name__ == "__main__":
    rates = ExchangeRates("BankOfCanadaExchangeRate.2026.csv")

    amount = float(input("Enter the amount: $"))
    from_currency = input("Convert from (USD or CAD): ")
    to_currency = input("Convert to (USD or CAD): ")

    converted_amount = rates.convert(amount, from_currency, to_currency)

    print(
        f"${amount:.2f} {from_currency.upper()} = "
        f"${converted_amount:.2f} {to_currency.upper()}"
    )