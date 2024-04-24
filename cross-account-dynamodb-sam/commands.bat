aws  cloudformation create-stack `
 --stack-name Cross-Account-Role-stack `
 --region ap-south-1 --profile agrima `
 --template-body file://role-lambda-acc-b.yaml `
 --capabilities CAPABILITY_NAMED_IAM

aws  cloudformation create-stack `
 --stack-name MilindB-DynamoDB-Stack   `
 --region ap-south-1 --profile agrima `
 --template-body file://dynamodb-acc-b.yaml

aws cloudformation package `
 --s3-bucket milindb-sam-bucket-2024 `
 --template-file template.yaml `
 --output-template-file gen/template-generated.yaml

aws cloudformation deploy `
 --template-file gen/template-generated.yaml `
 --stack-name dynamodb-cross-account `
 --capabilities CAPABILITY_NAMED_IAM

aws  cloudformation update-stack `
 --stack-name Cross-Account-Role-stack `
 --region ap-south-1 --profile agrima `
 --template-body file://role-lambda-acc-b.yaml `
 --capabilities CAPABILITY_NAMED_IAM