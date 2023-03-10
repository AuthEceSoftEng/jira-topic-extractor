from bertopic import BERTopic
import pymongo
from properties import database_host_and_port, project_name, model_save_folder
client = pymongo.MongoClient(database_host_and_port)
db = client["jidata"]
# Get the issues of the project
issues = [issue for issue in db["issues"].find({"projectname": project_name}, {"summary": 1, "description": 1, "assignee": 1}).sort("_id")]
# Get the texts of the issues (concatenation between the title and the description)
issue_texts = [issue.get("summary", "") + " " + issue.get("description", "") for issue in issues]
# Load the BERTopic model which corresponds to this project
topic_model = BERTopic.load(model_save_folder+project_name+".h5")
# create visualization of the topics
topic_model.visualize_documents(issue_texts, hide_document_hover=True)
