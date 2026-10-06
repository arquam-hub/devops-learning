from flask import Flask
import redis

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to the DApp!'

@app.route('/count')
def count():
    mydatabase = redis.Redis(
        host='mydatabase',  # Hostname of the Redis container
        port=6379,
        db=0,
        decode_responses=True
    )
    visit = mydatabase.incr('visit')
    return f"visit count: {visit}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
