"""
Proposition of MODEL CARD WHEN SHARING A MODEL
This template proposes a description of the useful information that we want to communicate when sharing a machine learning model.
Such information should help make machine learning models more easily replicable and deployable, and also help interpret its results.

At this point, this template is merely a draft to feed collaborative work (December 1st, 2022)
"""

import json
import datetime
import markdown
from collections import OrderedDict

model_card_date = datetime.date.today()

# -------------------- NAME AND CITATIONS --------------------
project_name = "explainable-demo"  # Choose a project name
project_version = "v1"  # If you have published several model releases, indicate the version number you are auditing.
maintainers = ["Name of the persons or organisms in charge of the model"]
contact = "contact@example.gouv.fr"
# Citation: In case of scholar publication, what is the needed citation?
scholar_reference = (
    "If a research paper has been published about the model, link the citation here"
)
# Citation: what is the license of the model?
license_model_uri = "Insert Link of the license"

# Legal limitation on some (generally accepted) re-uses 
# (example: if the model is trained on legally-protected data, its re-uses are restricted)
legal_reuses_limitation = "Is there specific reasons preventing the model from being used for normally lawful uses?"

# -------------------- MODEL SOURCES --------------------

# Import model: Have you published your final model somewhere?
final_model_uri = ""  # unpublished

# Import model: If the model is not published yet, do you consider publishing it in the future?
will_be_published = False

# Import model: Do you rely on a (or several) published model? If true, what is the exact path and the exact name ?
used_upstream_model_source = [
    "URI of the model component 1",
    "URI of the model component 2",
]
used_upstream_model_names = [
    "Name and release version of the model 1 to avoid ambiguities",
    "Name and version of model 2",
]

# Import model: What is the area of the model: computer vision, nlp, time series, graphs, speech, etc?
model_area = "".upper()
# Import model: What is the category of the model: question-answering, objet tracking, image classification, etc. ? 
# this concept of "category" draws from the webiste paperswithcode
model_category = "".upper()

# Import model: What is the type of the model: classification, regression, clustering, etc. ?
model_type = "".upper()

# Import model: What are the output of the model? Are the model output of clear significance for a non-expert user?
output_description = ""

# -------------------- MODEL USES --------------------

# System requirements to run the model
model_requirements = "URI of a README OR a requirement file"

# How to use the model
model_run_command = """
```
python3.10 predict_demo.py
```
"""

# Technical recommendations: what should the model be used for?
intended_uses = [
    "",
]

# Technical recommendations: what should the model not be used for?
not_intended_uses = [""]

# -------------------- DATA SOURCES --------------------
# Import data: Are your training, validation and production data published?
are_training_open_data = True

training_data_source = {
    "dataset_1": "URI of dataset",
    "dataset_2": "URI of dataset",
}  # these datasets should be versioned

validation_data_source = {}  # these datasets should be versioned

production_data_source = {
    "dataset_1": "URI of dataset",
    "dataset_2": "URI of dataset",
}  # these datasets should be versioned

# -------------------- DATA PREPROCESSING --------------------
training_data_preprocessing = {
    "dataset_1": "Link or description of the preprocessing step for training data",
    "dataset_2": "Link or description of the preprocessing step for training data",
}
validation_data_preprocessing = {}

production_data_preprocessing = {
    "dataset_1": "Link or description of the preprocessing step for production data",
    "dataset_2": "Link or description of the preprocessing step for production data",
}

# -------------------- MODEL TRAINING --------------------
hyperparameters_optimization = """
Explanation of choices of hyper-parametrization
"""
# -------------------- MODEL EVALUATION --------------------

validation_process_description = ""  # text describing the validation process
# Model training history: what metrics were used? What were the scores?
metrics_results = {}


# -------------------- MODEL INTERPRETATION --------------------
# Interpretable: Is the model naturally interpretable? If true, have you published somewhere an interpretaton diagram?
is_interpretable = False
interpretation_diagram_uri = ""

# The explanation task: What is the scope of the explanation you target? Local (eg: SHAP), global (eg: feature importance), etc. Who if this explanation for?
explanation_scope = "".upper()
explanation_protocol = [
    "Description of the explanation measurement 1. What kind of users need this measurement? What are the required field of knowledge to interpret it?",
    "In this example ",
    "etc",
]
explanation_report_source = (
    "URI of report files (if they exist)"  # this example is a bad exemple
)

# -------------------- BIAS CONTROL --------------------

# Bias analysis when relevant: insert bias control at this step
bias_control_variables = """
Which groups are more vulnerable to bias with this model? Why? At which step of the model use should we control it?
"""
bias_report_source = ["Versioned and dated bias control report URI"]

# -------------------- EXPORT OF MODEL CARD --------------------

project_name_version = f"{project_name}-{project_version}"

# Save all the previous fields
full_report = OrderedDict(
    {
        "Model Name and Version": project_name_version,
        "Model Card date": str(model_card_date),
        "Model Developers": maintainers,
        "Model Team contact": contact,
        "Model License": license_model_uri,
        "Possible legal restrictions": legal_reuses_limitation,
        "Scholar Reference": scholar_reference,
        "Model Area": model_area,
        "Model Category": model_category,
        "Model Type": model_type,
        "Intended uses of the model": intended_uses,
        "Not-intended use": not_intended_uses,
        "Model Source": final_model_uri,
        "If the model is not published yet, do you consider doing it in the future?": will_be_published,
        "Description of output of model": output_description,
        "Model requirements": model_requirements,
        "How to run the model": model_run_command,
        "Used Upstream Model Names": used_upstream_model_names,
        "Used Upstream Model Sources": used_upstream_model_source,
        "Are training data published as open data?": are_training_open_data,
        "Training Data Sources": training_data_source,
        "Validation Data Sources": validation_data_source,
        "Production Data Sources": production_data_source,
        "Training Data Preprocessing": training_data_preprocessing,
        "Validation Data Preprocessing": validation_data_preprocessing,
        "Production Data Preprocessing": production_data_preprocessing,
        "Process of validation": validation_process_description,
        "Metrics used for the model (metrics names and results)": metrics_results,
        "How the hyperparameters have been optimized?": hyperparameters_optimization,
        "Is the model interpretable?": is_interpretable,
        "Interpretation diagram (if relevant)": interpretation_diagram_uri,
        "Explanation scope? Global, Local?": explanation_scope,
        "Protocol(s) of explanation": explanation_protocol,
        "Explanation Report Sources (if relevant)": explanation_report_source,
        "Bias control variables? (if relevant)": str(bias_control_variables),
        "Bias Report Sources (if relevant)": bias_report_source,
    }
)

# Remove not-answered fields (maybe it would relevant to keep them ?)
for k, v in full_report.copy().items():
    if not v:
        del full_report[k]

save_path = f"{project_name}-{project_version}-{str(model_card_date)}"
markdown_text = ""
for k, v in full_report.items():
    markdown_text += f"### {k}\n {v}\n\n"

with open(save_path + ".md", "w") as f:
    f.write(markdown_text)

html_text = markdown.markdown(markdown_text)
with open(save_path + ".html", "w") as f:
    f.write(html_text)

with open(save_path + ".json", "w") as f:
    json.dump(full_report, f)
