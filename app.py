from flask import Flask, render_template, request
from main import preprocess, vectorize, check_plagiarism

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_files():
    file1 = request.files['file1']
    file2 = request.files['file2']

    text1 = file1.read().decode('utf-8')
    text2 = file2.read().decode('utf-8')

    processed_text1 = preprocess(text1)
    processed_text2 = preprocess(text2)

    vectors = vectorize([processed_text1, processed_text2])
    sim_score = check_plagiarism(vectors[0], vectors[1])

    return render_template('index.html', similarity=sim_score)

if __name__ == '__main__':
    app.run(debug=True)
