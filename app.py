from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

def get_recipe_from_ai(ingredients):
    prompt = f"Suggest a delicious recipe using the following ingredients: {ingredients}. Include a short title, ingredients, and step-by-step instructions in a friendly tone."
    result = subprocess.run(
        ['ollama', 'run', 'llama2'],
        input=prompt,
        text=True,
        capture_output=True
    )
    return result.stdout.strip()

@app.route("/", methods=["GET", "POST"])
def index():
    recipe = ""
    if request.method == "POST":
        ingredients = request.form["ingredients"].lower()
        if ingredients:
            recipe = get_recipe_from_ai(ingredients)
    return render_template("index.html", recipe=recipe)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)



