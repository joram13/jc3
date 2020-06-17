from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request

app = Flask(__name__)

tasks = [

    {
        'id': 1,
        "address": {
            "colorKeys": [
                "A",
                "G",
                "Z"
            ],
            "values": [
                74,
                117,
                115,
                116,
                79,
                110
            ]
        },
        "meta": {
            "digits": 33,
            "processingPattern": "d{5}+[a-z&$§]"
        }
    }

]

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/juston/challenge/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    ds = 0
    for i in task[0]["address"]["values"]:
        ds += i
    return jsonify({'result': ds})

@app.route('/juston/challenge/tasks', methods=['POST'])
def create_task():
    task = {
        'id': tasks[-1]['id'] + 1,
        'address': request.json['address'],
        'meta': request.json['meta']
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route('/', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks}, {'digit sum':' https://challenge-joram.herokuapp.com/juston/challenge/tasks/specific_id_number_of_task'},{'add task': 'http://challenge-joram.herokuapp.com/juston/challenge/task'})


if __name__ == '__main__':
    app.run(debug=True)
