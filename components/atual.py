import os
import dash
import json
import plotly.express as px
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from app import app
from datetime import datetime, date

import pdb
from dash_bootstrap_templates import ThemeChangerAIO
import numpy as np
import pandas as pd

layout = dbc.Card([
    html.H5('Página Dashboard Atual')
])