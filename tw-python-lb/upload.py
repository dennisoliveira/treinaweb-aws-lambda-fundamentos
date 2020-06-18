import boto3
import os

def lambda_handler(event, context):
	response = {
		"statusCode": 200,
		"statusDescription": "200 OK",
		"isBase64Encoded": False,
		"headers": {
			"Content-Type": "text/html;"
		}
	}
	
	if event['headers']['user-agent']=='ELB-HealthChecker/2.0':
		print("This is a Health Check Request")
		response['body'] = 'Response to Health Check Request'
		return response
	
	if event['httpMethod']=='GET':
		response['body'] = 'Response to GET {} request'.format(event['path'])
		return response

	s3key = event['queryStringParameters']['name']
	bucket = os.environ["BUCKET"]
	filePath = "/tmp/"+ s3key
	
	fileRes = open(filePath, "w")
	fileRes.write(event['body'])
	fileRes.close()
	
	if event['httpMethod']=='POST':
		s3 = boto3.resource('s3')
		try:
			s3.meta.client.upload_file(filePath, bucket, s3key)
			response['body'] = "Upload to S3 {} successfully".format(bucket)
			return response
		except Exception as e:
			print(e)
			response['body'] = "Failed to upload to S3 {}".format(bucket)
			return response
	
	response['body'] = "Default Response"
	return response

