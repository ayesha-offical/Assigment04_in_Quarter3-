# 🟢 1. Stonehenge – Time Ka Pehla Tareeqa (simple easy to understand)

# Explanation:
# Stonehenge aik purana pathar ka structure hai jo England mein hai.
# Log is se waqt aur mausam ka pata lagate thay. Jab sooraj ek khaas jagah par chamakta tha, wo samajh jaate ke summer ya winter aane wala hai.

# Use:
# ➡️ Yeh time dekhne ka pehla tareeqa tha – bina clock ke!

# 🟢 2. Epoch – Computer ka Zero Time

# Explanation:
# Epoch ka matlab hai starting point of time.
# Computer ke liye yeh hota hai:

# 🗓️ 1 January 1970

import time
print(time.time())

# Output:
# 1970 se le kar ab tak ke seconds.

# Use:
# ➡️ Jab bhi hum current time ya kisi bhi cheez ka duration nikalte hain, Python is point se count karta hai.

# 🟢 3. time.localtime() & time.asctime()

import time 
(time.localtime())  # Detail form
print(time.asctime(time.localtime())) # Simple readable form

# Use:
# ➡️ Abhi ka exact waqt dekhne ke liye
# ➡️ asctime → “Tue Apr 9 14:30:00 2025” jese output deta hai

# 🟢 4. calendar module – Calendar Print Karna

import calendar
print(calendar.month(2025, 4)) # April 2025 ka calendar

# Output:
# April 2025 ka pura calendar terminal mein dikhayega.

# Use:
# ➡️ Jab kisi month ke din aur weeks dekhne ho.


#  🟢 5. datetime module – Date & Time Fancy Format Mein

from datetime import datetime
now = datetime.now()

print(now.strftime("%A")) # day name
print(now.strftime("%B")) # month name
print(now.strftime("%Y")) # year

# Use:
# ➡️ Date aur time ko pretty format mein dikhana
# ➡️ Reports, projects, apps mein use hota hai

# 🟢 6. math module – Maths Helper in Python

import math
print(abs(-10))# 10
print(pow(2,3)) # 8
print(math.sqrt(25)) # 5.0
print(round(2.6))  # 3

# ✅ Special Concepts:

print(math.inf) # Infinity
print(float('nan')) # Not a Number


# Use:
# ➡️ Jab mathematical calculation karni ho
# ➡️ NaN ya infinity tab aata hai jab answer impossible ho (e.g. divide by zero)


# ✨ Conclusion:
# Module	Kaam
# time	Time dekhna, duration nikalna
# calendar	Mahine ka calendar dekhna
# datetime	Date/time ko readable format mein dikhana
# math	Maths ke important functions jaise power, root