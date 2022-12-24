from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(f'{page_name}.html')


def write_to_file(data):
    print(f'data de txt {data}')
    with open('database.txt', mode='a') as file:
        file.write(f'\n{data}')


def write_to_csv(data):
    print(f'data de csv {data}')
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('database.csv', mode='a') as database:
        csv_writer = csv.writer(
            database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, newline='')
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return redirect('thankyou')
        except:
            return 'did not save to database'
    else:
        return 'Something went wrong. Try again'


# Dinamic routes:
# @app.route('/user/<username>/<int:post_id>')
# def show_user_profile(username=None, post_id=None):
#     # None es el valor por default
#     # show the user profile for that user
#     return render_template('users.html', username=username, post_id=post_id)
