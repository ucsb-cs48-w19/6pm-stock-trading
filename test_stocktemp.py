import pytest
#import os
from flask import Flask, render_template, request, session, redirect, url_for, flash
from utility import fact

def test_stocktemp():
    assert fact(10) == pytest.approx(90)
