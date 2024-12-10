# from flask import Flask, request, jsonify, render_template_string
# from tensorflow.keras.models import load_model
# import numpy as np
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# import logging

# # Configure logging
# logging.basicConfig(level=logging.INFO)

# app = Flask(__name__)

# # Load the Keras model
# model = load_model('mymodel.keras')

# # Tokenizer settings (assume it was used during training)
# tokenizer = Tokenizer(num_words=10000)
# # Ensure to load the same tokenizer used during training, if saved
# # with open('tokenizer.pickle', 'rb') as handle:
# #     tokenizer = pickle.load(handle)

# # # HTML template
# html_template = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Sentiment Review Analyzer</title>
#     <style>
#         body {
#             font-family: TimesNewRoman;
#             margin: 0;
#             padding: 0;
#             background:url('https://www.revuze.it/blog/wp-content/uploads/sites/2/2020/03/Amazon-Review-Analysis.png');
#             background-size:cover;
#             color: #333;
#             display: flex;
#             justify-content: center;
#             align-items: center;
#             height: 100vh;
#         }

#         .container {
#             background: grey;
#             padding: 20px;
#             border-radius: 8px;
#             box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#             width: 800px;
#             display: flex;
#             justify-content: space-between;
#             align-items: flex-start;
#         }

#         .analyzer {
#             flex: 1;
#             margin-right: 20px;
#         }

#         textarea {
#             width: 100%;
#             height: 80px;
#             margin-bottom: 10px;
#             padding: 10px;
#             border: 1px solid #ddd;
#             border-radius: 4px;
#             resize: none;
#             font-size: 16px;
#         }

#         button {
#             background-color: #007bff;
#             color: #fff;
#             border: none;
#             padding: 10px 20px;
#             border-radius: 4px;
#             cursor: pointer;
#             font-size: 16px;
#         }

#         button:hover {
#             background-color: #0056b3;
#         }

#         .chart {
#             flex: 1;
#         }

#         canvas {
#             max-width: 100%;
#         }

#         #result {
#             margin-top: 10px;
#             font-size: 18px;
#         }
#     </style>
# </head>
# <body>
#     <div class="container">
#         <!-- Sentiment Analyzer -->
#         <div class="analyzer">
#             <h1>Sentiment Review Analyzer</h1>
#             <textarea id="textInput" placeholder="Enter your review here..."></textarea>
#             <button id="analyzeButton">Analyze Sentiment</button>
#             <p id="result">Sentiment: <span id="sentimentOutput">N/A</span></p>
#         </div>

#         <!-- Chart Display -->
#         <div class="chart">
#             <canvas id="sentimentChart"></canvas>
#         </div>
#     </div>

#     <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
#     <script>
#         function calculateSentiment(text) {
#             const positiveKeywords = ["good", "great", "excellent", "awesome", "amazing", "fantastic", "happy", "love", "wonderful", "perfect"];
#             const negativeKeywords = ["bad", "terrible", "awful", "horrible", "hate", "poor", "worse", "disappointing", "ugly", "sad"];
#             const neutralKeywords = ["okay", "average", "fine", "mediocre", "normal", "decent", "acceptable", "fair", "usual", "standard"];

#             const words = text.toLowerCase().split(/\W+/);
#             let positiveCount = 0;
#             let negativeCount = 0;
#             let neutralCount = 0;

#             words.forEach(word => {
#                 if (positiveKeywords.includes(word)) {
#                     positiveCount++;
#                 } else if (negativeKeywords.includes(word)) {
#                     negativeCount++;
#                 } else if (neutralKeywords.includes(word)) {
#                     neutralCount++;
#                 }
#             });

#             if (positiveCount > negativeCount && positiveCount > neutralCount) {
#                 return { sentiment: "Positive", intensity: positiveCount };
#             } else if (negativeCount > positiveCount && negativeCount > neutralCount) {
#                 return { sentiment: "Negative", intensity: negativeCount };
#             } else {
#                 return { sentiment: "Neutral", intensity: neutralCount };
#             }
#         }

#         document.getElementById("analyzeButton").addEventListener("click", () => {
#             const text = document.getElementById("textInput").value;
#             const result = calculateSentiment(text);

#             document.getElementById("sentimentOutput").textContent = result.sentiment;

#             const ctx = document.getElementById("sentimentChart").getContext("2d");
#             new Chart(ctx, {
#                 type: "bar",
#                 data: {
#                     labels: ["Positive", "Negative", "Neutral"],
#                     datasets: [{
#                         label: "Sentiment Intensity",
#                         data: [
#                             result.sentiment === "Positive" ? result.intensity : 0,
#                             result.sentiment === "Negative" ? result.intensity : 0,
#                             result.sentiment === "Neutral" ? result.intensity : 0
#                         ],
#                         backgroundColor: ["green", "red", "gray"],
#                         borderColor: ["darkgreen", "darkred", "darkgray"],
#                         borderWidth: 1
#                     }]
#                 },
#                 options: {
#                     responsive: true,
#                     maintainAspectRatio: false,
#                     scales: {
#                         y: { beginAtZero: true }
#                     }
#                 }
#             });
#         });
#     </script>
# </body>
# </html>





#  """

# @app.route('/')
# def home():
#     return render_template_string(html_template)

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         data = request.json
#         texts = data['texts']
#         logging.info(f"Received texts: {texts}")
        
#         # Preprocess the texts
#         sequences = tokenizer.texts_to_sequences(texts)
#         logging.info(f"Text sequences: {sequences}")
        
#         padded_sequences = pad_sequences(sequences, maxlen=100)
#         logging.info(f"Padded sequences: {padded_sequences}")
        
#         # Make predictions
#         predictions = model.predict(padded_sequences)
#         logging.info(f"Raw model predictions: {predictions}")
        
#         binary_predictions = (predictions > 0.5).astype(int)
#         logging.info(f"Binary predictions: {binary_predictions}")
        
#         # Generate labels
#         labels = ['Positive' if pred == 1 else 'Negative' for pred in binary_predictions]
#         logging.info(f"Generated labels: {labels}")

#         response = {'predictions': labels}
#         return jsonify(response)
#     except Exception as e:
#         logging.error(f"Error during prediction: {e}")
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)




from flask import Flask, render_template_string

app = Flask(__name__)

# Background image URL
background_image = "https://www.revuze.it/blog/wp-content/uploads/sites/2/2020/03/Amazon-Review-Analysis.png"

welcome_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background: url('{background_image}') no-repeat center center fixed;
            background-size: cover;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }}
        .container {{
            text-align: center;
            background: rgba(255, 255, 255, 0.8);
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        }}
        button {{
            background-color: #007bff;
            color: #fff;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }}
        button:hover {{
            background-color: #0056b3;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to the Sentiment Analysis Tool</h1>
        <p>Analyze reviews to discover their sentiment.</p>
        <button onclick="window.location.href='/sentiment'">Start</button>
    </div>
</body>
</html>
"""

sentiment_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sentiment Analysis</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background: url('{background_image}') no-repeat center center fixed;
            background-size: cover;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }}
        .container {{
            background: rgba(0, 0, 0, 0.7);
            color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
            width: 800px;
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
        }}
        textarea {{
            width: 100%;
            height: 80px;
            margin-bottom: 10px;
            padding: 10px;
            border-radius: 4px;
        }}
        button {{
            background-color: #007bff;
            color: white;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
            border-radius: 4px;
        }}
        button:hover {{
            background-color: #0056b3;
        }}
        canvas {{
            max-width: 100%;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div>
            <h1>Sentiment Analysis Tool</h1>
            <textarea id="textInput" placeholder="Enter a review"></textarea>
            <button id="analyzeButton">Analyze Sentiment</button>
            <p>Sentiment: <span id="sentimentOutput">N/A</span></p>
        </div>
        <canvas id="sentimentChart"></canvas>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
        document.getElementById("analyzeButton").addEventListener("click", () => {{
            const text = document.getElementById("textInput").value;
            const result = calculateSentiment(text);

            document.getElementById("sentimentOutput").textContent = result.sentiment;

            const ctx = document.getElementById("sentimentChart").getContext("2d");
            new Chart(ctx, {{
                type: "bar",
                data: {{
                    labels: ["Positive", "Negative", "Neutral"],
                    datasets: [{{
                        label: "Sentiment Intensity",
                        data: [
                            result.sentiment === "Positive" ? result.intensity : 0,
                            result.sentiment === "Negative" ? result.intensity : 0,
                            result.sentiment === "Neutral" ? result.intensity : 0
                        ],
                        backgroundColor: ["green", "red", "gray"]
                    }}]
                }}
            }});
            // Redirect to the "Thank You" page after analysis
            setTimeout(() => {{
                window.location.href = "/thankyou";
            }}, 3000); // Wait 3 seconds before redirecting
        }});

        function calculateSentiment(text) {{
            const positiveKeywords = ["good", "great", "excellent"];
            const negativeKeywords = ["bad", "terrible"];
            const neutralKeywords = ["okay", "average"];
            const words = text.toLowerCase().split(/\\W+/);

            let positiveCount = 0, negativeCount = 0, neutralCount = 0;
            words.forEach(word => {{
                if (positiveKeywords.includes(word)) positiveCount++;
                else if (negativeKeywords.includes(word)) negativeCount++;
                else if (neutralKeywords.includes(word)) neutralCount++;
            }});

            if (positiveCount > negativeCount && positiveCount > neutralCount) return {{ sentiment: "Positive", intensity: positiveCount }};
            if (negativeCount > positiveCount && negativeCount > neutralCount) return {{ sentiment: "Negative", intensity: negativeCount }};
            return {{ sentiment: "Neutral", intensity: neutralCount }};
        }}
    </script>
</body>
</html>
"""

thankyou_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thank You</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background: url('{background_image}') no-repeat center center fixed;
            background-size: cover;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }}
        .container {{
            text-align: center;
            background: rgba(255, 255, 255, 0.8);
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        }}
        button {{
            background-color: #007bff;
            color: #fff;
            padding: 10px 20px;
            border-radius: 4px;
            cursor: pointer;
            border: none;
        }}
        button:hover {{
            background-color: #0056b3;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Thank You for Visiting!</h1>
        <button onclick="window.location.href='/'">Go Back to Home</button>
    </div>
</body>
</html>
"""

@app.route('/')
def welcome():
    return render_template_string(welcome_template)

@app.route('/sentiment')
def sentiment():
    return render_template_string(sentiment_template)

@app.route('/thankyou')
def thankyou():
    return render_template_string(thankyou_template)

if __name__ == '__main__':
    app.run(debug=True)
