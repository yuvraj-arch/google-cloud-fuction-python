from google.cloud import storage

storage_client = storage.Client()


def hello_gcs(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    file = event
    bucket = storage_client.get_bucket(file['bucket'])
    blob = bucket.get_blob(file['name'])
    bstr = str(blob.download_as_string(), 'utf-8')
    for bline in bstr.splitlines():
        print(bline)

    print(f"bucket : {file['bucket']}")
    print(f"selfLink : {file['selfLink']}")
    print(f"Processing file : {file['name']}.")

