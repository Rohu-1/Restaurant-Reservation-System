import random
from datetime import datetime
from database import restaurants, reservations

def check_availability(restaurant_name, date_time, people):
    restaurant = next((r for r in restaurants if r['name'].lower() == restaurant_name.lower()), None)
    if not restaurant:
        return f"Restaurant '{restaurant_name}' not found."
    
    existing = [r for r in reservations if r['restaurant'] == restaurant_name and r['datetime'] == date_time]
    total_reserved = sum(r['people'] for r in existing)
    if total_reserved + people > restaurant['capacity']:
        return f"Sorry, '{restaurant_name}' is fully booked at {date_time}. Try another time."
    
    return f"Yes, '{restaurant_name}' has availability at {date_time} for {people} people."

def make_reservation(restaurant_name, date_time, people, user_name):
    msg = check_availability(restaurant_name, date_time, people)
    if "fully booked" in msg:
        return msg

    reservations.append({
        "restaurant": restaurant_name,
        "datetime": date_time,
        "people": people,
        "user": user_name
    })
    return f"Reservation confirmed at '{restaurant_name}' on {date_time} for {people} guests, {user_name}!"

def recommend_restaurant(cuisine=None, area=None):
    filtered = restaurants
    if cuisine:
        filtered = [r for r in filtered if r['cuisine'].lower() == cuisine.lower()]
    if area:
        filtered = [r for r in filtered if r['area'].lower() == area.lower()]
    if not filtered:
        return "Sorry, no matching restaurants found."

    recommendation = random.choice(filtered)
    return f"Try '{recommendation['name']}' in {recommendation['area']} for amazing {recommendation['cuisine']} food!"
