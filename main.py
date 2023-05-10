# Complete project details at https://RandomNerdTutorials.com
from boot import *


def web_page():
    # print(led_rouge.value == 1)

    if led_rouge.value() == 1:
        led_rouge_state = "ON"
    else:
        led_rouge_state = "OFF"
    if led_blanche.value() == 1:
        led_blanche_state = "ON"
    else:
        led_blanche_state = "OFF"
    if led_bleu.value() == 1:
        led_bleu_state = "ON"
    else:
        led_bleu_state = "OFF"
    if led_jaune.value() == 1:
        led_jaune_state = "ON"
    else:
        led_jaune_state = "OFF"
    pot_rouge_state = str(pot_rouge.read())
    pot_blanc_state = str(pot_blanc.read())
    pot_bleu_state = str(pot_bleu.read())
    watersensor_state = str(watersensor.read())

    html = """
<html>
<head><title>ESP Web Server</title>
    <meta http-equiv="refresh" content="5">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,">
    <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
    h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none;
    border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
    .button2{background-color: #4286f4;}
    </style>
</head>
<body><h1>ESP Web Server</h1>
<table>
    <tr>
        <td>
            <p>LED Rouge state: <strong>""" + led_rouge_state + """</strong></p>
            <p>POTENTIOMETER state: <strong>""" + pot_rouge_state + """</strong></p>
            <p><a href="/?led_Rouge=on">
                <button class="button">ON</button>
            </a></p>
            <p><a href="/?led_Rouge=off">
                <button class="button button2">OFF</button>
            </a></p>
        </td>
        <td>
            <p>LED Blanche state: <strong>""" + led_blanche_state + """</strong></p>
            <p>POTENTIOMETER state: <strong>""" + pot_blanc_state + """</strong></p>
            <p><a href="/?led_Blanche=on">
                <button class="button">ON</button>
            </a></p>
            <p><a href="/?led_Blanche=off">
                <button class="button button2">OFF</button>
            </a></p>
        </td>
    </tr>
    <tr>
        <td>
            <p>LED Bleu state: <strong>""" + led_bleu_state + """</strong></p>
            <p>POTENTIOMETER state: <strong>""" + pot_bleu_state + """</strong></p>
            <p><a href="/?led_Bleu=on">
                <button class="button">ON</button>
            </a></p>
            <p><a href="/?led_Bleu=off">
                <button class="button button2">OFF</button>
            </a></p>
        </td>
        <td>
            <p>LED Jaune state: <strong>""" + led_jaune_state + """</strong></p>
            <p>WATER SENSOR state: <strong>""" + watersensor_state + """</strong></p>
            <p><a href="/?led_Jaune=on">
                <button class="button">ON</button>
            </a></p>
            <p><a href="/?led_Jaune=off">
                <button class="button button2">OFF</button>
            </a></p>
        </td>
    </tr>
</table>
</body>
</html>

"""

    return html


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
print("Wait connection")
while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    # print('Content = %s' % request)
    led_rouge_on = request.find('/?led_Rouge=on')
    led_rouge_off = request.find('/?led_Rouge=off')
    if led_rouge_on == 6:
        print('LED rouge ON')
        led_rouge.value(1)
    if led_rouge_off == 6:
        print('LED rouge OFF')
        led_rouge.value(0)

    led_blanche_on = request.find('/?led_Blanche=on')
    led_blanche_off = request.find('/?led_Blanche=off')
    if led_blanche_on == 6:
        print('LED blanche ON')
        led_blanche.value(1)
    if led_blanche_off == 6:
        print('LED blanche OFF')
        led_blanche.value(0)

    led_bleu_on = request.find('/?led_Bleu=on')
    led_bleu_off = request.find('/?led_Bleu=off')
    if led_bleu_on == 6:
        print('LED bleu ON')
        led_bleu.value(1)
    if led_bleu_off == 6:
        print('LED bleu OFF')
        led_bleu.value(0)

    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
