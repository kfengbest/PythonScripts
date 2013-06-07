
## install boto
# git clone git://github.com/boto/boto.git
# cd boto
# python setup.py install

import boto
import sys, os
from boto.s3.key import Key

BUCKET_NAME = "kavensembbucket"
AWS_ACCESS_KEY_ID = "AKIAJK6U5OTJIXSFXOMQ"
AWS_SECRET_ACCESS_KEY = "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"

targetName = 'emb2.zip'
srcFile = '/Users/fengka/emb.zip'


def push_to_s3():
	try:
		# connect to the bucket
		conn = boto.connect_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)
		bucket = conn.get_bucket(BUCKET_NAME)

		# create a key to keep track of our file in the storage
		k = Key(bucket)
		k.key = targetName
		k.set_contents_from_filename(srcFile)

		# we need to make it public so it can be accessed publicly
		# using a URL like http://s3.amazonaws.com/bucket_name/key
		k.make_public()

		print "Uploaded success."

	except:
		print "Upload failed"


push_to_s3()

