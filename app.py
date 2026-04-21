from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    email = request.form['email']
    
    vec = vectorizer.transform([email])
    prediction = model.predict(vec)[0]

    if prediction == 1:
        result = "⚠️ Fraud Email Detected"
    else:
        result = "✅ Legitimate Email"

    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)