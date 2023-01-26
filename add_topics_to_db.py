import pymongo
from bertopic import BERTopic
from properties import database_host_and_port, model_save_folder
client = pymongo.MongoClient(database_host_and_port)
db = client["jidata"]
projects = [project["key"] for project in db["projects"].find({}, {"key": 1})]
for project in projects:
    #Load the BERTopic model for the corresponding project if exists
    try:
    	topic_model = BERTopic.load(model_save_folder+project+".h5")
    except FileNotFoundError:    	
        continue
    # Get the issues of the project and their ids
    issues = [issue for issue in db["issues"].find({"projectname": project}, {"_id": 1}).sort("_id")]
    print("Project %s (%d issues)" %(project, len(issues)))    
    issue_ids = [issue.get("_id","") for issue in issues]
    #Get topic names 
    project_topics=topic_model.topic_labels_
    #Get most frequent terms of the topic
    topic_terms=topic_model.topic_representations_
    #discard outliers if exist
    try:
        project_topics.pop(-1)
    except:
        pass
    #create list to save each topic of the project
    output=[]
    #store the necessary information for every topic
    for i in project_topics:
        record={}
        record['_id']=project+"_"+str(i+1).zfill(3)
        record['key']=record['_id']
        record['name']=project_topics[i]
        record['projectname']=project
        record['terms']=[words[0] for words in topic_terms[i]]
        record['probabilities']=[]
        probs=topic_model.probabilities_
        #store topic probabilities for each issue
        for j in range(len(probs)):
            #check if the probability of the topic for the issue is above threshold
            if probs[j][i]>0.0000000001:
                prob_record={}
                prob_record['issue_id']=issue_ids[j]
                prob_record['prob']=probs[j][i]
                record['probabilities'].append(prob_record)
        #add topic to the project topics list
        output.append(record)
    #insert project topics to DB
    db.topics.insert_many(output)
client.close()
