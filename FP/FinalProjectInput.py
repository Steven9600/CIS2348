#Final Project Part 1
#Steven Pesantez 1672034

import csv
from datetime import datetime

class OutputInventory:
        #class for methods used to make the output inventory files from the input files given
    def __init__(self, item_list):
        self.item_list = item_list
    def full(self):
        #required output A
        #creates csv output for the the full inventory
        #Each row contains item ID, manufacturer name, item type, price, service date, and damaged
        with open('FullInventory(1).csv','w') as file:
            items = self.item_list
            keys = sorted(items.keys(), key=lambda x: items[x]['manufacturer'])
            for item in keys:
                id = item
                manufacturer = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                file.write('{},{},{},{},{},{}\n'.format(id,manufacturer,item_type,price,service_date,damaged))
    def type(self):
        #Required output B
        #creates csv output for item by type and sorted by ID
        items = self.item_list
        types = []
        keys = sorted(items.keys())
        for item in items:
            item_type = items[item]['item_type']
            if item_type not in types:
                types.append(item_type)
        for type in types:
            file_name = type.capitalize() + 'Inventory.csv'
            with open('FullInventory(1).csv'+file_name, 'w') as file:
                for item in keys:
                    id = item
                    manufacturer = items[item]['manufacturer']
                    price = items[item]['price']
                    service_date = items[item]['service_date']
                    damaged = items[item]['damaged']
                    item_type = items[item]['item_type']
                    if type == item_type:
                        file.write('{},{},{},{},{}\n'.format(id,manufacturer,price,service_date,damaged))
    def past_service_date(self):
        #Required output C
        #create csv output file for items past the service date listed
        #sorts oldest to most recent
        items = self.item_list
        keys = sorted(items.keys(), key=lambda x: datetime.strptime(items[x]['service_date'], %B %d %Y).date(), reverse=True)
        with open('PastServiceDateInventory.csv','w') as file:
            for item in keys:
                id = item
                manufacturer = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                today = datetime.now().date()
                service_expiration = datetime.strptime(service_date, %B %d %Y).date()
                expired = service_expiration <today
                if expired:
                    file.write('{},{},{},{},{},{}\n'.format(id, manufacturer, item_type, price, service_date, damaged))
    def damaged(self):
        #Required output D
        #creates CSV output file for all items that are damaged
        items = self.item_list
        keys = sorted(items.keys(), key=lambda x: items[x]['price'], reverse=True)
        with open('DamagedInventory(1).csv','w') as file:
            for item in keys:
                id = item
                manufacturer = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                if damaged:
                        file.write('{},{},{},{},{},{}'.format(id, manufacturer, item_type, price, service_date))


if __name__ == '__main__':
    items= {}
    files = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']
    for file in files:
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                item_id = line[0]
                if file == files[0]:
                    items[item_id] = {}
                    manufacturer = line[1]
                    item_type = line[2]
                    damaged = line[3]
                    items[item_id]['manufacturer'] = manufacturer.strip()
                    items[item_id]['item_type'] = item_type.strip()
                    items[item_id]['damaged'] = damaged
                elif file ==files[1]:
                    price = line[1]
                    items[item_id]['price'] = price
                elif file == files[2]:
                    service_date = line[1]
                    items[item_id]['service_date'] = service_date

    #creates output files
    inventory = OutputInventory(items)
    inventory.full()
    inventory.type()
    inventory.PastServiceDateInventory()
    inventory.damaged()







