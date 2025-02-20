import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Get all EBS volumes
    response = ec2.describe_volumes()

    # Get all active EC2 instance IDs
    instances_response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    active_instance_ids = set()
    for reservation in instances_response['Reservations']:
        for instance in reservation['Instances']:
            active_instance_ids.add(instance['InstanceId'])

    # Iterate through each volume and check if it's attached to a running instance
    for volume in response['Volumes']:
        volume_id = volume['VolumeId']
        attachments = volume.get('Attachments', [])
        if not attachments:
            # Delete the volume if it's not attached to any instance
            ec2.delete_volume(VolumeId=volume_id)
            print(f"Deleted EBS volume {volume_id} as it was not attached to any instance.")
        else:
            # Check if the volume is attached to a running instance
            attached_instance_id = attachments[0]['InstanceId']
            if attached_instance_id not in active_instance_ids:
                ec2.delete_volume(VolumeId=volume_id)
                print(f"Deleted EBS volume {volume_id} as it was not attached to a running instance.")
