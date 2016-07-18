from flask import Flask
app = Flask(__name__)

class FakeDatabase(object):
    def __init__(self):
        pass

    def get_random_blog_post(self):
        from random import choice
        post_1 = ("Asparagus", "Roast it!")
        post_2 = ("Brownies", "Bake them!")
        post_3 = ("Pretzels", "Boil them!")
        post_4 = ("French fries", "Fry them!")
        post_5 = ("Mushroom soup", "Simmer it")
        post_6 = ("Tiramisu", "Prepare it!")
        posts = [post_1, post_2, post_3, post_4, post_5, post_6]
        return choice(posts)

@app.route("/")
def hello():
    return "<b/> Join me for dinner! </b>"
    
@app.route("/random")
def random_selection():
    recipes = FakeDatabase()
    blog_post = recipes.get_random_blog_post()
    colors = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F")
    from random import choice
    headline_color = "#"
    for i in range(6):
        headline_color = headline_color + choice(colors)
    return "<h1 style = \"color: %s;\"> <b/> Eat %s </b> </h1> <p> Here's how to make it: %s </p>" % (
        headline_color, blog_post[0], blog_post[1])


@app.route("/blog")
def blog():
    return "<b/> Here are my recipes! </b>"
    
if __name__ == "__main__":
    app.run(port=33507)

