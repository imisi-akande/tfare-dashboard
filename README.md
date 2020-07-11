# tfare-dashboard

This [web application](https://tfare-dashboard.herokuapp.com/) visualizes the trend of 
transport fare on five major routes in the States of Nigeria. Routes considered in this 
project are air, intracity, intercity, water and motorbikes.

## Instructions for local setup
- Enter your terminal

- Clone the project
    - ```git clone -b develop https://github.com/imisi-akande/tfare-dashboard.git```

- Change directory into the project folder
    - ```cd tfare-dashboard```

- Create a virtual environment
    - ```python -m venv tfare-env```

- Activate virtual environment
    - ```source tfare-env/bin/activate```

- Install the packages:
    - ```pip install -r requirements.txt```

- Set development environment
    - ```export FLASK_ENV=development```

-  Run the application
    - ```python tfare.py```

Transport Fare Watch (March 2020) data was obtained from the [National Bureau of Statistics](https://www.nigerianstat.gov.ng/elibrary?page=4&offset=30)

To see more about the initial data cleaning and preparation, visit this [link](https://github.com/imisi-akande/tfare-watch)

Have fun. Please Feel free to contact me if you encounter any issue.