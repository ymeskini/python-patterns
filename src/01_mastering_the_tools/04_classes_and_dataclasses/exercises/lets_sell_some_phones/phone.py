from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    address: str
    mail: str


@dataclass
class Phone:
    brand: str
    model: str
    price: int
    serial_number: str


@dataclass
class Plan:
    start_date: str
    customer: Customer
    phone: Phone | None
    monthly_price: int
    number_of_months: int
