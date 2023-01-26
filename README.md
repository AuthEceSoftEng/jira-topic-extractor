# jira-topic-extractor
Execution of BERTopic topic modeling technique on Jira data to extract topics from issues.

## Prerequisites
The python requirements are available in file 'requirements.txt' and may be installed using the command 'pip install -r requirements.txt'. To execute BERTopic you must have set a MongoDB instance with the issues data. The necessary details must be set in file 'properties.py'.

## Execution Instructions

To execute the topic extraction, all properties in 'properties.py' file must be set. After that, you can run 'python extract_topics.py' to perform the topicc generation. You can insert the extracted topics to the MongoDB instance by running 'python add_topics_to_db.py'

