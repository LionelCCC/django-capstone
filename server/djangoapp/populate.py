from .models import CarMake, CarModel

def initiate():
    print("initiating database population")
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Great cars. German technology"},
        {"name": "Audi", "description": "Great cars. German technology"},
        {"name": "Kia", "description": "Great cars. Korean technology"},
        {"name": "Toyota", "description": "Great cars. Japanese technology"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(CarMake.objects.create(name=data['name'], description=data['description']))

    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
        {"name": "Pathfinder", "car_type": "SUV", "year": 2023, "car_make": car_make_instances[0], "dealer_id": 1},
        {"name": "Qashqai", "car_type": "SUV", "year": 2023, "car_make": car_make_instances[0], "dealer_id": 1},
        {"name": "XTRAIL", "car_type": "SUV", "year": 2023, "car_make": car_make_instances[0], "dealer_id": 1},
        {"name": "A-Class", "car_type": "SUV", "year": 2023, "car_make": car_make_instances[1], "dealer_id": 1},
        {"name": "C-Class", "car_type": "SUV", "year": 2023, "car_make": car_make_instances[1], "dealer_id": 1},
        {"name": "E-Class", "car_type": "SUV", "year": 2023, "car_make": car_make_instances[1], "dealer_id": 1},
        {"name": "A4", "car_type": "SUV", "year": 2023, "car_make": car_make_instances[2], "dealer_id": 1},
        {"name": "A5", "car_type": "SUV", "year": 2023, "car_make": car_make_instances[2], "dealer_id": 1},
        {"name": "A6", "car_type": "SUV", "year": 2023, "car_make": car_make_instances[2], "dealer_id": 1},
        {"name": "Sorrento", "car_type": "SUV", "year": 2023, "car_make": car_make_instances[3], "dealer_id": 1},
        {"name": "Carnival", "car_type": "SUV", "year": 2023, "car_make": car_make_instances[3], "dealer_id": 1},
        {"name": "Cerato", "car_type": "Sedan", "year": 2023, "car_make": car_make_instances[3], "dealer_id": 1},
        {"name": "Corolla", "car_type": "Sedan", "year": 2023, "car_make": car_make_instances[4], "dealer_id": 1},
        {"name": "Camry", "car_type": "Sedan", "year": 2023, "car_make": car_make_instances[4], "dealer_id": 1},
        {"name": "Kluger", "car_type": "SUV", "year": 2023, "car_make": car_make_instances[4], "dealer_id": 1},
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'],
            car_make=data['car_make'],
            car_type=data['car_type'],  # Match the dictionary key to the model field
            year=data['year'],
            dealer_id=data['dealer_id']  # Add the dealer ID field
        )
