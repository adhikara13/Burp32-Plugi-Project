# Burp Suite Base32 Encoder Plugin
This is a simple plugin for Burp Suite that encodes HTTP requests in Base32 format.

## Installation
1. Download the burp32.py file to your computer.
2. Open Burp Suite and go to the "Extender" tab.
3. Click on the "Extensions" tab and then click the "Add" button.
4. In the "Extension Details" dialog, select "Python" as the extension type and browse to the burp32.py file.
5. Click "Next" and then "Finish".

## Usage
To encode an HTTP request in Base32 format, right-click on the request in the "Proxy" tab and select "Encode request in Base32" from the context menu.

The encoded request will be printed to the Burp Suite output console and the request in the "Proxy" tab will be updated with the encoded request.
