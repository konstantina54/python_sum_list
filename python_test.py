"""This is a script creating a REST endpoint that displays sum of all list items.
 I needed to import flask and jsonify libraries. Then I added the url for the result page.
 I ran a loop through the list and added every item to a total variable that was zeroed at the beginning.
 At the end the result is added to json object as response.
 I added simple test list to see that the calculation is working correct.
 The loop can be transferred in a function if it will be used in different cases."""


from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def start():
    return "Hi Welcome to python test. You can find result at http://127.0.0.1:5000/total  "


@app.route('/total', methods=['GET'])
def total():
    numbers_to_add = list(range(10000001))
    # numbers_to_add = [1,2,3]
    total = 0
    for i in numbers_to_add:
        total += i
    # print(total)
    return jsonify({'total': total})


if __name__ == '__main__':
    app.run(debug=True)


