from meican.models import Restaurant, Tab, Dish, Section


def get_tabs(data):
    """
    :type data: dict
    :rtype: list[meican.models.Tab]
    """
    tabs = []
    for day in data["dateList"]:
        tabs.extend([Tab(_) for _ in day["calendarItemList"]])
    return tabs


def get_restaurants(tab, data):
    """
    :type tab: meican.models.Tab
    :type data: dict
    :rtype: list[meican.models.Restaurant]
    """
    restaurants = []
    for restaurant_data in data["restaurantList"]:
        restaurants.append(Restaurant(tab, restaurant_data))
    return restaurants


def get_dishes(restaurant, data):
    """
    :type restaurant: meican.models.Restaurant
    :type data: dict
    :rtype: list[meican.models.Dish]
    """
    sections = {}
    for section_data in data.get("sectionList", []):
        section = Section(section_data)
        sections[section.id] = section
    dishes = []
    for dish_data in data["dishList"]:
        if dish_data.get("isSection", False) or dish_data.get("priceString") is None:
            continue
        dishes.append(Dish(restaurant, dish_data, sections))
    return dishes
