
from flask import Flask, render_template, request, jsonify

from main import *

app = Flask(__name__)


@app.route("/")
def Home():
    return ('''
        <head>
          <script src="https://cdn.tailwindcss.com"></script>
        </head> 
        <div class="container p-8">
            <h1 class="text-2xl font-semibold mb-4">Login</h1>
            <form action="/bezoeker">
                <div class="mb-4">
                    <label for="username" class="block text-gray-600 text-sm font-medium mb-2">Username</label>
                    <input type="text" id="username" name="username" class="w-full p-2 border rounded focus:outline-none focus:border-blue-500">
                </div>
                <div class="mb-4">
                    <label for="password" class="block text-gray-600 text-sm font-medium mb-2">Password</label>
                    <input type="password" id="password" name="password" class="w-full p-2 border rounded focus:outline-none focus:border-blue-500">
                </div>
                <button type="submit" class="w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-600 focus:outline-none focus:shadow-outline-blue">Login</button>
            </form>
        </div>
        
    ''')


@app.route('/bezoeker')
def Bezoeker():
    return render_template("bezoeker.html", bezoekers=bezoekers,  presentaties=presentaties)


@app.route('/organisator')
def Organisator():
    return 'Organisator pagina'


# @app.route('/call_python_function', methods=['POST'])
# def call_python_function(parameter):
#     print("Received parameter:", parameter)

#     print("kahsjd")
#     # result = bezoeker_toevoegen_aan_presentatie()
#     print("result")
#     # print(result)
#     # return result
#     return None


@app.route('/call_python_function', methods=['POST'])
def call_python_function():
    data = request.json
    presentatie_id = data.get('presentatieId')
    bezoeker_id = data.get('bezoekerId')

    # Do something with the values

    bezoeker_toevoegen_aan_presentatie(
        bezoeker_id=bezoeker_id, presentatie_id=presentatie_id)

    return jsonify({
        "status": "success",
        "presentatieId": presentatie_id,
        "bezoekerId": bezoeker_id
    })
