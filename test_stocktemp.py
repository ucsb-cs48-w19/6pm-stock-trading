import pytest
#import os
from flask import Flask, render_template, request, session, redirect, url_for, flash
from config import fact

def test_stocktemp():
    assert (assert fact(10) == pytest.approx(90))
