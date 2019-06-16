class Deal(object):
    def __init__(self, _txn, _amount, _marker=False):
        self.txnId = _txn
        self.amount = _amount
        self.eodMarker = _marker
        self.dbRecord = 'Im a very big record'


class DealData(object):
    def get_data(self):
        print('Conected to server-prod-HKG')
        return [Deal(1234, 2300000), Deal(1235, 5000000, True)]

