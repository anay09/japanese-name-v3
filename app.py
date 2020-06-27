from flask import Flask, render_template, request, url_for

app = Flask(__name__)


alphabet_map = {
    'A': 'ka',
    'B': 'tu',
    'C': 'mi',
    'D': 'te',
    'E': 'ku',
    'F': 'lu',
    'G': 'ji',
    'H': 'ri',
    'I': 'ki',
    'J': 'zu',
    'K': 'me',
    'L': 'ta',
    'M': 'rin',
    'N': 'to',
    'O': 'mo',
    'P': 'no',
    'Q': 'ke',
    'R': 'shi',
    'S': 'ari',
    'T': 'chi',
    'U': 'do',
    'V': 'ru',
    'W': 'mei',
    'X': 'na',
    'Y': 'fu',
    'Z': 'zi',
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/output", methods=["POST"])
def output():
    name = request.form.get("name")
    output_name = list()
    [output_name.append(alphabet_map[i.upper()]) for i in name]
    return render_template("output.html", name=name, output_name=output_name)
