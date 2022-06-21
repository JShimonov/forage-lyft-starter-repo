from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

from car import Car


class CarFactory:
    # create calliope
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear) -> Car:
        '''Create a calliope car model
        
        Args:
            current_date (date): the current date
            last_service_date (date): the last time the battery was serviced
            current_mileage (int): current mileage on the engine
            last_service_mileage (int): mileage on engine since last time it was serviced
            tire_wear (list): state of each tire
        
        Returns:
            Car: the calliope car
        '''
        engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        battery = SpindlerBattery(current_date=current_date, last_service_date=last_service_date)
        tires = CarriganTires(tire_wear=tire_wear)
        car = Car(engine, battery, tires)
        return car
    
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear) -> Car:
        '''Create a glissade car model
        
        Args:
            current_date (date): the current date
            last_service_date (date): the last time the battery was serviced
            current_mileage (int): current mileage on the engine
            last_service_mileage (int): mileage on engine since last time it was serviced
            tire_wear (list): state of each tire
        
        Returns:
            Car: the glissade car
        '''
        engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        battery = SpindlerBattery(current_date=current_date, last_service_date=last_service_date)
        tires = OctoprimeTires(tire_wear=tire_wear)
        car = Car(engine, battery, tires)
        return car
    
    def create_palindrome(current_date, last_serviced_date, indicator_light, tire_wear) -> Car:
        '''Create a palindrome car model
        
        Args:
            current_date (date): the current date
            last_service_date (date): the last time the battery was serviced
            indicator_light (boolean): true if warning indicator is on, else false
            tire_wear (list): state of each tire
        
        Returns:
            Car: the palindrome car
        '''
        engine = SternmanEngine(indicator_light=indicator_light)
        battery = SpindlerBattery(current_date=current_date, last_service_date=last_serviced_date)
        tires = CarriganTires(tire_wear=tire_wear)
        car = Car(engine, battery, tires)
        return car
    
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear) -> Car:
        '''Create a palindrome car model
        
        Args:
            current_date (date): the current date
            last_service_date (date): the last time the battery was serviced
            current_mileage (int): current mileage on the engine
            last_service_mileage (int): mileage on engine since last time it was serviced
            tire_wear (list): state of each tire

        Returns:
            Car: the palindrome car
        '''
        engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        battery = NubbinBattery(current_date=current_date, last_service_date=last_service_date)
        tires = OctoprimeTires(tire_wear=tire_wear)
        car = Car(engine, battery, tires)
        return car
    
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear) -> Car: 
        '''Create a thovex car model
        
        Args:
            current_date (date): the current date
            last_service_date (date): the last time the battery was serviced
            current_mileage (int): current mileage on the engine
            last_service_mileage (int): mileage on engine since last time it was serviced
            tire_wear (list): state of each tire
        
        Returns:
            Car: the thovex car
        '''
        engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        battery = NubbinBattery(current_date=current_date, last_service_date=last_service_date)
        tires = CarriganTires(tire_wear=tire_wear)
        car = Car(engine, battery, tires)
        return car
    
    
    