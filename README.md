# WeatherAppGUI

WeatherAppGUI is a Python application with a graphical user interface (GUI) built using Tkinter. It retrieves and displays weather information for a specified city using the OpenWeatherMap API.

## Features

- Fetches current weather data for a given city.
- Displays city name, temperature, weather description, humidity, and wind speed.
- Allows users to search for cities in a local JSON file.

## Requirements

- Python 3.x
- `requests` library
- `tkinter` library (included with standard Python installations)
- A JSON file (`city.list.json`) containing a list of city names

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/saksham342/WeatherAppGUI.git
    cd WeatherAppGUI
    ```

2. Install the required dependencies:

    ```sh
    pip install requests
    ```

3. Ensure you have a `city.list.json` file in the project directory. This file should contain a list of city names.

## Usage

1. Obtain your API key from [OpenWeatherMap](https://openweathermap.org/api).

2. Replace `"your_api_key_here"` with your actual API key in the `main` function.

3. Run the application:

    ```sh
    python weather_app_gui.py
    ```

4. Enter the name of the city when prompted, or search for a city from the list.

## Code Explanation

The application is structured into several classes:

- `Weather`: Handles the interaction with the OpenWeatherMap API.
- `WeatherData`: Represents the weather data and provides a method to format it for display.
- `WeatherAppGUI`: Manages the GUI, including user input and displaying weather data.

### Weather Class

- `__init__(self, api_key)`: Initializes the class with the API key.
- `get_weather_data(self, city)`: Fetches weather data for the specified city from the OpenWeatherMap API.

### WeatherData Class

- `__init__(self, data)`: Initializes the class with the weather data.
- `format_display(self)`: Returns a formatted string of the weather information.

### WeatherAppGUI Class

- `__init__(self, master, api_key)`: Initializes the class with the Tkinter master and the weather API object.
- `create_widgets(self)`: Creates the GUI widgets.
- `load_city_data(self)`: Loads city data from a JSON file.
- `search_city(self)`: Searches for cities in the list based on user input.
- `search_weather(self)`: Fetches and displays the weather data for the specified city.

### main Function

- Initializes the `WeatherAppGUI` with the provided API key and runs the application.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
