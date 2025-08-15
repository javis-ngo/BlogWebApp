import os

from app.repositories import s3_client, endpoint_url
from app.utils.my_util import get_time_stamp

aws_s3_bucket_name = os.getenv('BUCKET_NAME')
aws_s3_region = os.getenv('REGION_NAME')
end_point_url = os.getenv('ENDPOINT_URL')

def upload_image_to_s3(file, filename):
    s3_filename = f"{str(get_time_stamp())}-{filename}"
    s3_client.upload_fileobj(
        file,
        aws_s3_bucket_name,
        s3_filename,
        ExtraArgs={
            'ContentType': file.content_type,
            # 'ContentDisposition': 'attachment',
            # 'ACL': 'public-read',
        }
    )
    file_url = f"{end_point_url}/{aws_s3_bucket_name}/{s3_filename}"
    return file_url