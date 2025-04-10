# 1. What is Exception Handling?
# Kabhi kabhi code likhte hue kuch unexpected cheezein ho jaati hain, jaise number ko zero se divide kar diya, ya file hi nahi mili — is tarah ki situations ko “exception” kehte hain.

# Exception handling ka matlab hai aise errors ko pyaar se handle karna taake program crash na kare aur user ko proper message mile.

# 🔹 2. Keywords used in Exception Handling:

# ✅ try:
# Ye block un lines ke liye hota hai jahan error aa sakta hai.

# try:
    # yahan risky code aata hai

# ✅ except:
# Agar try block mein error aata hai toh except block usay handle karta hai.

# except:
#     # error handle karte hain

# ✅ else:
# Agar try block bilkul sahi chalta hai (koi error nahi aata) toh else block chalta hai

# else:
    # sab sahi chala toh ye chalega

# ✅ finally:
# Ye block hamesha chalta hai, chahe error aaye ya na aaye

# finally:
    # clean up ya closing ka kaam


# 3: 💡 Example: Online Food Order Experience

try:
    print("You placed an online food order 🍔")
    order_status= "confirmed" # imagine yahan error aata toh except chalega
    print("Food is being prepared....")
except:
         print("Oops! Something went wrong with your order 🚫")
else:
    print("Your food is on the way! 🚚")
finally:
    print("Thanks for using our food app. Have a great day! 😊")   

# 🔹 4. raise keyword:         
# Kabhi kabhi hum khud se error raise karna chahte hain. Uske liye raise use hota hai.

age = int(input("Enter your age: "))
if age< 0:
     raise ValueError("Age cannot be negative")

# 🔹 5. Custom Exceptions:
# Apna khud ka error class banake bhi exception handle kar sakte hain.

class TooyoungError(Exception):
     pass 
age = 10
if age< 18:
     raise TooyoungError("You are too young to vote!")

# ✅ Summary:
# try — risk le lo

# except — agar error aaya toh sambhal lo

# else — sab smooth chala toh reward milega

# finally — chahe kuch bhi ho, ye toh chalega hi

# raise — khud se error uthao