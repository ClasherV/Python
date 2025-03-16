from flask import Flask

app = Flask(__name__)

inp = input("Enter route name (without '/'): ")  # User-defined route

@app.route(f'/{inp}')  # Route is created dynamically
def dynamic():
    return f"This is your custom route: /{inp}"

if __name__ == "__main__":
    app.run(debug=True)