from flask import Flask
from flask_odoo import Odoo

app = Flask(__name__)
# Here we can configure in the next manner as we can see
app.config["ODOO_URL"] = "the_odoo_url"
app.config["ODOO_DB"] = "odoo"
app.config["ODOO_USERNAME"] = "admin"
app.config["ODOO_PASSWORD"] = "admin"
odoo = Odoo(app)  # This is the manner to call in the next manner of the main


def some_subroutine(func):
    pass


