# CryptoMonitor
Simple python app to monitor cryptocurrency and send mobile notification via IFTTT. No need for complex server setup.

### Table of Contents

  * [Setup IFTTT](#setup-ifttt)
  * [Starting The Monitor](#starting-the-monitor)

### Setup IFTTT

  * Create IFTTT account
    * Go to http://ifttt.com and sign up using a gmail account (since we're using gmail server in the code)
    * Note make sure to use the same email for your smtp server
  * Create Applet
    * Go to https://ifttt.com/create
    * Click on +this
    * Search for "Email" then click the Email tile
    * Choose "Send IFTTT and email"
    * Click on +that
    * Search for "Notifications" then click the Notifications tile
    * Click Connect
    * Click the trigger and edit the details.
  * Download the IFTTT mobile app iOS/Android

### Starting The Monitor

  * Download monitor_http.py
  * Run it using `python monitor_http.py`

<img src="https://github.com/EliHar/CryptoMonitor/blob/master/img/example.jpg"/>
