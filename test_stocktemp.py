import pytest
#import os
from flask import Flask, render_template, request, session, redirect, url_for, flash
from app import about


def test_stocktemp_about():
    assert about() == render_template("about.html")
