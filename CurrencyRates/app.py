import sys
from exchange_rate import CurrencyConverter

from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QComboBox, QTextEdit


class CurrencyLookupApp(QWidget):
    def __init__(self, rates):
        super().__init__()

        self.rates = rates
        self.setWindowTitle('Currency Exchange Lookup')
        self.setWindowIcon(QIcon('wallet.jpg'))
        self.setFixedSize(600, 200)

        fnt = QFont('Open Sans', 13)

        currencyList = ['RUB', 'EUR', 'CAD', 'JPY', 'THB', 'TWD']
        timestamp = self.rates['timestamp']

        mainLayout = QVBoxLayout()

        label_timestamp = QLabel(f'<font size=5>Last updated {timestamp} </font>')

        self.comboCurrencyList = QComboBox()
        self.comboCurrencyList.setFont(fnt)
        self.comboCurrencyList.setFixedHeight(55)
        self.comboCurrencyList.addItems(currencyList)
        self.comboCurrencyList.currentIndexChanged.connect(self.lookupCurrencyRate)

        self.outputField = QTextEdit()
        self.outputField.setFont(fnt)

        self.lookupCurrencyRate()

        mainLayout.addWidget(label_timestamp)
        mainLayout.addWidget(self.comboCurrencyList)
        mainLayout.addWidget(self.outputField)

        self.setLayout(mainLayout)

    def lookupCurrencyRate(self):
        currencyRates = self.rates['quotes']
        targetCurrency = self.comboCurrencyList.currentText()
        currencyPair = 'USD' + targetCurrency
        exchangeRate = currencyRates[currencyPair]
        self.outputField.setText(f'$1 USD = {exchangeRate} {targetCurrency}')

def main():
    API_KEY = '3ece61d3ec6d85eeb638aa8576a81836'
    c1 = CurrencyConverter(API_KEY)

    global currency_rates
    currency_rates = c1.requestCurrency()

    if currency_rates is None:
        sys.exit()


if __name__ == '__main__':
    main()

    app = QApplication(sys.argv)

    exchange_app = CurrencyLookupApp(currency_rates)
    exchange_app.show()

    sys.exit(app.exec_())
