const Twitter = require('twitter');

const client = new Twitter({
  consumer_key: 'dkueMn2pmtVUdn51GBAgFSSM0',
  consumer_secret: 'nSuWPVr6TGfD7ML35n7stVDWNgLCLV4zxFdGB0moeGdjIaRotO',
  access_token_key: '2027865526333313024-QnTROy76RwOXk50cPXRkazEwk2GPIx',
  access_token_secret: 'PHsQkvipLzCtmp5uxyQ09dEYTbKZOLxQtoLyAm6kDSdlz',
  access_token: '2027865526333313024-QnTROy76RwOXk50cPXRkazEwk2GPIx',
});

const message = process.argv[2] || 'Hello from Hari Seldon! 🤖';

client.post('statuses/update', { status: message }, function(error, tweet, response) {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }
  console.log('Tweet posted successfully!');
  console.log('Tweet ID:', tweet.id_str);
  console.log('Tweet text:', tweet.text);
});
