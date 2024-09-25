

import streamlit as st
from PIL import Image
from typing import Optional

hide_menu = """
<style>
#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}
</style>
"""

showWarningOnDirectExecution = False
image = Image.open('icons/logo.png')

st.set_page_config(page_title="Algorithms", page_icon=image)

st.markdown(hide_menu, unsafe_allow_html=True)

st.sidebar.image(image, use_column_width=True, output_format='auto')

st.sidebar.markdown("---")

st.sidebar.markdown(" <br> <br> <br> <br> <br> <br> <br> <h1 style='text-align: center; font-size: 18px; color: #0080FF;'>© 2024 | SafeSpeak </h1>", unsafe_allow_html=True)



st.markdown("""
    <h1 style='font-size: 50px;'>Algorithms📊</h1>
""", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

all_Datasets = ["Select a Dataset", "Cyber Bullying Types Dataset", "Cyber Troll Dataset", "Classified Tweets Dataset", "Cyberbulling Classification Dataset", "Cyber Bullying Types Dataset + Cyber Troll Dataset", "Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset"]
data_choice: Optional[str] = st.selectbox("Dataset", all_Datasets)
all_Vectorizers = ["Select a Vectorizer", "TF-IDF", "CountVectorizer"]
vect_choice: Optional[str] = st.selectbox("Vectorizer", all_Vectorizers)
all_ML_models = ["Select a Machine Learning Algorithm", "Logistic Regression", "Decision Tree", "Random Forest", "XGBoost", "Naive Bayes", "Support Vector Machine"]
# "Bagging Decision Tree", 
# "Boosting Decision Tree"
model_choice: Optional[str] = st.selectbox("Machine Learning Algorithm", all_ML_models)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("---")

if not all([data_choice, vect_choice, model_choice]):
    missing_choices = [c for c in ["Dataset", "Vectorizer", "Machine Learning Algorithm"] if not eval(f"{c.lower().replace(' ', '_')}_choice")]
    st.warning(f":white[You should select **_{', '.join(missing_choices)}_**]")
else:
    accuracy_mapping = {
    ("Cyber Bullying Types Dataset", "TF-IDF", "Logistic Regression"): "90.88%",
    ("Cyber Bullying Types Dataset", "TF-IDF", "Decision Tree"): "87.38%",
    ("Cyber Bullying Types Dataset", "TF-IDF", "Random Forest"): "89.71%",
    ("Cyber Bullying Types Dataset", "TF-IDF", "XGBoost"): "87.38%",
    ("Cyber Bullying Types Dataset", "TF-IDF", "Naive Bayes"): "88.78%",
    ("Cyber Bullying Types Dataset", "TF-IDF", "Support Vector Machine"): "89.71%",
    ("Cyber Bullying Types Dataset", "TF-IDF", "Bagging Decision Tree"): "88.08%",
    ("Cyber Bullying Types Dataset", "TF-IDF", "Boosting Decision Tree"): "87.38%",
    ("Cyber Bullying Types Dataset", "CountVectorizer", "Logistic Regression"): "90.65%",
    ("Cyber Bullying Types Dataset", "CountVectorizer", "Decision Tree"): "89.71%",
    ("Cyber Bullying Types Dataset", "CountVectorizer", "Random Forest"): "90.18%",
    ("Cyber Bullying Types Dataset", "CountVectorizer", "XGBoost"): "89.95%",
    ("Cyber Bullying Types Dataset", "CountVectorizer", "Naive Bayes"): "90.88%",
    ("Cyber Bullying Types Dataset", "CountVectorizer", "Support Vector Machine"): "90.88%",
    ("Cyber Bullying Types Dataset", "CountVectorizer", "Bagging Decision Tree"): "89.25%",
    ("Cyber Bullying Types Dataset", "CountVectorizer", "Boosting Decision Tree"): "89.01%",

    ("Cyber Troll Dataset", "TF-IDF", "Logistic Regression"): "76.08%",
    ("Cyber Troll Dataset", "TF-IDF", "Decision Tree"): "85.92%",
    ("Cyber Troll Dataset", "TF-IDF", "Random Forest"): "91.70%",
    ("Cyber Troll Dataset", "TF-IDF", "XGBoost"): "76.00%",
    ("Cyber Troll Dataset", "TF-IDF", "Naive Bayes"): "78.20%",
    ("Cyber Troll Dataset", "TF-IDF", "Support Vector Machine"): "80.50%",
    ("Cyber Troll Dataset", "TF-IDF", "Bagging Decision Tree"): "84.87%",
    ("Cyber Troll Dataset", "TF-IDF", "Boosting Decision Tree"): "91.22%",
    ("Cyber Troll Dataset", "CountVectorizer", "Logistic Regression"): "81.57%",
    ("Cyber Troll Dataset", "CountVectorizer", "Decision Tree"): "84.60%",
    ("Cyber Troll Dataset", "CountVectorizer", "Random Forest"): "86.47%",
    ("Cyber Troll Dataset", "CountVectorizer", "XGBoost"): "73.48%",
    ("Cyber Troll Dataset", "CountVectorizer", "Naive Bayes"): "79.73%",
    ("Cyber Troll Dataset", "CountVectorizer", "Support Vector Machine"): "83.72%",
    ("Cyber Troll Dataset", "CountVectorizer", "Bagging Decision Tree"): "81.75%",
    ("Cyber Troll Dataset", "CountVectorizer", "Boosting Decision Tree"): "89.35%",

    ("Classified Tweets Dataset", "TF-IDF", "Logistic Regression"): "90.52%",
    ("Classified Tweets Dataset", "TF-IDF", "Decision Tree"): "89.10%",
    ("Classified Tweets Dataset", "TF-IDF", "Random Forest"): "91.45%",
    ("Classified Tweets Dataset", "TF-IDF", "XGBoost"): "90.95%",
    ("Classified Tweets Dataset", "TF-IDF", "Naive Bayes"): "87.89%",
    ("Classified Tweets Dataset", "TF-IDF", "Support Vector Machine"): "91.30%",
    ("Classified Tweets Dataset", "TF-IDF", "Bagging Decision Tree"): "91.17%",
    ("Classified Tweets Dataset", "TF-IDF", "Boosting Decision Tree"): "90.24%",
    ("Classified Tweets Dataset", "CountVectorizer", "Logistic Regression"): "91.07%",
    ("Classified Tweets Dataset", "CountVectorizer", "Decision Tree"): "88.90%",
    ("Classified Tweets Dataset", "CountVectorizer", "Random Forest"): "90.92%",
    ("Classified Tweets Dataset", "CountVectorizer", "XGBoost"): "91.38%",
    ("Classified Tweets Dataset", "CountVectorizer", "Naive Bayes"): "90.39%",
    ("Classified Tweets Dataset", "CountVectorizer", "Support Vector Machine"): "90.24%",
    ("Classified Tweets Dataset", "CountVectorizer", "Bagging Decision Tree"): "90.95%",
    ("Classified Tweets Dataset", "CountVectorizer", "Boosting Decision Tree"): "89.40%",

    ("Cyberbulling Classification Dataset", "TF-IDF", "Logistic Regression"): "86.10%",
    ("Cyberbulling Classification Dataset", "TF-IDF", "Decision Tree"): "82.23%",
    ("Cyberbulling Classification Dataset", "TF-IDF", "Random Forest"): "84.12%",
    ("Cyberbulling Classification Dataset", "TF-IDF", "XGBoost"): "86.26%",
    ("Cyberbulling Classification Dataset", "TF-IDF", "Naive Bayes"): "84.67%",
    ("Cyberbulling Classification Dataset", "TF-IDF", "Support Vector Machine"): "86.27%",
    ("Cyberbulling Classification Dataset", "TF-IDF", "Bagging Decision Tree"): "84.61%",
    ("Cyberbulling Classification Dataset", "TF-IDF", "Boosting Decision Tree"): "83.54%",
    ("Cyberbulling Classification Dataset", "CountVectorizer", "Logistic Regression"): "86.10%",
    ("Cyberbulling Classification Dataset", "CountVectorizer", "Decision Tree"): "82.07%",
    ("Cyberbulling Classification Dataset", "CountVectorizer", "Random Forest"): "84.43%",
    ("Cyberbulling Classification Dataset", "CountVectorizer", "XGBoost"): "86.26%",
    ("Cyberbulling Classification Dataset", "CountVectorizer", "Naive Bayes"): "84.67%",
    ("Cyberbulling Classification Dataset", "CountVectorizer", "Support Vector Machine"): "86.27%",
    ("Cyberbulling Classification Dataset", "CountVectorizer", "Bagging Decision Tree"): "84.19%",
    ("Cyberbulling Classification Dataset", "CountVectorizer", "Boosting Decision Tree"): "83.55%",



    ("Cyber Bullying Types Dataset + Cyber Troll Dataset", "TF-IDF", "Logistic Regression"): "78.12%",
    ("Cyber Bullying Types Dataset + Cyber Troll Dataset", "TF-IDF", "Decision Tree"): "85.45%",
    ("Cyber Bullying Types Dataset + Cyber Troll Dataset", "TF-IDF", "Random Forest"): "90.29%", 
    ("Cyber Bullying Types Dataset + Cyber Troll Dataset", "TF-IDF", "XGBoost"): "75.52%",
    ("Cyber Bullying Types Dataset + Cyber Troll Dataset", "TF-IDF", "Naive Bayes"): "79.95%",
    ("Cyber Bullying Types Dataset + Cyber Troll Dataset", "TF-IDF", "Support Vector Machine"): "80.60%",
    ("Cyber Bullying Types Dataset + Cyber Troll Dataset", "TF-IDF", "Bagging Decision Tree"): "84.84%",
    ("Cyber Bullying Types Dataset + Cyber Troll Dataset", "TF-IDF", "Boosting Decision Tree"): "90.06%",
    ("Cyber Bullying Types Dataset + Cyber Troll Dataset", "CountVectorizer", "Logistic Regression"): "81.89%",
    ("Cyber Bullying Types Dataset + Cyber Troll Dataset", "CountVectorizer", "Decision Tree"): "83.60%",
    ("Cyber Bullying Types Dataset + Cyber Troll Dataset", "CountVectorizer", "Random Forest"): "85.52%",
    ("Cyber Bullying Types Dataset + Cyber Troll Dataset", "CountVectorizer", "XGBoost"): "73.51%",
    ("Cyber Bullying Types Dataset + Cyber Troll Dataset", "CountVectorizer", "Naive Bayes"): "79.58%",
    ("Cyber Bullying Types Dataset + Cyber Troll Dataset", "CountVectorizer", "Support Vector Machine"): "83.24%",
    ("Cyber Bullying Types Dataset + Cyber Troll Dataset", "CountVectorizer", "Bagging Decision Tree"): "82.45%",
    ("Cyber Bullying Types Dataset + Cyber Troll Dataset", "CountVectorizer", "Boosting Decision Tree"): "89.16%",

    ("Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset", "TF-IDF", "Logistic Regression"): "84.57%",
    ("Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset", "TF-IDF", "Decision Tree"): "80.03%",
    ("Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset", "TF-IDF", "Random Forest"): "81.77%",
    ("Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset", "TF-IDF", "XGBoost"): "84.50%",
    ("Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset", "TF-IDF", "Naive Bayes"): "74.90%",
    ("Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset", "TF-IDF", "Support Vector Machine"): "84.72%",
    ("Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset", "TF-IDF", "Bagging Decision Tree"): "82.69%",
    ("Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset", "TF-IDF", "Boosting Decision Tree"): "80.65%",
    ("Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset", "CountVectorizer", "Logistic Regression"): "84.57%",
    ("Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset", "CountVectorizer", "Decision Tree"): "80.11%",
    ("Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset", "CountVectorizer", "Random Forest"): "82.03%",
    ("Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset", "CountVectorizer", "XGBoost"): "84.50%",
    ("Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset", "CountVectorizer", "Naive Bayes"): "74.90%",
    ("Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset", "CountVectorizer", "Support Vector Machine"): "84.72%",
    ("Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset", "CountVectorizer", "Bagging Decision Tree"): "82.65%",
    ("Cyber Bullying Types Dataset + Cyber Troll Dataset + Classified Tweets Dataset + Cyberbulling Classification Dataset", "CountVectorizer", "Boosting Decision Tree"): "80.48%"
}


    key = (data_choice, vect_choice, model_choice)
    if key in accuracy_mapping:
        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("Evaluation Metrics")
        st.success(f":green[Accuracy: **_{accuracy_mapping[key]}_**]")
    else:
        st.warning(":red[No evaluation metrics available for the selected combination.]")
        