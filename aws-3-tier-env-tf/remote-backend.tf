terraform {
  backend "s3" {
    bucket         = "avinash-terraform-remote-state"
    key            = "terraform.tfstate" # The path to the state file within the bucket
    region         = "us-east-1"
    dynamodb_table = "tf-backend-remote-lock"   # Optional: DynamoDB table for state locking
  }
}
