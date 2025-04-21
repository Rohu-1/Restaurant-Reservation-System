import json

with open("data/restaurants.json") as f:
    restaurants = json.load(f)

reservations = []
