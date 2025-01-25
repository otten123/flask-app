<<<<<<< HEAD
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    # HTML-Vorlage mit eingebettetem Python-Code
    html_template = """
    <!DOCTYPE html>
    <html lang="de">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Radios für den Bre</title>
        <style>
        body {
            font-family: Arial, sans-serif;
            background-image: url('/static/background.webp');
            background-size: cover;
            background-position: center;
            margin: 0;
            padding: 0;
            color: #ffffff;
        }
        .clickable-numbers {
            position: relative;
            width: 100%;
            height: 100vh; /* Volle Bildschirmhöhe für Testzwecke */
        }
        .number {
            position: absolute;
            display: block;
            background-color: rgba(255, 255, 255, 0); /* Rot für Debugging */
            cursor: pointer;
        }
        .number:hover {
            background-color: rgba(255, 255, 255, 0); /* Grün beim Hover */
        }
        </style>
    </head>
    <body>
        <h1>Radios, damit der Rattenjunge auch Baba Mucke hören kann</h1>
        <div class="clickable-numbers">
            <!-- Korrigierte Positionen der Links -->
            <a href="https://www.amazon.de/Jimtour-Bluetooth-Autoradio-Bildschirm-Carplay/dp/B0D8B91LLZ" class="number" style="top: 11%; left: 43%; width: 3%; height: 10%;"></a>
            <a href="https://www.amazon.de/Autoradio-Wireless-Touchscreen-Bluetooth-Rückfahrkamera-7-Inch/dp/B0DKF614G9" class="number" style="top: 9%; left: 48%; width: 3%; height: 10%;"></a>
            <a href="https://www.amazon.de/64G-Autoradio-Bluetooth-Bildschirm-Rückfahrkamera/dp/B0D3D2241T" class="number" style="top: 8%; left: 52%; width: 3%; height: 10%;"></a>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template)

if __name__ == "__main__":
=======
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    # HTML-Vorlage mit eingebettetem Python-Code
    html_template = """
    <!DOCTYPE html>
    <html lang="de">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Radios für den Bre</title>
        <style>
        body {
            font-family: Arial, sans-serif;
            background-image: url('/static/background.webp');
            background-size: cover;
            background-position: center;
            margin: 0;
            padding: 0;
            color: #ffffff;
        }
        .clickable-numbers {
            position: relative;
            width: 100%;
            height: 100vh; /* Volle Bildschirmhöhe für Testzwecke */
        }
        .number {
            position: absolute;
            display: block;
            background-color: rgba(255, 255, 255, 0); /* Rot für Debugging */
            cursor: pointer;
        }
        .number:hover {
            background-color: rgba(255, 255, 255, 0); /* Grün beim Hover */
        }
        </style>
    </head>
    <body>
        <h1>Radios, damit der Rattenjunge auch Baba Mucke hören kann</h1>
        <div class="clickable-numbers">
            <!-- Korrigierte Positionen der Links -->
            <a href="https://www.amazon.de/Jimtour-Bluetooth-Autoradio-Bildschirm-Carplay/dp/B0D8B91LLZ" class="number" style="top: 11%; left: 43%; width: 3%; height: 10%;"></a>
            <a href="https://www.amazon.de/Autoradio-Wireless-Touchscreen-Bluetooth-Rückfahrkamera-7-Inch/dp/B0DKF614G9" class="number" style="top: 9%; left: 48%; width: 3%; height: 10%;"></a>
            <a href="https://www.amazon.de/64G-Autoradio-Bluetooth-Bildschirm-Rückfahrkamera/dp/B0D3D2241T" class="number" style="top: 8%; left: 52%; width: 3%; height: 10%;"></a>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template)

if __name__ == "__main__":
>>>>>>> aa210f568eb3fdc609835eea1a6f3f19da4ccb87
    app.run(debug=True)