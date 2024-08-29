exports.handler = async (event) => {
    const authorizationResponse = event.queryStringParameters;

    const oauth2UserHandler = new tweepy.OAuth2UserHandler({
        client_id: process.env.TWITTER_OAUTH2_CLIENT_ID,
        client_secret: process.env.TWITTER_OAUTH2_CLIENT_SECRET,
        redirect_uri: 'https://your-deployed-url/.netlify/functions/handleOAuth'
    });

    const token = await oauth2UserHandler.fetchToken(authorizationResponse);

    // Now, generate and post tweets using the fetched token
    const client = new tweepy.Client({
        bearer_token: token.access_token
    });

    const tweetText = `Check out this blog post: ${event.queryStringParameters.blogLink}`;
    const response = await client.createTweet({ text: tweetText });

    return {
        statusCode: 200,
        body: JSON.stringify({ message: `Tweeted: ${response.data.id}` })
    };
};