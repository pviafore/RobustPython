import datetime

from dataclasses import dataclass
from typing import Any, List, Dict, Set, Union

notifications: list[Any] = []

Dish = str
Ingredient = str

@dataclass
class NewSpecial:
    dish: Dish
    start_date: datetime.datetime
    end_date: datetime.datetime

@dataclass
class IngredientsOutOfStock:
    ingredients: set[Ingredient]

@dataclass
class IngredientsExpired:
    ingredients: set[Ingredient]

@dataclass
class NewMenuItem:
    dish: Dish

Notification = Union[NewSpecial, IngredientsOutOfStock, IngredientsExpired, NewMenuItem]


@dataclass
class Text:
    phone_number: str

@dataclass
class Email:
    email_address: str

@dataclass
class SupplierAPI:
    pass

NotificationMethod = Union[Text, Email, SupplierAPI]

def notify(notification_method: NotificationMethod, notification: Notification):
    if isinstance(notification_method, Text):
        send_text(notification_method, notification)
    elif isinstance(notification_method, Email):
        send_email(notification_method, notification)
    elif isinstance(notification_method, SupplierAPI):
        send_to_supplier(notification)
    else:
        raise ValueError("Unsupported Notification Method")

def send_text(text: Text, notification: Notification):
    if isinstance(notification, NewSpecial):
        # ... snip send text ...
        pass
    elif isinstance(notification, IngredientsOutOfStock):
        # ... snip send text ...
        pass
    elif isinstance(notification, IngredientsExpired):
        # ... snip send text ...
        pass
    elif isinstance(notification, NewMenuItem):
        # .. snip send text ...
        pass
    raise NotImplementedError("Notification method not supported")

def send_email(email: Email, notification: Notification):
    # .. similar to send_text ...
    global notifications
    if isinstance(notification, IngredientsExpired):
        # ... snip send text ...
        notifications.append((email.email_address, notification.ingredients))
    if isinstance(notification, NewMenuItem):
        # ... snip send text ...
        notifications.append((email.email_address, notification.dish))


def send_to_supplier(notification: Notification):
    # .. similar to send_text
    global notifications
    if isinstance(notification, IngredientsExpired):
        # ... snip send text ...
        notifications.append(("supplier", notification.ingredients))

users_to_notify: dict[type, list[NotificationMethod]] = {
    NewSpecial: [SupplierAPI(), Email("boss@company.org"), Email("marketing@company.org"), Text("555-2345")],
    IngredientsOutOfStock: [SupplierAPI(), Email("boss@company.org")],
    IngredientsExpired: [SupplierAPI(), Email("boss@company.org")],
    NewMenuItem: [Email("boss@company.org"), Email("marketing@company.org")]
}

def send_notification(notification: Notification):
    try:
        users = users_to_notify[type(notification)]
    except KeyError:
        raise ValueError("Unsupported Notification Method")
    for user in users:
        notify(user, notification)


send_notification(NewMenuItem("Pasta"))
assert notifications == [("boss@company.org", "Pasta"), ("marketing@company.org", "Pasta")]

notifications = []

send_notification(IngredientsExpired({"Tomato", "Garlic"}))

assert notifications == [("supplier", {"Tomato", "Garlic"}), ("boss@company.org", {"Tomato", "Garlic"})]
