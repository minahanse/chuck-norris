# chuck-norris

Generates random Chuck Norris jokes using the Chuck Norris Jokes API.

Prints out one Chuck Norris joke, for example: "Superman is afraid of only two things, kryptonite--and Chuck Norris."

You can use env variable JOKES to change the amount of jokes return, maximum is 5. For example JOKES=2 returns 2 jokes.

## Usage
```
python app.py
```

### Docker
```
docker build -t chuck-norris .

docker run -it -e JOKES=2 chuck-norris
```