#trying to make the website interactive

from flask import Flask, request

from processing import do_calculation

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def adder_page():
    if request.method == "POST":
        number1 = None
        number2 = None
    if number1 is not None and number2 is not None:
        result = do_calculation(number1, number2)
    return '''
        <html>
        <body>
        <p>Enter your specifications:</p>
        <p>Workout Length</p>
            <form method="post" action=".">
              <p><input name="number1" /></p>
            </form>
        <p>Target Area</p>
            <!-- <form method="post" action="." -->
                <form name="form1" id="form1" action="/action_page.php">
                    Subjects: <select name="area" id="area">
                      <option value="" selected="selected">Arms</option>
                      <option value="" selected="selected">Legs</option>
                      <option value="" selected="selected">Core</option>
                    </select>
                </form>
                <!-- <p><input name="number2" /></p> -->
                <p><input type="submit" value="Do calculation" /></p>
            <!-- </form> -->
    </body>
</html>