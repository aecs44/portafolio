from flask import Flask, render_template,  url_for, request
import csv


app = Flask(__name__)
print(__name__)


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/<string:page_name>')
def html_page(page_name=None):
    print(page_name)
    return render_template(page_name + '.html')


def save_data(data):
    with open('database.txt', mode='a') as database:
        username = data['user_name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n-------------\nUsername: {username}\nEmail: {email}\nSubject: {subject}\nMessage: {message}')


def save_to_csv(data):
    with open('database.csv', newline= '', mode='a') as database2:
        username = data['user_name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([username, email, subject, message])


@app.route('/submitform', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            save_to_csv(data)
            user_name = data['user_name']
            return render_template('thankyou.html', user_name=user_name)
        except:
            return 'Did not save to database.'
    else:
        return 'Could not submit request. Please try again!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

