import json
import boto3
from ThumbnailGenerator import ThumbnailGenerator  


def lambda_handler(event, context):
    """
    Lambda handler function for processing S3 events and generating thumbnails.

    Args:
      event (dict): S3 event notification data.
      context (object): Lambda context object.

    Returns:
      dict: Response containing status code and message.
    """

    s3_client = boto3.client('s3')

    try:
        # Extracting information from the event
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        image_object_key = event['Records'][0]['s3']['object']['key']
    
        # Download the image from S3
        print(f"Downloading image: {image_object_key}")
        response = s3_client.get_object(Bucket=bucket_name, Key=image_object_key)
        image_data = response['Body'].read()
    
        # Generate thumbnail object
        thumbnail_generator = ThumbnailGenerator()
        thumbnail_data = thumbnail_generator.generate_thumbnail(image_data)
    
        if not thumbnail_data:
            print("Error generating thumbnail") # This should be LOG.info
            return {
                'statusCode': 500,
                'body': json.dumps('Error generating thumbnail.')
            }
    
        else:
            thumbnail_bucket_name = "save-thumbnails"
            thumbnail_object_key = f"/{image_object_key}"
            try:
                print(f"Uploading thumbnail to: {thumbnail_bucket_name}/{thumbnail_object_key}") # This should be LOG.info
                s3_client.put_object(Body=thumbnail_data, Bucket=thumbnail_bucket_name, Key=thumbnail_object_key)
                print("Thumbnail uploaded successfully") # This should be LOG.info
                return {
                'statusCode': 200,
                'body': json.dumps('Thumbnail generated successfully!')
                }
            except Exception as e:
                print(f"Error uploading thumbnail: {e}") # This should be LOG.info

    except Exception as e:
      print(f"Unexpected error processing image: {e}")  # This should be LOG.info
      return {
          'statusCode': 500,
          'body': json.dumps(f'Error processing image: {str(e)}')
      }
