class ItineraryDetails:

    def __init__(self, details: dict) -> None:
        self.destination = details['destination']
        self.package = details['package']
        self.total_weight = details['weight']
        self.time = self.calc_time()
        self.cost = self.calc_cost()
        self.passed = self.calc_time_passed()

    def calc_time(self):
        return self.destination['distance'] / (self.package['max_speed'])

    def calc_cost(self):
        return (self.total_weight * 10000 * self.destination['distance'] + self.package['package_rate'])
    
    def calc_time_passed(self):
        return self.time * (1/(1-self.package['max_speed']**2)**0.5)


class Customer:
    
    def __init__(self,customer:dict):
        self.first_name = customer['first_name']
        self.last_name = customer['last_name']
        self.age = customer['age']
        self.id_number = customer['id_number']
        self.package = customer['package']
        self.weight = customer['weight']
        self.luggage_weight = customer['luggage_weight']
        self.destination = customer['destination']
        self.details = self.build_itinerary()


    def build_itinerary(self):
        dest = Destinations(self.destination)
        pack = Packages(self.package)
        total_weight = self.weight + self.luggage_weight
        details = ItineraryDetails({'destination':dest.destination_details(), 'package': pack.package_details(), 'weight':total_weight})

        return details

    def print_ticket(self):
        print('|--------------------------------------|------------------------------------------|')
        print(f'| {self.last_name}, {self.first_name}: {self.id_number}                   Travel Group: {self.package}')
        print('|--------------------------------------|------------------------------------------|')
        print(f'| System: {self.details.destination["star"]}                       Resort: {self.details.destination["resort"]}')
        print('|--------------------------------------|------------------------------------------|')
        print(f'| Travel Time: ' + '{0:.2f}'.format(self.details.time) + ' years' + '                   Time passed on Earth: ' + '{0:.2f}'.format(self.details.passed) + ' years')     
        print('|--------------------------------------|------------------------------------------|')
        print(f'| Ticket Cost: ' + '${:,.2f}'.format(self.details.cost))   
        print('|--------------------------------------|------------------------------------------|')
        print('\n\n')



class Destinations:

    def __init__(self,destination) -> None:
        self.destination = destination

    def destination_details(self):
        details = {}
        
        match self.destination:
            case 'proxima centauri b':
                details = {
                    'distance': 4.22,
                    'resort': 'Proxima b Highlands',
                    'star': 'Proxima Centauri',
                    'star_type':'M'}
            case 'proxima centauri c':
                details = {
                    'distance': 4.22,
                    'resort': 'Proxima c Resort',
                    'star': 'Proxima Centauri',
                    'star_type':'M'}
            case 'barnards star b':
                details = {
                    'distance': 5.958,
                    'resort': 'Barnards Resort & Spa ',
                    'star': 'Barnard\'s Star',
                    'star_type':'M'}
            case 'ross 128 b':
                details = {
                    'distance': 11.03,
                    'resort': 'Ross Star Retreat',
                    'star': 'Ross 128',
                    'star_type':'M'}
            case 'luyten b':
                details = {
                    'distance': 12.2,
                    'resort': 'Luyten\'s Reserve',
                    'star': 'Luyten\'s Star',
                    'star_type':'M'}
            case _:
                details = {
                    'distance': 0.0,
                    'resort': '',
                    'star': '',
                    'star_type':''}                    

        return details                                                                            
                    

class Packages:
    
    def __init__(self, package) -> None:
        self.package = package

    def package_details(self):
        allowances = {}

        match self.package.lower():
            case 'silver':
                allowances = {'max_speed':0.6,'max_weight':200,'package_rate': 1000000}
            case 'gold':
                allowances = {'max_speed':0.7,'max_weight':220,'package_rate': 2000000}
            case 'platinum':
                allowances = {'max_speed':0.8,'max_weight':260,'package_rate': 4000000}
            case 'beryllium':
                allowances = {'max_speed':0.99,'max_weight':500,'package_rate': 8000000}
            case _:
                allowances = {'max_speed':0.5,'max_weight':100}

        return allowances
        


if __name__ == '__main__':

    bob = Customer({
        'first_name': 'Robert',
        'last_name': 'Smeagol', 
        'age':23,
        'id_number':'123-45-6789',
        'package':'Beryllium',
        'weight':185,
        'luggage_weight':50,
        'destination':'proxima centauri b'})

    lisa = Customer({
        'first_name': 'Lisa',
        'last_name': 'Smeagol', 
        'age':21,
        'id_number':'246-80-1234',
        'package':'Silver',
        'weight':125,
        'luggage_weight':80,
        'destination':'proxima centauri b'})

    lisa2 = Customer({
        'first_name': 'Lisa',
        'last_name': 'Smeagol', 
        'age':21,
        'id_number':'246-80-1234',
        'package':'Beryllium',
        'weight':125,
        'luggage_weight':80,
        'destination':'proxima centauri b'})

    frank = Customer({
        'first_name': 'Frank',
        'last_name': 'Freedom', 
        'age':73,
        'id_number':'333-33-1234',
        'package':'Beryllium',
        'weight':275,
        'luggage_weight':40000,
        'destination':'luyten b'})


    #bob.print_ticket()
    lisa.print_ticket()
    lisa2.print_ticket()
    #frank.print_ticket()
    

    

    