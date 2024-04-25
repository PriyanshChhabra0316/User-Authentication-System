from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        print(f'Username: {username}, Email: {email}, Password: {password}')
        return redirect(url_for('index'))

    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
 
        username = request.form.get('username')
        password = request.form.get('password')

        print(f'Username: {username}, Password: {password}')

        return redirect(url_for('index'))


    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)





