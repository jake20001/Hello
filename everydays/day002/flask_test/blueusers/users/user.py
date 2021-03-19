from backend.flask_test.blueusers import app

print("app",app)

@app.route('/edit')
def edit():
    return 'edit'

# app.run(host='0.0.0.0', port=5000, debug=True)