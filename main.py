from google.cloud import storage
from pandas.io import json

client = storage.Client()
# https://console.cloud.google.com/storage/browser/[bucket-id]/
bucket = client.get_bucket('gcloud-example-bucket')
# Then do other things...
blob = bucket.get_blob('cloud_function_test.json')
bstr = str(blob.download_as_string(), 'utf-8')
for bline in bstr.splitlines():
    json_data = json.loads(bline)
    print(json_data['data']['zoneType'])
# blob.upload_from_string('New contents!')
# blob2 = bucket.blob('remote/path/storage.txt')
# blob.upload_from_filename(filename='/Users/yuvraj/code/python/gcp/path.txt')
