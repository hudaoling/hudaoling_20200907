import requests
import pandas as pd
import  numpy as np
import random
# from pymongo import MongoClient
import json

import pyecharts
from  pyecharts import Funnel

pd.set_option('display.width',2000)
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

yyyy={
  "adhoc_filters": [
    {
      "clause": "WHERE",
      "comparator": "1",
      "expressionType": "SIMPLE",
      "filterOptionName": "filter_7vn5x6k76d7_nqt9awnesa",
      "fromFormData": True,
      "operator": "==",
      "sqlExpression": None,
      "subject": "special_order"
    },
    {
      "clause": "WHERE",
      "comparator": "",
      "expressionType": "SIMPLE",
      "filterOptionName": "filter_3b9109w1ucx_mypa5ig3kj",
      "fromFormData": True,
      "operator": "IS NOT NULL",
      "sqlExpression": None,
      "subject": "max_reviewdate"
    }
  ],
  "align_pn": False,
  "all_columns": [
    "priceapply_no" ,
    "project_id",
    "approval_price",
    "apply_create_date",
    "special_order",
    "reviewprice",
    "permissionprice",
    "reviewer",
    "reviewdate",
    "max_reviewdate",
    "310_reviewdate"
  ],
  "color_pn": True,
  "datasource": "92__table",
  "granularity_sqla": "apply_create_date",
  "groupby": [],
  "include_search": True,
  "include_time": True,
  "metrics": [],
  "order_by_cols": [],
  "order_desc": True,
  "page_length": 0,
  "percent_metrics": [],
  "row_limit": 10000,
  "slice_id": 357,
  "table_filter": False,
  "table_timestamp_format": "%Y-%m-%d %H:%M:%S",
  "time_grain_sqla": None,
  "time_range": "No filter",
  "timeseries_limit_metric": None,
  "url_params": {},
  "viz_type": "table"
}

yyyy["all_columns"]=
print(yyyy["all_columns"])