import tkinter as tk
import requests
import time
import sqlite3

# Create/connect to the database
conn = sqlite3.connect('price_data.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS prices
             (product text, amazon_price real, google_price real)''')

def insert_into_db(product, amazon_price, google_price):
    c.execute("INSERT INTO prices VALUES (?, ?, ?)", (product, amazon_price, google_price))
    conn.commit()

def search():
    product = product_entry.get()

    url = "https://price-analytics.p.rapidapi.com/search-by-term"

    payload = {
        "source": "google",
        "country": "in",
        "values": product
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "b3d1423e7bmsh64ac78ee3adc8ddp10ef9djsn48535059df90",
        "X-RapidAPI-Host": "price-analytics.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)

    googleid = response.json()['job_id']

    payload = {
        "source": "amazon",
        "country": "in",
        "values": product
    }

    response = requests.post(url, data=payload, headers=headers)

    amzid = response.json()['job_id']
    print(googleid, amzid)

    # Amazon
    time.sleep(120)

    url = f"https://price-analytics.p.rapidapi.com/poll-job/{googleid}"

    headers = {
        "X-RapidAPI-Key": "b3d1423e7bmsh64ac78ee3adc8ddp10ef9djsn48535059df90",
        "X-RapidAPI-Host": "price-analytics.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    result = response.json()
    print(result)
    amazon_price = result["results"][0]['content']['offers'][0]['price']
    amazon_label.config(text=f"Amazon Price: {amazon_price}")
    
    # Google
    url = f"https://price-analytics.p.rapidapi.com/poll-job/{amzid}"

    response = requests.get(url, headers=headers)

    result = response.json()

    google_price = result["results"][0]['content']['offers'][0]['price']
    google_label.config(text=f"Google Price: {google_price}")
    
    # Insert data into the database
    insert_into_db(product, amazon_price, google_price)

# GUI
root = tk.Tk()
root.title("Price Comparison")

product_label = tk.Label(root, text="Enter product to search:")
product_label.pack()

product_entry = tk.Entry(root)
product_entry.pack()

search_button = tk.Button(root, text="Search", command=search)
search_button.pack()

amazon_label = tk.Label(root, text="Amazon Price: ")
amazon_label.pack()

google_label = tk.Label(root, text="Google Price: ")
google_label.pack()

root.mainloop()

# Close the database connection
conn.close() 
