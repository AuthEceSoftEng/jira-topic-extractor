from bertopic import BERTopic
import pymongo
client = pymongo.MongoClient('mongodb://user:password@host:port/')
db = client["jidata"]
# Get all projects
projects = [project["key"] for project in db["projects"].find({"key": "FTPSERVER"}, {"key": 1})]
for project in projects:
        # Get the issues of the project
        issues = [issue for issue in db["issues"].find({"projectname": project}, {"summary": 1, "description": 1, "assignee": 1}).sort("_id")]
        # Get the texts of the issues (concatenation between the title and the description)
        issue_texts = [issue.get("summary", "") + " " + issue.get("description", "") for issue in issues]
topic_model = BERTopic.load("PATH_TO_MODEL"+"FTPSERVER.h5")
topic_model.visualize_documents(iss, hide_document_hover=True)
