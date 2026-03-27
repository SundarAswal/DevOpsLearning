from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'Hello, World!'

print("Hello, World! from Python app.py")

with open("test.text") as file:
    text  = file.read()
    text  = text.split()

for i, word in enumerate(text):
    print(f"{i + 1}. {word}")

if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0', debug=False)