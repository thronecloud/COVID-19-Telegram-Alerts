# COVID-19-Telegram-Alerts
The Telegram bot is built in Python which sends messages to channel. 

The bot is built using Python 3.6

The bot utlizies API data from covid19india.org's API and is able to send alerts to a channel on Telegram. 
Currently the bot is set to send alerts to Telegram channel - @coronagzb and is tracking cases of Ghaziabad, Lucknow, and India.

Bot can be configured to send alerts for any other district as well.

Requests library is used for API calls and JSON response is later parsed and sent via Telegram API. 
