import os
import subprocess

# Set the external UUID and security role
os.environ['AWS_ROLE_ARN'] = 'arn:aws:iam::192326305567:role/RSMSecurityRole'
os.environ['AWS_EXTERNAL_ID'] = '08f1b1a6-72d4-453f-ab20-2c79d3c6a7fc'

# Run the CloudSploit scan command
subprocess.run(['cloudsploit', 'scan'])