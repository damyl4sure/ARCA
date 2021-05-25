# Run this .py file to start the provisoned EC2 instance.

from logging import Filter
import boto3
from pprint import pprint

#To start the EC2 instance using tag filters. 

client = boto3.client('ec2', region_name='us-east-2')
tag_start_ec2={'Name': 'tag:ARCA_start','Values':['start']}
for each_ins in client.describe_instances(Filters=[tag_start_ec2])['Reservations']:
    for inst_id in each_ins['Instances']:
        #print (inst_id['InstanceId'])
        client.start_instances(InstanceIds=[inst_id['InstanceId']])
        print ("Starting instance's' now")