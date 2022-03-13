from os.path import splitext
import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

        if self.brand == '':
            raise AttributeError
        
        if self.carrying == 0.0:
            raise AttributeError

        if self.get_photo_file_ext().lower() not in ['.jpg', '.jpeg', '.png', '.gif']:
            raise AttributeError

    def get_photo_file_ext(self):
        _, ext = splitext(self.photo_file_name)
        return ext


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'car'
        self.passenger_seats_count = int(passenger_seats_count)
        if self.passenger_seats_count <= 0:
            raise AttributeError

class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_lwh):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        try:
            self.body_length, self.body_width, self.body_height = map(float, body_lwh.split('x'))
        except ValueError:
            self.body_length, self.body_width, self.body_height = 0., 0., 0.
        
        self._body_volume = self.body_length * self.body_width * self.body_height

    def get_body_volume(self):
        return self._body_volume


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra
        if self.extra == '':
            raise AttributeError

def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.DictReader(csv_fd, delimiter=';')

        # заголовок: car_type;brand;passenger_seats_count;photo_file_name;body_whl;carrying;extra
        
        for row in reader:

            try:
                car_type = row['car_type']
                brand = row['brand']
                passenger_seats_count = row['passenger_seats_count']
                photo_file_name = row['photo_file_name']
                body_whl = row['body_whl']
                carrying = row['carrying']
                extra = row['extra']
                
                if car_type == 'car': 
                    car_list.append(Car(brand, photo_file_name, carrying, passenger_seats_count))
                elif car_type == 'truck':
                    car_list.append(Truck(brand, photo_file_name, carrying, body_whl))
                elif car_type == 'spec_machine': 
                    car_list.append(SpecMachine(brand, photo_file_name, carrying, extra))
                    
            except ValueError:
                continue
            except TypeError:
                continue
            except AttributeError:
                continue

    return car_list
