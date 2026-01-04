import pytest # type: ignore
from vehicle import Vehicle, Car

@pytest.fixture
def basic_vehicle():
    """Provide a basic vehicle."""
    return Vehicle("Toyota", "Camry", 2020)

@pytest.fixture
def basic_car():
    """Provide a basic car."""
    return Car("Honda", "Civic", 2021, "gasoline")

# ============================================================================
# TESTING BASE CLASS (Vehicle)
# ============================================================================

def test_vehicle_description(basic_vehicle):
    """Test vehicle description."""
    assert basic_vehicle.get_description() == "2020 Toyota Camry"

def test_vehicle_starts_with_zero_odometer(basic_vehicle):
    """Test odometer starts at 0."""
    assert basic_vehicle.read_odometer() == 0

def test_update_odometer(basic_vehicle):
    """Test updating odometer."""
    basic_vehicle.update_odometer(100)
    assert basic_vehicle.read_odometer() == 100

def test_cannot_roll_back_odometer(basic_vehicle):
    """Test that rolling back odometer raises error."""
    basic_vehicle.update_odometer(100)

    with pytest.raises(ValueError) as exc_info:
        basic_vehicle.update_odometer(50)

    assert "Cannot roll back" in str(exc_info.value)

# ============================================================================
# TESTING CHILD CLASS (Car)
# ============================================================================

def test_car_inherits_vehicle_methods(basic_car):
    """Test that Car has Vehicle methods."""
    basic_car.update_odometer(50)
    assert basic_car.read_odometer() == 50

def test_car_description_includes_fuel_type(basic_car):
    """Test that Car description includes fuel type."""
    assert "gasoline" in basic_car.get_description()

def test_car_overrides_description(basic_car):
    """Test that Car overrides Vehicle description."""
    desc = basic_car.get_description()
    assert desc == "2021 Honda Civic (gasoline)"
