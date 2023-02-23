from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, this is my first python server"

@app.route("/armstrong/<int:n>")
def armstrong(n):
    temp = n
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    # display the result
    if n == sum:
       result = {
           "Number" : n,
           "isArmstrong" : True
       }
    else:
        result = {
            "Number": n,
            "isArmstrong": False
        }

    return jsonify(result)



if __name__ == "__main__":
    app.run(debug=True)