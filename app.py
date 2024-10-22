import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==



# Request:
# GET /hello?name=David

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args['name'] # The value is 'David'

    # Send back a friendly greeting with the name
    return f"Hello {name}!"

# To make a request, run:
# curl "http://localhost:5001/hello?name=David"



# Request:
# POST /goodbye
#   With body parameter: name=Alice

@app.route('/goodbye', methods=['POST'])
def goodbye():
    name = request.form['name'] # The value is 'Alice'

    # Send back a fond farewell with the name
    return f"Goodbye {name}!"

# To post, run:
#  curl -X POST -d "name=Alice" http://localhost:5001/goodbye


# Request:
# POST /submit
#  With body parameter: name=Leo, message:"Hello world"

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name'] # Leo
    message = request.form['message'] # Hello world
    return f'Thanks {name}, you sent this message: "{message}"'

# To post, run:
#  curl -X POST -d "name=Leo&message=Hello world" http://localhost:5001/submit


# Request:
# GET /wave?name=Leo
#  with body paremeter: name=Leo
# Expected response (200 OK): I am waving at Leo

@app.route('/wave', methods=['GET'])
def wave():
    name = request.args['name'] # Leo
    return f"I am waving at {name}"

# To post, run:
# curl -X POST -d "name=Leo" http://localhost:5001/wave


# Request:
# POST /count_vowels
#   with body parameter: text=word

@app.route('/count_vowels', methods=["POST"])
def count_vowels():
    text = request.form['text']
    vowel_count = 0
    for letter in text:
        if letter in 'aeiouAEIOU':
            vowel_count += 1
    return f'There are {vowel_count} vowels in "{text}"'

# to post, run:
# curl -X POST -d "text=moodswings" http://localhost:5001/count_vowels


# Request:
# POST http://localhost:5001/sort_names
#   With body parameters: names=Joe,Alice,Zoe,Julia,Kieran
# Expected response (sorted list of names): Alice,Joe,Julia,Kieran,Zoe

@app.route('/sort_names', methods=['POST'])
def sort_names():
    names = request.form['names']
    name_list = names.split(',')
    sorted_names = sorted(name_list)
    return ",".join(sorted_names)

# Request:
# GET /add_names?add=Eddie
# This route should return a list of pre-defined names, plus the name given.
# Expected response (2OO OK): Julia, Alice, Karim, Eddie

@app.route('/add_names', methods=['GET'])
def add_names():
    name = request.args['name']
    return f"Julia, Alice, Karim, {name}"


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))




