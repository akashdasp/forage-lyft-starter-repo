from datetime import datetime

def need_service(self,num : int)  -> bool:
    service_threshold_date=self.last_service_date.replace(year=self.last_service_date.year+num)
    if(service_threshold_date<datetime.today().date() or self.engine_should_be_serviced()):
        return True
    else:
        return False