from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        data = request.get_json()
        
        # Extracting data from the request
        user_id = data.get('user_id', 'N/A')
        college_email = data.get('college_email', 'N/A')
        college_roll_number = data.get('college_roll_number', 'N/A')
        numbers = data.get('numbers', [])
        alphabets = data.get('alphabets', [])

        # Return response
        return jsonify({
            'status': 'success',
            'user_id': user_id,
            'college_email': college_email,
            'college_roll_number': college_roll_number,
            'numbers': numbers,
            'alphabets': alphabets
        })

    elif request.method == 'GET':
        return jsonify({'operation_code': 'GET_METHOD_CALLED'})

if __name__ == '__main__':
    app.run(debug=True)
