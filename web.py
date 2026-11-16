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