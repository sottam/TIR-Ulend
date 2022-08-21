from cashflow import Wallet
from investments import investments
from installments import installments
import numpy_financial as npf

Wlt = Wallet(investments, installments)
cashflow = Wlt.get_cashflow()


def calc_irr():
    data = []
    for amount in cashflow.values():
        data.append(amount)

    irr = round(npf.irr(data), 2)
    print("TIR:", f'{irr:.2f}%')


if __name__ == "__main__":
    calc_irr()