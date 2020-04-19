from google.cloud import storage
from pandas.io import json
from google.cloud import firestore

storage = storage.Client()
db = firestore.Client()


def hello_gcs(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    file = event
    bucket = storage.get_bucket(file['bucket'])
    blob = bucket.get_blob(file['name'])
    bstr = str(blob.download_as_string(), 'utf-8')
    for bline in bstr.splitlines():
        json_data = json.loads(bline)
        doc_ref = db.collection(u'data').document(json_data['entityId'])
        doc_ref.set(json_data['data'])

    print(f"bucket : {file['bucket']}")
    print(f"selfLink : {file['selfLink']}")
    print(f"Processing file : {file['name']}.")
