
from util_feat import *
FIRST_DAY = 1500
data_demand = create_dt(is_train=True, first_day= FIRST_DAY)
data_rolling = create_dt(is_train=True, first_day= FIRST_DAY)
rolling_sales(data_rolling)
rolling_demand(data_demand)

data_demand.dropna(inplace=True)
data_rolling.dropna(inplace=True)
cat_feats = ['item_id', 'dept_id','store_id', 'cat_id', 'state_id'] + ["event_name_1", "event_name_2", "event_type_1", "event_type_2"]
useless_cols = ["id", "date", "sales","d", "wm_yr_wk", "weekday"]
train_cols_d = data_demand.columns[~data_demand.columns.isin(useless_cols)]
X_train_d = data_demand[train_cols_d]
y_train_d = data_demand["sales"]
train_cols_r = data_rolling.columns[~data_rolling.columns.isin(useless_cols)]
X_train_r = data_rolling[train_cols_r]
y_train_r = data_rolling["sales"]




