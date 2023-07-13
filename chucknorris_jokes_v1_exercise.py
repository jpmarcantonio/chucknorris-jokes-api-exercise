"""
Write a script that will call Chucknorris Jokes api and print jokes to the console.
The number of jokes to display should be a command line argument.
Each joke on the console should be separated by a line.

URL: https://api.chucknorris.io/jokes/random
Method: GET

Information about the API: https://api.chucknorris.io

Example command to display 3 jokes:
    $ checknorris_jokes_v1_exercise.py 3

Example command to display 10 jokes:
    $ checknorris_jokes_v1_exercise.py 10


Example output.

    (my_venv) admas@/.../chucknorris_jokes_v1_exercise : python chucknorris_jokes_v2_solution.py 3
    Here are 3 Chucknorris jokes
    -------------------------------------------
    * During the Japan Tsunami a UFO was spotted flying out of the water.Recent news report Chuck Norris piloted the object. That object was his leg.
    -------------------------------------------
    * Chuck Norris can eat chicken noodle soup with a knife.
    -------------------------------------------
    * No one can be sure what Chuck Norris looking at, only that it has 5 seconds left to live
"""
import requests
import sys

arguments = sys.argv
num_of_jokes = int(arguments[1])

url = "https://api.chucknorris.io/jokes/random"

print(f"Here are {num_of_jokes} Chuck Norris jokes:")

for i in range (num_of_jokes):
    try:
        r = requests.get(url)
        data = r.json()
        joke = data["value"]
    except:
        print("Error. Chuck Norris says the joke is on you")

    print("-------------------------------------------")
    print("* " + joke)
