from pathlib import Path
import streamlit as st

# Pour construire vos graphiques pyecharts
from pyecharts import options as opts
from pyecharts.charts import Bar

# Pour afficher vos graphiques (ECharts natif ou PyEcharts) dans Streamlit
from streamlit_echarts import st_echarts, st_pyecharts
