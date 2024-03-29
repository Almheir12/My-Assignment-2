#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import datetime   #importing date time
from PurchaseTicket import PurchaseTicket # importing purchase ticket class
from Visitor import Visitor  # importing visitor class

# Get visitor's name from user
visitor_name = input("Enter visitor's name: ")

# Get visitor's age from user
visitor_age = int(input("Enter visitor's age: "))

# Get visitor's category from user
visitor_category = input("Enter visitor's category (Adult/Child/Senior/Student/Teacher): ")

# Ticket price and VAT rate
ticket_price = 63  # Assuming the ticket price is 63 AED
vat_rate = 0.05  # 5% VAT rate

# Create a Visitor object with the given name, age, and category
visitor = Visitor(visitorId=1, visitorName=visitor_name, visitorAge=visitor_age, visitorCatagory=visitor_category)

# Create a new PurchaseTicket object with the visitor details
ticket = PurchaseTicket(
    ticketId=1,
    event_type="Special Event",
    price=ticket_price,
    dateOfPurchase=datetime.now(),
    visitor=visitor  # Pass the Visitor object
)

# Calculate the final price including VAT based on visitor details
if visitor_category == "Adult":
    # Adults pay full price
    final_price = ticket_price * (1 + vat_rate)
elif visitor_category in ["Child", "Senior", "Student", "Teacher"]:
    # Children, seniors, students, and teachers get a free ticket
    final_price = 0
else:
    # Other visitor categories get a 50% discount
    final_price = ticket_price * 0.5 * (1 + vat_rate)

# Print visitor details and the final bill
print(f"Visitor Name: {visitor_name}")
print(f"Visitor Age: {visitor_age}")
print(f"Visitor Category: {visitor_category}")
print(f"Final Bill After VAT (5%): {final_price}")


# In[ ]:





# In[ ]:




