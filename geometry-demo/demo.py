from geometry import Square, Circle, area_stats

def main():
    shapes = [Square(3),Circle(2),Square(4)]
    for s in shapes:
        print(f"{s.__class__.__name__} area: {s.area()}")

    print("\nSummary stats:")
    stats = area_stats(*shapes)
    for k, v in stats.items():
        print(f"{k}: {v}")
