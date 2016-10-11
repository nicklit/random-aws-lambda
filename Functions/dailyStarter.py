from __future__ import print_function

import json
import boto3
from pprint import pprint

print('Loading function')


def lambda_handler(event, context):
    client = boto3.client('ec2')
    ec2 = boto3.resource('ec2')
    
    response = client.describe_instances(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': [
                    'trent'
                ]
            },
        ],
    )
    
    print(response)
    
    reservations = response['Reservations']
        
    for reservation in reservations:
        instances = reservation['Instances']
        
        for instance in instances:
            instance_id = instance['InstanceId']
            instance_state = instance['State']['Name']
            
            # start the ec2 instance
            pprint('Starting the ec2 instance with ID: ' + instance_id + ', and State: ' + instance_state)
            instance = ec2.Instance(instance_id)
            instance.start()
            pass
        
    return 'Succesfully returning from lambda function'
