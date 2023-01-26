# jira-topic-extractor
Execution of BERTopic topic modeling technique on Jira data to train the necessary models and extract topics from issues of every project.

## Prerequisites
The python requirements are available in file `requirements.txt` and may be installed using the command `pip install -r requirements.txt`. To execute BERTopic you must have set a MongoDB instance with the issues data. The necessary details must be set in file `properties.py`.

## Execution Instructions

To execute the topic extraction, all properties in `properties.py` file must be set. After that, you can run 'python extract_topics.py' to perform the topic generation. You can insert the extracted topics for all projects to the MongoDB instance by running `python add_topics_to_db.py`.

## Visualize Topics

After the topic extraction, by running `python visualize_topics.py`, a  visualization of the topics extracted and the issues assigned to them can be produced for a selected project. The selected project must be set in the `properties.py` file.

Citation information
--------------------
If your use this tool or the corresponding dataset in your work, you can cite it using the following bibtex entry:

```
@unpublished{JiraApacheData,
  author = {Themistoklis Diamantopoulos, Dimitrios-Nikitas Nastos and Andreas Symeonidis},
  title = {Semantically-enriched Jira Issue Tracking Data},
  year = {2023},
  note = {Paper submitted}
}
```
