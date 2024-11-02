from flask import Flask, render_template, jsonify, request, Blueprint
from sqlalchemy import create_engine, text
import json

file_path = "C:\Users\\16789\Desktop\ebay_business_modules\\new_flask_project"
# grabbing from inside folder
from .__init__ import create_app

app = create_app()
if __name__ == '__main__':
    app.run(debug=True)