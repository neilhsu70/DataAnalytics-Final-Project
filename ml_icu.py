import pandas as pd
import numpy as np

from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV

import plotly.graph_objects as go

pd.options.display.max_rows = 4000

df = pd.read_csv("diagnosis-of-covid-19-and-its-clinical-spectrum.csv")
df_positive = df.loc[df["sars_cov_2_exam_result"]=="positive"]

df_positive_selected_features = (df_positive[["patient_addmited_to_intensive_care_unit_1_yes_0_no",
                                              "patient_age_quantile",
                                              "hematocrit",
                                              "hemoglobin",
                                            #   "platelets",
                                              "mean_platelet_volume",
                                              "red_blood_cells",
                                              "lymphocytes",
                                            #   "basophils",
                                              "mean_corpuscular_hemoglobin_mch",
                                            #   "eosinophils",
                                            #   "mean_corpuscular_volume_mcv",
                                              "monocytes",
                                              "red_blood_cell_distribution_width_rdw",
                                              "neutrophils",
                                              "urea",
                                              "proteina_c_reativa_mg_dl",
                                             ]])

df_positive_selected_features_drop = df_positive_selected_features.dropna()

# Set features. This will also be used as your x values.
X=df_positive_selected_features_drop.drop("patient_addmited_to_intensive_care_unit_1_yes_0_no", axis =1)
y= df_positive_selected_features_drop["patient_addmited_to_intensive_care_unit_1_yes_0_no"]

#create a train test split 
X = pd.get_dummies(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

#create random forest cassifier
rf = RandomForestClassifier(n_estimators=2000) 
rf = rf.fit(X_train, y_train) 
acc = rf.score(X_test, y_test)

feature_importance= pd.DataFrame({
    "feature": X.columns.to_list(),
    "importance": rf.feature_importances_
    
})

feature_importance= feature_importance.sort_values(by="importance", ascending=False)

def case_features_icu():
    fig = go.Figure(go.Bar(
            x=feature_importance["importance"],
            y=feature_importance["feature"],
            orientation='h'))
    fig.update_layout(yaxis=dict(autorange="reversed"))
    return fig 



