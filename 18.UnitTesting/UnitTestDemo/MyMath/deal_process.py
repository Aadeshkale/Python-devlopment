from MyMath.third_party import DealData

class DealProcess(object):
    def today_deals(self):
        dd = DealData()
        _deals = dd.get_data() # Third party code
        processed = self.process_deals(_deals)
        return processed

    def process_deals(self, _deals):
        print ('.... processing....')
        return _deals
