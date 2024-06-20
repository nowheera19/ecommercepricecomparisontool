**Price Comparison Tool**
**Description**
The Price Comparison Tool is a Python application that compares product prices between Amazon and Google. It uses the RapidAPI Price Analytics API to fetch and display the prices of a given product from both platforms. The tool also stores the price data in an SQLite database.

**Features**
*Graphical User Interface (GUI)*: Built with Tkinter for user-friendly interaction.
*API Integration*: Uses the RapidAPI Price Analytics API to fetch prices from Amazon and Google*.
*Data Storage*: Stores product price data in an SQLite database for future reference.

**Intallation**
1.clone the repository: git clone https://github.com/yourusername/price-comparison-tool.git
cd price-comparison-tool
2.Install the required Python packages:
pip install requests tk sqlite3

**Code Overview**
*GUI Setup*: The GUI is created using Tkinter with input fields and buttons to search for product prices.
*API Requests*: The search function sends requests to the RapidAPI Price Analytics API to get price data from Amazon and Google.
*Database Interaction*: The tool connects to an SQLite database (price_data.db) and inserts the fetched price data.

**API Configuration**
Make sure to replace the X-RapidAPI-Key with your own API key from RapidAPI.
