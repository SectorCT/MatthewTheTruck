from dataclasses import dataclass

@dataclass
class Package:
    id: int                    # Unique identifier for the package
    address: str               # Delivery address
    lat: float                 # Latitude coordinate
    long: float                # Longitude coordinate
    client_name: str           # Name of the client
    client_phone: str          # Client's phone number
    volume: float               # Size of the package (e.g., "small", "medium", "large")
    weight: float              # Weight of the package in kg

package1 = Package(
    id="P001",
    address="1 Tsar Osvoboditel Blvd, Sofia",
    lat=42.695873,
    long=23.332879,
    client_name="Ivan Petrov",
    client_phone="+359 88 123 4567",
    volume="medium",
    weight=2.5
)

package2 = Package(
    id="P002",
    address="15 Vitosha Blvd, Sofia",
    lat=42.691944,
    long=23.321111,
    client_name="Maria Dimitrova",
    client_phone="+359 89 987 6543",
    volume="large",
    weight=5.0
)

package3 = Package(
    id="P003",
    address="Boyana Residential Area, Sofia",
    lat=42.644722,
    long=23.265833,
    client_name="Georgi Ivanov",
    client_phone="+359 87 555 1212",
    volume="small",
    weight=0.8
)

# Example usage: Printing the packages
if __name__ == "__main__":
    print("Package 1:")
    print(package1)
    print("\nPackage 2:")
    print(package2)
    print("\nPackage 3:")
    print(package3)