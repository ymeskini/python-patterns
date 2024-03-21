from dataclasses import dataclass


@dataclass
class HourlyEmployee:
    name: str
    id: int
    pay_rate: int
    hours_worked: float = 0
    employer_cost: int = 100000

    def compute_pay(self) -> int:
        return int(self.pay_rate * self.hours_worked + self.employer_cost)


@dataclass
class SalariedEmployee:
    name: str
    id: int
    monthly_salary: int
    percentage: float = 1

    def compute_pay(self) -> int:
        return int(self.monthly_salary * self.percentage)


@dataclass
class Freelancer:
    name: str
    id: int
    pay_rate: int
    hours_worked: float = 0
    vat_number: str = ""

    def compute_pay(self) -> int:
        return int(self.pay_rate * self.hours_worked)


@dataclass
class SalariedEmployeeWithCommission(SalariedEmployee):
    commission_rate: int = 10000
    deals_landed: int = 0

    def compute_pay(self) -> int:
        return super().compute_pay() + int(self.commission_rate * self.deals_landed)


@dataclass
class HourlyEmployeeWithCommission(HourlyEmployee):
    commission_rate: int = 8000
    deals_landed: int = 0

    def compute_pay(self) -> int:
        return super().compute_pay() + int(self.commission_rate * self.deals_landed)


@dataclass
class FreelancerWithCommission(Freelancer):
    commission_rate: int = 5000
    deals_landed: int = 0

    def compute_pay(self) -> int:
        return super().compute_pay() + int(self.commission_rate * self.deals_landed)


def main() -> None:
    hourly_employee = HourlyEmployee(
        name="Henry", id=12346, pay_rate=5000, hours_worked=100
    )
    print(
        f"{hourly_employee.name} earned ${(hourly_employee.compute_pay() / 100):.2f}."
    )

    employee = SalariedEmployeeWithCommission(
        name="Sara", id=47832, monthly_salary=500000, deals_landed=10
    )
    print(f"{employee.name} earned ${(employee.compute_pay() / 100):.2f}.")


if __name__ == "__main__":
    main()
