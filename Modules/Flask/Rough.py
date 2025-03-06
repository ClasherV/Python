from flask import Flask

app = Flask(__name__)

app.logger.info("This is an info log")
app.logger.warning("This is a warning log")
app.logger.error("This is an error log")