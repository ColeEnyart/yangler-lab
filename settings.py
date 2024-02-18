import os
import sys

from dotenv import load_dotenv

load_dotenv()

s3_path = os.environ.get('S3_PATH')
glue_db = os.environ.get('GLUE_DB')