# Run this .py file to stop the running provisoned EC2 instance.

from logging import Filter
import boto3
from pprint import pprint

#To stop the EC2 instance using tag filters. 

client = boto3.client('ec2', region_name='us-east-2')
tag_stop_ec2={'Name': 'tag:ARCA_stop','Values':['stop']}
for each_ins in client.describe_instances(Filters=[tag_stop_ec2])['Reservations']:
    for inst_id in each_ins['Instances']:
        #print (inst_id['InstanceId'])
        client.stop_instances(InstanceIds=[inst_id['InstanceId']])
        print ("Stoping instance now")