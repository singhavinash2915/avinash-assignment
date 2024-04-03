import boto3
import json

def get_instance_metadata(keys=None):
    # Initialize the EC2 client
    ec2_client = boto3.client('ec2')

    # Retrieve instance metadata
    response = ec2_client.describe_instances()

    # Extract relevant information from the response
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_data = {}
            for key in keys:
                if key in instance:
                    instance_data[key] = instance[key]
                else:
                    instance_data[key] = 'N/A'
            instances.append(instance_data)

    return instances

def save_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {filename} successfully.")

# Specify the keys to retrieve
keys_to_retrieve = ['InstanceId', 'InstanceType', 'PrivateIpAddress']

# Get instance metadata for specified keys
instance_metadata = get_instance_metadata(keys_to_retrieve)

# Save metadata to JSON file
save_to_json(instance_metadata, 'ec2_instance_metadata.json')
