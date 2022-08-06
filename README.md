# Web server for IoT component
This service allows RPi Pico (and other microboards using MicroPython) to connect to the AP.
Starts the webserver serving JSON data based on the defined template, which uses the data passed to the apConnector function.

# How to use it
## Add credentials
To connect to AP you need to pass username and password. File contains this informations is not stored in the repo for the security reason. It should be upload directy to the microboard. File should be named `secrets.py` and looks like below:
```
secrets = {
    'ssid' : 'SSID',
    'password' : 'PASSWORD'
}
```
## Add JSON response template
Web server respond in JSON format. Template of the response should be creted in the file named `response.json`. Keys should be exact like in the data passed to the `apConnector(data: object)` function.
```
{
    "temperature": 0,
    "humidity": "0%"
}
```
## Run web server and pass data
Tu start web servwer and connect to the AP you need to call `apConnector(data: object)` function. To do it import `apConnector(data: object)` function from `apConnector.py` file. This function takes as an argument an object containing the data to be inserted into the server's response in JSON format.
Object keys should be the same as those contained in the response template in `response.json` file.
```
from apConnector import apConnector

data = {
    "temperature": 28,
    "humidity": "65%"
}

apConnector(data)
```
An example of how this can be done is shown in the `start.py` file.
