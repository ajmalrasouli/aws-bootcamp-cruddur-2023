# Week 11 — CloudFormation Part 2

## Required Homework/Tasks

Final Cruddur Network Diagram using draw.io


<img src="https://raw.githubusercontent.com/ajmalrasouli/aws-bootcamp-cruddur-2023/d6ff9e9ac9c20c65224d65d042e1530303b2e863/journal/assets/Network%20Diagram.drawio.svg" alt="network diagram" title="cruddur network diagram" style="max-width: 100%;">



![01 - week-11-CrdSrvBackendFlask-error](https://github.com/ajmalrasouli/aws-bootcamp-cruddur-2023/assets/88502375/0ae5d57c-1e76-4aff-a78c-c7a7790c83a9)

![03 - week-11-db-stacks](https://github.com/ajmalrasouli/aws-bootcamp-cruddur-2023/assets/88502375/e0568e9a-69de-49bb-a80f-879dbaa89298)

![05 - week-11-backend-flask-health-check](https://github.com/ajmalrasouli/aws-bootcamp-cruddur-2023/assets/88502375/7a16314c-0484-46d6-94fc-a6783b39b75a)

![06 - week-11-CrdSrvBackendFlask](https://github.com/ajmalrasouli/aws-bootcamp-cruddur-2023/assets/88502375/62c2ca87-b436-478f-a00e-c305edd6fbee)

![07 - week-11-sam-validation-template yaml](https://github.com/ajmalrasouli/aws-bootcamp-cruddur-2023/assets/88502375/616816c8-cbfc-4fd4-914f-992b4e3ad787)

![08 - week-11-CrdDdb-stack-created](https://github.com/ajmalrasouli/aws-bootcamp-cruddur-2023/assets/88502375/97f30d50-6d81-45b8-af79-882b24bba00b)

![09 - week-11-ddb-folder-on-s3](https://github.com/ajmalrasouli/aws-bootcamp-cruddur-2023/assets/88502375/79bd08ca-592b-49ee-bd05-1696e04dfef1)

![10 - week-11-ddb-folder-on-s3](https://github.com/ajmalrasouli/aws-bootcamp-cruddur-2023/assets/88502375/4d683a1b-5ce5-4ba3-9bbc-e92fce2c4a74)

![12 - week-11-backend-codepipeline](https://github.com/ajmalrasouli/aws-bootcamp-cruddur-2023/assets/88502375/92381fe6-8c28-4da4-af0e-93ef7d4461c0)

![13 - week-11-backend-codepipeline](https://github.com/ajmalrasouli/aws-bootcamp-cruddur-2023/assets/88502375/f5fc31b7-0429-4916-8b40-859790f890c0)

![14 - week-11-cicd](https://github.com/ajmalrasouli/aws-bootcamp-cruddur-2023/assets/88502375/67596c52-be32-4457-b22e-ba6cf2a9a9a0)

![15 - week-11-cicd-codepipeline](https://github.com/ajmalrasouli/aws-bootcamp-cruddur-2023/assets/88502375/5ce32c2e-303c-400e-9dea-024b63d5f296)

![16 - week-11-cicd-codepipeline](https://github.com/ajmalrasouli/aws-bootcamp-cruddur-2023/assets/88502375/c8f67346-e45a-438d-b81c-f62604b71ed7)

![17 - week-11-cicd-codepipeline](https://github.com/ajmalrasouli/aws-bootcamp-cruddur-2023/assets/88502375/eb2e236d-df05-496c-a79d-6e1046919ba7)

![18 - week-11-cicd-codepipeline](https://github.com/ajmalrasouli/aws-bootcamp-cruddur-2023/assets/88502375/21a62620-7c01-4dab-9b1b-c351e3d23333)

![19 - week-11-cloudfront](https://github.com/ajmalrasouli/aws-bootcamp-cruddur-2023/assets/88502375/22d99e3e-09f6-4eb5-a446-62133eece9e2)

![20 - week-11-zip-build](https://github.com/ajmalrasouli/aws-bootcamp-cruddur-2023/assets/88502375/47bd08c1-a855-4a6f-99b5-03e860a53161)

![21 - week-11-syncing-tool](https://github.com/ajmalrasouli/aws-bootcamp-cruddur-2023/assets/88502375/1f3ef5ac-c806-40b6-afb3-e81dfda9b95f)

![22 - week-11-github](https://github.com/ajmalrasouli/aws-bootcamp-cruddur-2023/assets/88502375/09d8ff4a-b857-4b9b-8681-2bc234176636)

![22 - week-11-github-access-token](https://github.com/ajmalrasouli/aws-bootcamp-cruddur-2023/assets/88502375/b55e5847-c73e-4e4b-9be3-30b0f20fd135)

![23 - week-11-github-access-token](https://github.com/ajmalrasouli/aws-bootcamp-cruddur-2023/assets/88502375/79f2ada7-468b-4bfd-8f33-76fb52e70707)

![24 - week-11-github-workflows-permissions](https://github.com/ajmalrasouli/aws-bootcamp-cruddur-2023/assets/88502375/5582c391-2b35-4f7d-96c8-0595beb93f2e)

![25 - week-11-list-of-s3-bucket-using-aws-cli](https://github.com/ajmalrasouli/aws-bootcamp-cruddur-2023/assets/88502375/0c7fcc90-17e7-458e-8d1e-d0fbf1bc1b60)

![26 - week-11-database-sg](https://github.com/ajmalrasouli/aws-bootcamp-cruddur-2023/assets/88502375/42b89d05-f756-4087-b4bd-ad734fa13527)

![27 - week-11-connect-to-prod](https://github.com/ajmalrasouli/aws-bootcamp-cruddur-2023/assets/88502375/05fc5d17-6bd3-4abf-b95b-016d509c6896)

![27 - week-11-databas-add-bio-column](https://github.com/ajmalrasouli/aws-bootcamp-cruddur-2023/assets/88502375/a586facd-6747-493e-9a6c-1efac318b647)

![28  - week-11-codepipeline](https://github.com/ajmalrasouli/aws-bootcamp-cruddur-2023/assets/88502375/ba301e2c-9b26-4e91-bcf8-44ccf06a98e7)

![29 - week-11-codepipeline](https://github.com/ajmalrasouli/aws-bootcamp-cruddur-2023/assets/88502375/3708dfd2-478e-47da-a3e3-56f722ef6f26)

![30 - week-11-codepipeline-successeed](https://github.com/ajmalrasouli/aws-bootcamp-cruddur-2023/assets/88502375/1e28dea6-39b4-4d27-8512-567224b79765)

![31  - week-11-clean](https://github.com/ajmalrasouli/aws-bootcamp-cruddur-2023/assets/88502375/766b76e0-c548-4136-99c0-3aecd6a55c9f)

![35 - week-11-crdmachineuser](https://github.com/ajmalrasouli/aws-bootcamp-cruddur-2023/assets/88502375/6f21b028-d09a-4a7e-83ff-15a56d6d0694)
