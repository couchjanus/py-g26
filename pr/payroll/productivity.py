class Productivity:
    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        for employee in employees:
            employee.work(hours)
            print()
            
class ManagerRole:
    def work(self, hours):
        print(f'{self.name} screams and tells for {hours}.')
    
class SecretaryRole:
    def work(self, hours):
        print(f'{self.name} expends {hours} hours doing office paperwork.')
            
class SalerRole:
    def work(self, hours):
        print(f'{self.name} expends {hours} hours on the phone.')
            
class FactoryRole:
    def work(self, hours):
        print(f'{self.name} manufactures gadgets for {hours} hours.')