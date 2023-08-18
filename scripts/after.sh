# Build and run the Docker image
source  constants.env

docker run -d --name testing_aws -p 80:80 "$ACCOUNT_NUMBER.dkr.ecr.$REGION.amazonaws.com/$REPOSITORY_NAME:$IMAGE_TAG"
