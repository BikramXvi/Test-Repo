# -------------------- IMPORTS -------------------- #
import requests  # used to send HTTP requests to weather API
import tkinter as tk  # used to create GUI application
from tkinter import messagebox  # used for popup error/info messages


# -------------------- API KEY -------------------- #
# Unique key provided by OpenWeatherMap to access weather data
API_KEY = "74decccaa3c8f65b7dbed9a5584dbc7a"


# -------------------- FUNCTION: GET WEATHER -------------------- 
def get_weather():
    """
    This function is called when user clicks the Search button.
    It fetches weather data from OpenWeather API and updates GUI.
    """

    # Get city name from input box and remove extra spaces
    city = entry_city.get().strip()

    # Validate input (empty check)
    if city == "":
        messagebox.showerror("Error", "Please enter a city name")
        return

    # Build API request URL dynamically using user input
    url = (
        "https://api.openweathermap.org/data/2.5/weather?q="
        + city +
        "&appid=" + API_KEY +
        "&units=metric"
    )

    try:
        # Send request to API
        response = requests.get(url)

        # Convert JSON response into Python dictionary
        data = response.json()

        # Check if request was successful (HTTP code 200)
        if str(data["cod"]) == "200":

            # ---------------- Extract required data ---------------- #
            temperature = data["main"]["temp"]  # current temperature
            humidity = data["main"]["humidity"]  # humidity percentage
            weather = data["weather"][0]["description"]  # weather condition text
            wind_speed = data["wind"]["speed"]  # wind speed

            # ---------------- Update GUI labels ---------------- #
            val_city.config(text=city)
            val_temp.config(text=str(temperature) + " °C")
            val_humidity.config(text=str(humidity) + " %")
            val_wind.config(text=str(wind_speed) + " m/s")
            val_condition.config(text=weather)

        else:
            # Show API error message (like city not found)
            messagebox.showerror("Error", data["message"])

    except:
        # Handles network errors, API failure, or invalid response
        messagebox.showerror("Error", "Network or API error")


# -------------------- MAIN WINDOW SETUP -------------------- #
window = tk.Tk()  # create main application window
window.title("Weather App")  # set window title
window.geometry("420x300")  # set fixed window size
window.resizable(False, False)  # disable resizing for clean layout


# -------------------- TOP INPUT SECTION -------------------- #
top_frame = tk.Frame(window, pady=10)  # container for input section
top_frame.pack()  # place frame in window

# App title label
title = tk.Label(
    top_frame,
    text="Weather App",
    font=("Arial", 18, "bold")
)
title.grid(row=0, column=0, columnspan=2, pady=5)

# Input field for city name
entry_city = tk.Entry(top_frame, font=("Arial", 12), width=25)
entry_city.grid(row=1, column=0, padx=5)

# Search button triggers API call
btn = tk.Button(top_frame, text="Search", command=get_weather)
btn.grid(row=1, column=1, padx=5)


# -------------------- RESULT DISPLAY SECTION -------------------- #
result_frame = tk.Frame(window, padx=20, pady=20)  # container for output
result_frame.pack()


# Helper function to create label titles (left column)
def row(label_text, row):
    """
    Creates left-side labels (like City, Temperature, etc.)
    to avoid repeating code.
    """
    tk.Label(
        result_frame,
        text=label_text,
        font=("Arial", 11, "bold")
    ).grid(row=row, column=0, sticky="w", pady=3)


# Static labels (left side)
row("City:", 0)
row("Temperature:", 1)
row("Humidity:", 2)
row("Wind Speed:", 3)
row("Condition:", 4)


# -------------------- DYNAMIC VALUE LABELS -------------------- #
# These labels get updated when API response is received

val_city = tk.Label(result_frame, text="-", font=("Arial", 11))
val_city.grid(row=0, column=1, sticky="w")

val_temp = tk.Label(result_frame, text="-", font=("Arial", 11))
val_temp.grid(row=1, column=1, sticky="w")

val_humidity = tk.Label(result_frame, text="-", font=("Arial", 11))
val_humidity.grid(row=2, column=1, sticky="w")

val_wind = tk.Label(result_frame, text="-", font=("Arial", 11))
val_wind.grid(row=3, column=1, sticky="w")

val_condition = tk.Label(result_frame, text="-", font=("Arial", 11))
val_condition.grid(row=4, column=1, sticky="w")


# -------------------- START APPLICATION LOOP -------------------- #

window.mainloop()