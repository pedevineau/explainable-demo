# Audit date
import json
import datetime
audit_date = datetime.date.today()
project_name = "explainable-demo" # Choose a project name
project_version = "v1" # If you have published several model releases, indicate the version number you are auditing.

# Import data: Are your training and production data published?
training_data_source = [
    "URI of the data used for the training of the different models (source 1)",
    "URI of the data used for the training of the different models (source 2)", 
    "etc."
]
prod_data_source = ["URI of prod data source"]

# Import model: Do you rely on a (or several) published model? If true, what is the exact path and the exact name ?
used_model_source = ["URI of the model component 1", "URI of the model component 2"]
used_model_full_name = [
    "Name and release version of the model 1 to avoid ambiguities",
    "Name and version of model 2"
]

# Import model: Have you published your final model somewhere?
final_model_uri = ""
final_model_full_name = ""

# Import model: What are the output of the model? Are the model output of clear significance for a non-expert user?
output_nature = "Description of the model output"

# Import model: Is the model naturally interpretable? If true, what is the explicit rule?
interpretable = False
explicit_rule = ""

# The explaination task: What is the scope of the explanation you target? Local, global, etc. Who if this explanation for?
explanation_scope = "local"
explanation_protocol = [
    "Description of the explanation measurement 1. What kind of users need this measurement? What are the required field of knowledge to interpret it",
    "Description of the explanation measurement 2. What kind of users need this measurement? What are the required field of knowledge to interpret it",
    "etc"
]
explanation_report_source = "URI of the explanation report if it exists"

# Bias analysis: insert bias control at this step
last_social_bias_control = None # datetime.date(1970,1,1)
last_performance_bias_control = None
bias_report_source = "URI of the explanation report if it exists"


# Print bilan of 
full_report = {
    "audit_date": str(audit_date),
    "prod_data_source": prod_data_source,
    "training_data_source": training_data_source,
    "used_model_source": used_model_source,
    "used_model_full_name": used_model_full_name,
    "final_model_uri": final_model_uri,
    "output_nature": output_nature,
    "interpretable": interpretable,
    "explicit_rule": explicit_rule,
    "explanation_scope": explanation_scope,
    "explanation_protocol": explanation_protocol,
    "explanation_report_source": explanation_report_source,
    "last_social_bias_control": str(last_social_bias_control),
    "last_performance_bias_control": str(last_performance_bias_control),
    "bias_report_source": bias_report_source
}
print(f"Full report: \n {full_report}")

with open(f"{project_name}-{project_version}-{str(audit_date)}", "w") as f:
    json.dump(full_report, f)
