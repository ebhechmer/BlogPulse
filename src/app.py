from flask import Flask, request
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.post_tweet import post_tweet

app = Flask(__name__)

@app.route('/')
def home():
    return "BlogPulse Backend is running!"

@app.route('/post_tweet', methods=['POST'])
def post_tweet_route():
    blog_link = request.form['blogLink']
    tweet_text = f"Check out this blog post: {blog_link}"  # Example tweet text
    post_tweet(tweet_text)
    return f"Tweet posted for blog link: {blog_link}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))