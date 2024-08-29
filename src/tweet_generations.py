import openai
from dotenv import load_dotenv
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.extract_content import extract_content
from src.post_tweet import post_tweet
# from src import extract_content, post_tweet
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = openai.Client(api_key=OPENAI_API_KEY)

def generate_tweets(content, blog_link):
    tweets = []

    system_message = (
        "You are a social media expert who writes engaging and natural-sounding tweets. "
        "The tweets should be written in a conversational tone, similar to what you'd see from a thoughtful, engaged user on Twitter. "
        "Avoid using too many emojis or exclamation marks, and make sure the tweets are informative, concise, and encourage readers to check out the linked blog post. "
        "Please include the blog link naturally at the end of each tweet."
        "You want to make sure that your followers are interested in the content and click on the link to read the full blog post."
        "You also don't want your followers to think that you are a bot or a spammer, so make sure the tweets are engaging and natural-sounding."
        "Since you also want to make sure people don't think you are self-promoting, you should make it clear that you are sharing the blog post because you found it interesting and think others will too."
    )
    # generate 5 different tweet options
    for _ in range(5):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": f"Write a tweet that summarizes the following blog content and encourages people to read it: {content}. Include this blog link: {blog_link}"}
            ]
        )
        tweets.append(response.choices[0].message.content.strip())

    return tweets

def main():
    blog_link = input("Enter the blog link: ")

    content = extract_content(blog_link)
    
    tweet_options = generate_tweets(content, blog_link)
    
    print("Generated Tweet Options:")
    for i, tweet in enumerate(tweet_options, 1):
        print(f"{i}: {tweet}\n")
    
    # asks the user to select the tweets they want to post
    selected_tweets = input("Enter the numbers of the tweets you want to post (e.g., 1 2 3 4): ")
    selected_indices = [int(i) - 1 for i in selected_tweets.split()]
    
    # posts the tweets you selected
    for i in selected_indices:
        post_tweet(tweet_options[i])

if __name__ == "__main__":
    main()