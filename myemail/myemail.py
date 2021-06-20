from flask import Flask, render_template, request, jsonify, make_response, send_from_directory, redirect, url_for
import json
import smtplib
import email.message

app = Flask(__name__)


@app.route('/myemail', methods=['GET','POST'])
@app.route('/', methods=['GET','POST'])
def myemail():
    if request.method == 'POST':
        #sender=request.values['sender']
        receiver=request.values['receiver']
        subject=request.values['subject']
        content=request.values['content']
        
        msg=email.message.EmailMessage()
        msg['From'] = 'test@gmail.com'
        msg['To'] = receiver
        msg['Subject'] = subject
        msg.set_content(content)

        server=smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("test@gmail.com","password")
        server.send_message(msg)
        server.close()

    else:
        return render_template('myemail.html')
   
       
          
        
@app.route('/')
def index():
    return 'Web App with Python Flask!'
    # return render_template("cuser.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006)
