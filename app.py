from flask import Flask, render_template, request, jsonify


app = Flask(__name__)


@app.route('/')
def index():
	return "Hello World"


def pallinndrome_using_pallindrome(s):
    if len(s)>1:
        if s[0]==s[-1]:
            return pallinndrome_using_pallindrome(s[1:-1])
        else:
            return False
    elif len(s)==1:
        return True
    else:
        return False
if __name__ == "__main__":
    app.run(debug = True)
