import csv

def load_from_csv(path, cls):
    objects = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            obj = cls.from_dict(row)
            objects.append(obj)
    return objects

def save_to_csv(path, objects, fieldnames):
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for obj in objects:
            writer.writerow(obj.to_dict())
