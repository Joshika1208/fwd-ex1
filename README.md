# EX01 Developing a Simple Webserver
## Date:11/11/2026
## Name : JOSHIKA S
## Reg no : 26006014

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:

```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
    <title>TCP/IP Protocol Suite</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f8ff;
            text-align: center;
        }

        h1 {
            color: darkblue;
        }

        table {
            margin: auto;
            border-collapse: collapse;
            width: 70%;
            background-color: white;
        }

        th, td {
            border: 1px solid black;
            padding: 12px;
            text-align: center;
        }

        th {
            background-color: navy;
            color: white;
        }

        tr:nth-child(even) {
            background-color: #dbeafe;
        }

        tr:hover {
            background-color: lightyellow;
        }
    </style>
</head>

<body>

    <h1>TCP/IP Protocol Suite</h1>
    <h3>List of Protocols in TCP/IP Model</h3>

    <table>
        <tr>
            <th>Layer</th>
            <th>Protocols</th>
        </tr>

        <tr>
            <td>Application Layer</td>
            <td>HTTP, HTTPS, FTP, SMTP, DNS, DHCP, Telnet, SSH, POP3</td>
        </tr>

        <tr>
            <td>Transport Layer</td>
            <td>TCP, UDP</td>
        </tr>

        <tr>
            <td>Internet Layer</td>
            <td>IP, ICMP, IGMP, ARP</td>
        </tr>

        <tr>
            <td>Network Access Layer</td>
            <td>Ethernet, Wi-Fi, PPP</td>
        </tr>
    </table>

</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',880)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()

```


## OUTPUT:
![alt text](<Screenshot (13).png>)

![alt text](<Screenshot (11).png>)

## RESULT:
The program for implementing simple webserver is executed successfully.

