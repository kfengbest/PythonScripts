import os 
connected = 0 

BUCKET_NAME = "openshelfbookthumb"
LOCAL_PATH = "/Users/fengka/Documents/S3InLocal/"
AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""

def connect(): 
    access_key = AWS_ACCESS_KEY_ID 
    secret_key = AWS_SECRET_ACCESS_KEY 
    from boto.s3.connection import S3Connection 
    global conn 
    conn = S3Connection(access_key, secret_key) 
    global connected 
    connected = 1 
    print 'connected!' 

def put(fileName, bucketName): 
    if connected == 0: 
        print 'Not connected!' 
    elif connected == 1: 
        bucket = bucketName.strip() 
        from boto.s3.key import Key 
        b = conn.get_bucket(bucket) 
        k = Key(b) 
        k.key = fileName 
        local_file = os.path.join(root,fileName)
        k.set_contents_from_filename(local_file)
        k.make_public() 
         
if __name__ == '__main__': 
	connect() 
	sourceFolder = LOCAL_PATH
	print 'Start uploading...' 
	for root, dirs, files in os.walk(sourceFolder):
		for file in files:
			print '  '+str(os.path.join(root,file)) 
			#put(os.path.join(root,file),BUCKET_NAME)
			put(file,BUCKET_NAME);
	print 'finished' 