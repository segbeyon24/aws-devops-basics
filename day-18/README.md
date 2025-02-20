# AWS Cloud Cost Optimization - Identifying Stale Resources

## Identifying Stale EBS Snapshots

In this example, we'll create a Lambda function that identifies EBS snapshots that are no longer associated with any active EC2 instance and deletes them to save on storage costs.

### Description:

The Lambda function fetches all EBS snapshots owned by the same account ('self') and also retrieves a list of active EC2 instances (running and stopped). For each snapshot, it checks if the associated volume (if exists) is not associated with any active instance. If it finds a stale snapshot, it deletes it, effectively optimizing storage costs.


## Steps [to apply any of the functions]
1. Create a lambda function
2. Paste the code from this repo (in the IDE, at the `code` tab)
3. Go to the `onfiguration` tab
4. Increase the function invokation period from the default 3 seconds to 7 or 10 seconds (Note: aws charges nore as the duration increases)
5. Click on the `Permissions` on the left sidebar (still on the `configuration` tab)
6. click on the on the auto-generated (link) role name of the new function. At `Permissions policies`, click on `Add prmission` to create a policy and also to attach the policy to the role.
7. For the tasks that either of the functons in this repo would can perform, they are limited to ec2, snapshots and volumes. Both functions need `ec2:DescribeInstances` policy, while each of them need the describe and delete permissions for snapshot and volumes.
8. Save
9. Go back to `code` and deploy and test the function. Confirm if the resources have all been deleted.
10. Clean up-  by deleting the function(s), role(s) and policy(s)
11. Beyond a one-time usage of the function, use AWS Cloudwatch to schedule and monitor the implementation of the function subsequently.

