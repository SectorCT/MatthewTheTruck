from dataclasses import dataclass

@dataclass
class Driver:
    name: str                  # Name of the driver
    phone: str                 # Driver's phone number
    zone: str                  # Delivery zone (e.g., area or neighborhood they cover)

driver1 = Driver(
    name="Dimitar Stoyanov",
    phone="+359 88 765 4321",
    zone="Central Sofia"
)

driver2 = Driver(
    name="Elena Georgieva",
    phone="+359 87 999 8888",
    zone="Boyana"
)

if __name__ == "__main__":
    print("\nDriver 1:")
    print(driver1)
    print("\nDriver 2:")
    print(driver2)