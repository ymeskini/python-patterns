from dataclasses import dataclass
from typing import Optional


@dataclass
class DealBasedCommission:
    commission_rate: int = 10000
    deals_landed: int = 0

    def compute_pay(self) -> int:
        return int(self.commission_rate * self.deals_landed)


@dataclass
class HourlyEmployee:
    name: str
    id: int
    pay_rate: int = 0
    hours_worked: float = 0
    employer_cost: int = 100000
    commission: Optional[DealBasedCommission] = None

    def compute_pay(self) -> int:
        total = int(self.pay_rate * self.hours_worked + self.employer_cost)

        if self.commission:
            total += self.commission.compute_pay()

        return total


@dataclass
class SalariedEmployee:
    name: str
    id: int
    monthly_salary: int = 0
    percentage: float = 1
    commission: Optional[DealBasedCommission] = None

    def compute_pay(self) -> int:
        total = int(self.monthly_salary * self.percentage)

        if self.commission:
            total += self.commission.compute_pay()

        return total


@dataclass
class Freelancer:
    name: str
    id: int
    pay_rate: int = 0
    hours_worked: float = 0
    vat_number: str = ""
    commission: Optional[DealBasedCommission] = None

    def compute_pay(self) -> int:
        total = int(self.pay_rate * self.hours_worked)

        if self.commission:
            total += self.commission.compute_pay()

        return total


def main() -> None:
    employee_commission = DealBasedCommission(deals_landed=10)

    employee = SalariedEmployee(
        name="Sara", id=47832, monthly_salary=5000, commission=employee_commission
    )
    print(f"{employee.name} earned ${(employee.compute_pay() / 100):.2f}.")


if __name__ == "__main__":
    main()
