import json
import codecs
import pymongo
from sklearn.feature_extraction.text import CountVectorizer
from bertopic import BERTopic
client = pymongo.MongoClient('mongodb://user:password@host:port/')
db = client["jidata"]
vectorizer_model = CountVectorizer(stop_words="english")
# Get all projects
projects = [project["key"] for project in db["projects"].find({}, {"key": 1})]
for project in projects:
        # Get the issues of the project
        issues = [issue for issue in db["issues"].find({"projectname": project}, {"summary": 1, "description": 1, "assignee": 1}).sort("_id")]
        # Get the texts of the issues (concatenation between the title and the description)
        issue_texts = [issue.get("summary", "") + " " + issue.get("description", "") for issue in issues]
        #No topic extraction for projects with low number of issues
        if len(issue_texts)<20:
            continue
        # Apply BERTopic on issue_texts
        print("Running BERTopic for project %s (%d issues)" %(project, len(issues)))
        try:
            topic_model = BERTopic(verbose=True,nr_topics='auto',vectorizer_model=vectorizer_model,calculate_probabilities=True)
        except IndexError:
            topic_model = BERTopic(verbose=True,vectorizer_model=vectorizer_model,calculate_probabilities=True)
        try:
            topics, probs = topic_model.fit_transform(issue_texts)
        #if the model can not fit due to low number of issues continue to the next project
        except IndexError:
            continue
        # Save BERTopic model to disk
        topic_model.save("PATH_TO_MODEL"+project + ".h5")
