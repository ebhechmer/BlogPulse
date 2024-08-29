const fetch = require('node-fetch');
const tweepy = require('tweepy');  // Assuming you can use tweepy-like functionality in your backend

exports.handler = async (event) => {
    const blogLink = event.body.blogLink;

    // Initiate OAuth flow
    const oauth2UserHandler = new tweepy.OAuth2UserHandler({
        client_id: process.env.TWITTER_OAUTH2_CLIENT_ID,
        redirect_uri: 'https://your-deployed-url/.netlify/functions/handleOAuth',
        scope: ['tweet.read', 'tweet.write', 'users.read', 'offline.access']
    });

    const authorizationUrl = oauth2UserHandler.getAuthorizationUrl();

    return {
        statusCode: 200,
        body: JSON.stringify({
            message: 'Redirecting to Twitter for authentication',
            authorizationUrl: authorizationUrl
        })
    };
};