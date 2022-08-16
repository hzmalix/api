# -*- coding: utf-8 -*-

from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re

from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return ('After Changing API')


if __name__ == '__main__':
    app.run(debug=True)
