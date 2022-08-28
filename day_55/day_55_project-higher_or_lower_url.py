import random
from flask import Flask


# Create Flask app
app = Flask(__name__)


# Image links
images = {
    "start_img": "https://media3.giphy.com/media/l46Cp6Q5aj1eb7BF6/giphy.gif?cid=ecf05e471ofntmurqgkrtd0c2uj5m7wkz5ddhp8nryl6rsin&rid=giphy.gif&ct=g",
    "high_guess": "https://media4.giphy.com/media/3oEjHRI8390hTUFs88/giphy.gif?cid=ecf05e471ofntmurqgkrtd0c2uj5m7wkz5ddhp8nryl6rsin&rid=giphy.gif&ct=g",
    "low_guess": "https://media1.giphy.com/media/z814KHJuoNck0/giphy.gif?cid=ecf05e471ofntmurqgkrtd0c2uj5m7wkz5ddhp8nryl6rsin&rid=giphy.gif&ct=g",
    "right_guess": "https://media1.giphy.com/media/t3ln1KX5XabdK/giphy.gif?cid=ecf05e474n0u284vt29mrhmgazzmqanewgm4qj12levxuqkj&rid=giphy.gif&ct=g"
}


# Generate random number
answer = random.randint(0, 9)
print(answer)

# CSS
text_css = "font-family:system-ui;text-align:center;"
img_css = "display:block;margin:auto;"


# Home route
@app.route("/")
def higher_or_lower():
    return f'<h1 style={text_css}>Higher or Lower Game</h1>' \
        f'<h4 style={text_css}>Guess a number between 0 and 9' \
        f'<img style={img_css} src={images["start_img"]}/>'


# Webpage based on guess
@app.route("/<int:guess>")
def check_guess(guess):
    if guess > answer:
        return f'<h1 style={text_css}>High! Try again.</h1>' \
            f'<img style={img_css} src={images["high_guess"]}/>'
    elif guess < answer:
        return f'<h1 style={text_css}>Too low! Try again.</h1>' \
            f'<img style={img_css} src={images["low_guess"]}/>'
    elif guess == answer:
        return f'<h1 style={text_css}>You got it!</h1>' \
            f'<img style={img_css} src={images["right_guess"]}/>'


if __name__ == "__main__":
    app.run(debug=True)
