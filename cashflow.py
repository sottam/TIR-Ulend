from datetime import datetime, timedelta

class Wallet():

    DATE_FORMAT = '%Y-%m-%d'
    
    wallet = {}
    __investments = {}
    __installments = {}
    __min_date = None
    __max_date = None

    def __init__(self, investments:dict, installments:dict) -> None:
        self.__investments = investments
        self.__installments = installments
        self.__set_min_max_dates()
        self.__build_date_interval_dict()
        self.__subtract_investments_from_wallet()
        self.__add_installments_to_wallet()

    def get_cashflow(self) -> dict:
        return self.wallet

    def __set_min_max_dates(self) -> None:
        dates = []
        for inv in self.__investments:
            dates.append(datetime.strptime(inv['created_at'], self.DATE_FORMAT))

        for ins in self.__installments:
            dates.append(datetime.strptime(ins['due_date'], self.DATE_FORMAT))

        self.__min_date = min(dates)
        self.__max_date = max(dates)

    def __build_date_interval_dict(self) -> None:
        out = {}
        date = self.__min_date
        while date <= self.__max_date:
            out[date.strftime(self.DATE_FORMAT)] = 0.0
            date += timedelta(days=1)
        
        self.wallet = out

    def __subtract_investments_from_wallet(self) -> None:
        for inv in self.__investments:
            date = inv['created_at']
            amount = float(inv['amount'])
            
            self.wallet[date] -= amount

    def __add_installments_to_wallet(self) -> None:
        for ins in self.__installments:
            date = ins['due_date']
            amount = float(ins['amount'])
            
            self.wallet[date] += amount

    

