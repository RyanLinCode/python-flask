from flask import Flask, render_template

app = Flask(__name__)  # 建立 Application 物件


@app.route("/for-loop/conditionals/")
def render_for_loops_conditionals():
    user_os = {
        "Bob Smith": "Windows",
        "Anne Pun": "MacOS",
        "Adam Lee": "Linux",
        "Jose Salvatierra": "Windows",
    }
    return render_template("loops_and_conditionals.html", user_os=user_os)


@app.route("/for-loop")
def render_loops_for():
    planets = [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune"
    ]

    return render_template("for_loop.html", planets=planets)


@app.route("/conditionals-basics/")
def render_conditionals():
    company = "Microsoft"
    return render_template("conditionals_basics.html", company=company)


class GalileanMoons:
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth


@app.route("/data_structures")
def render_data_structures():
    movies = [
        "Leon the Professional",
        "The Usual Suspects",
        "A Beautiful Mind"
    ]

    car = {
        "brand": "Tesla",
        "model": "Roadster",
        "year": "2020",
    }

    moons = GalileanMoons("Io", "Europa", "Ganymede", "Callisto")
    return render_template("data_structures.html", movies=movies, car=car, moons=moons)


# 建立網站首頁的回應
@app.route("/second")
def hello_world():
    # interpolation
    color = "brown"
    animal_one = "fox"
    animal_two = "dog"

    # addition and subtraction
    orange_amount = 10
    apple_amount = 20
    donate_amount = 15

    # string concatenation

    first_name = "Captain"
    last_name = "Marvel"

    kwargs = {
        "color": color,
        "animal_one": animal_one,
        "animal_two": animal_two,
        "orange_amount": orange_amount,
        "apple_amount": apple_amount,
        "donate_amount": donate_amount,
        "first_name": first_name,
        "last_name": last_name,

    }

    return render_template("expressions.html", **kwargs)


@app.route("/")
def hello_world_fancy():
    return render_template("test.html")
