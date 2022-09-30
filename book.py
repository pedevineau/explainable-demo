# Audit date
import datetime
audit_date = datetime.date.today()
project_name = "explainable-demo" # Choose a project name
project_version = "v1" # If you have published several model releases, indicate the version number you are auditing.

# Import data

## Are your training and production data published?
training_data_source = ["URI of the data used for the training of the different models (source 1)", "URI of the data used for the training of the different models (source 2), etc."]
prod_data_source = ["URI of prod data source"]

# Import model

## Do you rely on a (or several) published model? If true, what is the exact path and the exact name ?
used_model_source = ["URI of the model component 1", "URI of the model component 2"]
used_model_full_name = ["Name and release version of the model 1 to avoid ambiguities", "Name and version of model 2"]

## Have you published your final model somewhere?
final_model_uri = ""
final_model_full_name = ""

## What are the output of the model? Are the model output of clear significance for a non-expert user?
output_nature = "Description of the model output"

## Is the model naturally interpretable? If true, what is the explicit rule?
interpretable = False
explicit_rule = ""

# The explaination task

## What is the scope of the explanation you target? Local, global, etc. Who if this explanation for?
explanation_scope = "local"
explanation_recipient = "Description of the interest and required field of knowledge of the recipient"

# Bias analysis
import datetime
last_social_bias_control = None # datetime.date(1970,1,1)
last_performance_bias_control = None

# Print bilan of 
full_report = {
    "audit_date": audit_date,
    "prod_data_source": prod_data_source,
    "training_data_source": training_data_source,
    "used_model_source": used_model_source,
    "used_model_full_name": used_model_full_name,
    "final_model_uri": final_model_uri,
    "output_nature": output_nature,
    "interpretable": interpretable,
    "explicit_rule": explicit_rule,
    "explanation_scope": explanation_scope,
    "explanation_recipient": explanation_recipient,
    "last_social_bias_control": last_social_bias_control,
    "last_performance_bias_control": last_performance_bias_control
}
print(f"Full report: \n {full_report}")

import json
with open(f"{project_name}-{project_version}-str(audit-date)}", "w") as f:
    json.dump(full_report, f)
