# ARCA Test

CLONE OR DOWNLOAD THIS REPO TO VERIFY THE TASKS.

A. Requirements to automate the 3 docker containers deployment with the bash script.

1. Install docker on your PC depending on your OS.
    https://docs.docker.com/engine/install/ 


2. Install docker-compose on your PC.
    https://docs.docker.com/compose/install/ 


3. Navigate to the DIR 'deploy_3_docker_containers' 


4. RUN 'bash automate.sh'


5. To test containers connectivity:
    a. sudo docker  exec -it (containerID) /bin/sh          
    b. ping servicename (e.g my_kibana/ my_mysql/ my_nginx)


ACCESS the nginx container on http://localhost:8092/



B. CloudFormation template to provision EC2 instance in the AWS default VPC.

1. Install awccli depending on your PC OS.
    https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html 

2. Configure AWS right profile with the neccessary permisions and select the default VPC location.

3. Navigate to the DIR 'deploy_aws_cloudformation'


4. RUN 'aws cloudformation create-stack --stack-name arca-stage --template-body file://$PWD/stack.yaml --profile arca --region us-east-2' 
    # Specify the stack-name and your default VPC location while running the command. 
    # RUN a similar command to delete the stack  'aws cloudformation delete-stack --stack-name arca-stage --profile arca --region us-east-2'


C. To start and stop EC2 instances with python script.

1. Install python3 and boto3 module on your PC depending on the OS.


2. To start the provisioned EC2 instance if the instance is in a stopped state, Navigate to the DIR 'python_automate_aws_EC2' and RUN 'python3 start_ec2.py'


3. To stop the provisioned running EC2 instance, Navigate to the DIR 'python_automate_aws_EC2' and RUN 'python3 stop_ec2.py'