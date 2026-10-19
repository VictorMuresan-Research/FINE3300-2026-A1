# This program converts between USD and CAD using the latest exchange rate from the Bank of Canada.
# The exchange rate is read from a CSV file downloaded from the Bank of Canada website.
# This class reads the exchange rate from the CSV file and provides a method (convert) to convert between USD and CAD.
class ExchangeRates:
    def __init__(self, file_name):
        # This rate is in CAD for one USD.
        self.__usd_cad_rate = 0

        # Open the CSV file and read all of its lines.
        file = open(file_name, "r")
        lines = file.readlines()
        file.close()

        # Find the position of the USD/CAD column in the first row.
        header = lines[0].split(",")
        rate_column = header.index("FXAUSDCAD")

        # Keep updating the rate from the CSV file so the most recently available one is saved.
        for line in lines[1:]:
            row = line.split(",")
            if row[rate_column] != "":
                self.__usd_cad_rate = float(row[rate_column])

    # This method converts an amount from one currency to another.
    def convert(self, amount, from_currency, to_currency):
        # Return the amount if both currencies are the same.
        if from_currency == to_currency:
            return amount
        # Multiply by the rate to convert USD to CAD.
        elif from_currency == "USD" and to_currency == "CAD":
            return amount * self.__usd_cad_rate
        # Divide by the rate to convert CAD to USD.
        else:
            return amount / self.__usd_cad_rate

if __name__ == "__main__":
    # Create the exchange rate object using the CSV file.
    rates = ExchangeRates("BankOfCanadaExchangeRate.2026.csv")

    # Get the amount and currencies from the user.
    amount = float(input("Enter the amount: "))
    from_currency = input("Convert from (USD or CAD): ").upper()
    to_currency = input("Convert to (USD or CAD): ").upper()

    # Check that the user entered USD or CAD before converting.
    if from_currency in ["USD", "CAD"] and to_currency in ["USD", "CAD"]:
        # Convert the amount and print the result.
        answer = rates.convert(amount, from_currency, to_currency)
        print("${:.2f} {} equals ${:.2f} {}".format(amount, from_currency, answer, to_currency))
    # Prints error message if the user did not enter USD or CAD.
    else:
        print("Please enter USD or CAD for both currencies.")