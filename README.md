# The thumbnail generator on AWS

* The pourpoise is provide the step-by-step guide to implement a thumbnail generator using AWS Cloudformation
* The pipeline to use will be:
  S3(Source) --> |Object Upload| Lambda (Trigger) --> |Start Function| Lambda (Processing) --> |Get Object| S3(Source Image)
* We will considered the schematic option from Cloud formation and the yaml snipset.

## Resources used:
* **Python version:** 3.8
* **Packages:** PIL and boto3
* Based on a test for a job as data engineer

## The pipeline
! [alt text] (enlace a imagen)
