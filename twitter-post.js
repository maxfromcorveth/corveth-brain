const Twitter = require('twitter');

const client = new Twitter({
  consumer_key: 'dkueMn2pmtVUdn5iGBAqFSSM0',
  consumer_secret: 'nSuWPVz6T6fD7ML35n7stVDWNgLCLV4zxFdGB0mqeGdJiaRotO',
  access_token: '2027865526333313024-9RUWzU01hYwAyjnwieN9y0oKwRSaRR',
  access_token_secret: 'SNQodf1DJvU4V5F72g7mSi3ha2BFH9nLke07V60ePhqP5',
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
