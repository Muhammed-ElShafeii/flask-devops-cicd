from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head><title>DevOps Lab</title></head>
        <body style="font-family: Arial; text-align: center; padding: 50px; background: #f0f0f0;">
            <h1>🚀 CI/CD Pipeline - DevOps Lab</h1>
            <p>Flask App deployed via Jenkins + Docker</p>
            <p style="color: green;"><b>Status: Running Successfully!</b></p>
        </body>
    </html>
    '''

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)