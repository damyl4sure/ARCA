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
    b. ping servicename




B. CloudFormation template to provision EC2 instance in the AWS default VPC.

1. Install awccli depenind on your PC OS.
    https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html 

2. Configure AWS right profile with the neccessary permisions and select the default VPC location.

3. Navigate to the DIR 'deploy_aws_cloudformation'


4. RUN 'aws cloudformation create-stack --stack-name arca-stage --template-body file://$PWD/stack.yaml --profile arca --region us-east-2' 
    # Specify the stack-name and your default VPC location while running the command. 
    # RUN a similar command to delete the stack  'aws cloudformation delete-stack --stack-name arca-stage --profile arca --region us-east-2'

