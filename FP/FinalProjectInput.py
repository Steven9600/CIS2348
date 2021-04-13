#Final Project Part 1
#Steven Pesantez 1672034

import csv
from datetime import datetime

class OutputInventory:
        #class for methods used to make the output inventory files from the input files given
    def __init__(self, item_list):
        self.item_list = item_list
    def full_inventory(self):
        #required output A
        #creates csv output for the the full inventory
        #Each row contains item ID, manufacturer name, item type, price, service date, and damaged

        f= open("FullInventory(1).csv","w")
        items_list = self.item_list
        keys = sorted(items_list.keys(), key=lambda x: items_list[x]["manufacturer"])
        # Sorted Alphabetically using build in function sorted & by manufacturer using lambda

        for item in keys:
            the_id = item
            manufacturer_name = items_list[item]["manufacturer"]
            item = items_list[item]["item_type"]
            price_item = items_list[item]["price"]
            serv_date = items_list[item]["service_date"]
            damaged_item = items_list[item]["damaged"]
            file.write("{},{},{},{},{},{}".format(the_id, manufacturer_name, item, price_item, serv_date, damaged_item))
    def type(self):
        #Required output B
        #creates csv output for item by type and sorted by ID
        items_list = self.item_list
        types = []
        keys = sorted(items.keys())
        for item in items:
            item = items[item]['item_type']
            if item not in types:
                types.append(item)
        for types in types:
            file_name = types() + "Inventory.csv"
            f = open("FullInventory(1).csv", + file_name, "w")
            for item in keys:
                the_id = item
                manufacturer_name = items[item]["manufacturer"]
                price_item = items[item]["price"]
                serv_date = items[item]["service_date"]
                damaged_item = items[item]["damaged"]
                item = items[item]["item_type"]
                if types == item:
                    file.write("{},{},{},{},{}".format(the_id, manufacturer_name, price_item, serv_date, damaged_item))
    def past_service_date(self):
        #Required output C
        #create csv output file for items past the service date listed
        #sorts oldest to most recent
        items_number = self.item_list
        keys = sorted(items_number.keys(), key=lambda x: datetime.strptime(items_number[x]['service_date'], % B % d % Y).date(), reverse =True))
        f= open("PastServiceDateInventory.csv","w")
            for item in keys:
                the_id = item
                manufacturer_name = items_number[item]['manufacturer']
                item = items_number[item]['item_type']
                price_item = items_number[item]['price']
                service_date = items_number[item]['service_date']
                damaged_item = items_number[item]['damaged']
                today = datetime.now().date()
                service_expiration = datetime.strptime(service_date, %B %d %Y).date()
                expired = service_expiration <today
                if expired:
                    file.write('{},{},{},{},{},{}'.format(the_id, manufacturer_name, item, price_item, service_date, damaged_item))
    def damaged(self):
        #Required output D
        #creates CSV output file for all items that are damaged
        items = self.item_list
        keys = sorted(items.keys(), key=lambda x: items[x]['price'], reverse=True)
        with open('DamagedInventory(1).csv','w') as file:
            for item in keys:
                the_id = item
                manufacturer_name = items[item]['manufacturer']
                item = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                if damaged:
                        file.write('{},{},{},{},{},{}'.format(the_id, manufacturer_name, item, price, service_date))


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







