from dateutil.relativedelta import relativedelta

from battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        super().__init__()
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        return relativedelta(self.current_date, self.last_service_date).years > 2
