from bertopic import BERTopic
import pymongo
from properties import database_host_and_port, model_name, model_save_folder
client = pymongo.MongoClient(database_host_and_port)
db = client["jidata"]
# Get the issues of the project
issues = [issue for issue in db["issues"].find({"projectname": model_name}, {"summary": 1, "description": 1, "assignee": 1}).sort("_id")]
# Get the texts of the issues (concatenation between the title and the description)
issue_texts = [issue.get("summary", "") + " " + issue.get("description", "") for issue in issues]
topic_model = BERTopic.load(model_save_folder+model_name+".h5")
topic_model.visualize_documents(issue_texts, hide_document_hover=True)
