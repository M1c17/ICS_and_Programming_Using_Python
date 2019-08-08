#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 14:11:20 2019

@author: MASTER
"""

#Imagine we run a car dealership. We sell all types of vehicles, 
#from motorcycles to trucks. We set ourselves apart from the competition 
#by our prices. Specifically, how we determine the price of a vehicle on our
# lot: $5,000 x number of wheels a vehicle has. We love buying back our
# vehicles as well. We offer a flat rate - 10% of the miles driven on the 
# vehicle. For trucks, that rate is $10,000. For cars, $8,000. For motorcycles,
# $4,000.
#
#If we wanted to create a sales system for our dealership using Object-oriented
# techniques, how would we do so? What would the objects be? We might have a
# Sale class, a Customer class, an Inventory class, and so forth, but
# we'd almost certainly have a Car, Truck, and Motorcycle class.

from abc import ABCMeta, abstractmethod
class Vehicle(object):
    """A vehicle for sale by Jeffco Car Dealership.


    Attributes:
        wheels: An integer representing the number of wheels the vehicle has.
        miles: The integral number of miles driven on the vehicle.
        make: The make of the vehicle as a string.
        model: The model of the vehicle as a string.
        year: The integral year the vehicle was built.
        sold_on: The date the vehicle was sold.
    """

    __metaclass__ = ABCMeta

    base_sale_price = 0
    wheels = 0

    def __init__(self, miles, make, model, year, sold_on):
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    def sale_price(self):
        """Return the sale price for this vehicle as a float amount."""
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        """Return the price for which we would pay to purchase the vehicle."""
        if self.sold_on is None:
            return 0.0  # Not yet sold
        return self.base_sale_price - (.10 * self.miles)

    @abstractmethod
    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        pass
    
class Car(Vehicle):
    """A car for sale by Jeffco Car Dealership."""

    base_sale_price = 8000
    wheels = 4

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'car'

class Truck(Vehicle):
    """A truck for sale by Jeffco Car Dealership."""

    base_sale_price = 10000
    wheels = 4

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'truck'
    
class Motorcycle(Vehicle):
    """A motorcycle for sale by Jeffco Car Dealership."""

    base_sale_price = 4000
    wheels = 2

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'motorcycle'
    
    
    
    