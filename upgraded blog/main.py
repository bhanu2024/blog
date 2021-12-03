from flask import Flask, render_template
import requests

app = Flask(__name__)
posts = requests.get("https://api.npoint.io/32593b53d1afc7f22c90").json()



@app.route("/")
def home():
    return render_template("index.html", all_blog=posts)


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/contact")
def contact_page():
    return render_template("contact.html")

@app.route("/post/<int:num>")
def get_post(num):
    return render_template("post.html", all_blog=blog_data, id_num=num)


if __name__ == "__main__":
    app.run(debug=True)

