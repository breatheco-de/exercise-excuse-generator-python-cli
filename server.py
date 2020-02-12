import os
import random
import math
from flask import Flask
from flask import send_from_directory


def html(code):
    return code.replace('--html', '').replace('--!html', '')

app = Flask(__name__)


def generate_excuse():
    # array with the words
    first = 'A '
    adj = ['two headed ', 'nuclear ', 'angry ', 'lonely ','crazy ','glowing ','smelly ','slow ','old ' ]
    noun = ['jogger ','racoon ','dog ', 'merchant ', 'driver ', 'comedian ', 'pinecone ']
    action = ['took my ', 'threw my ', 'yelled at my ' , 'kicked my ', 'stole my ', 'burned my ', 'bit my ', 'hit my ']
    possetion = ['toe ', 'car ', 'watch ', 'shoe ', 'wallet ', 'shirt ', 'keys ', 'computer ', 'phone ', 'sandwich ']
    where = ['on the street','in my house','in my driveway', 'in front of the office', 'near the mall', 'near the toilet', 'at the bus station']

    # declaring random variables
    rdm1 = math.floor(random.randint(1, len(adj)))
    rdm2 = math.floor(random.randint(1, len(noun)))
    rdm3 = math.floor(random.randint(1, len(action)))
    rdm4 = math.floor(random.randint(1, len(possetion)))
    rdm5 = math.floor(random.randint(1, len(where)))

    # creating a sentence (the excuse)
    return first + adj[rdm1 - 1] + noun[rdm2 - 1] + action[rdm3 - 1] + possetion[rdm4 - 1] + where[rdm5 - 1]

# Serving the index file
@app.route('/', methods=['GET'])
def home():
    excuse = generate_excuse()
    return html(f'''--html
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8">

            <title>The HTML5 Herald</title>
            <meta name="description" content="The HTML5 Herald">
            <meta name="author" content="SitePoint">

            <link rel="stylesheet" href="css/styles.css?v=1.0">

        </head>

        <body>
            <p>Excuse: {excuse}</p>
        </body>
    </html>
--!html''')

app.run(host='0.0.0.0',port=3000, debug=True)