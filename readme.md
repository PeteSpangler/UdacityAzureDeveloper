# Welcome

Pete Spangler's repository for assignments and practice files for [Udacity Azure Developer Nanodegree](https://www.udacity.com/course/developer-for-microsoft-azure-nanodegree--nd081).

[//]: # (Image References)
[graduation]: ./AzureNanodegree.PNG "Graduation"

## Project 1: Deploying Flask CMS (Azure Applications)
- [Code](./Article_CMS_Project)
- Implemented Sign In With Microsoft with MSAL library
- Created Azure SQL Database connection for blog posts to be saved and served from
- Brief analysis of choices made for deployment, [VM or App Service](./Article_CMS_Project/WRITEUP.md/).

## Project 2: Deploying Neighborly App with Azure Functions (Azure Microservices)
- [Code](./Neighborly_APP)
- Deployed Azure Functions (HTTP Trigger) in Back Ends for Front Ends design pattern.
- Connected APP with MongoDB Database in CosmosDB Azure.
- Setup CI/CD of Dockerized Azure Functions with Kubernetes.
- Created an Event Hub based on a Logic App with HTTP Trigger.

## Project 3: Migrating App to Azure (Azure Migration)
- [Code](./Migrate_App_to_Azure)
- Migrated and deployed pre-existing web app to Azure App Service.
- Migrated a PostgreSQL database to an Azure Postgres database.
- Refactored notification logic to an Azure Function via service bus queue message.

## Project 4: Enhancing Applications (Azure Performance)
- [Code](./Enhancing_Applications)
- Setup Application Insights monitoring on a VMSS and implemented monitoring in the application to collect telemetry data.
- Setup auto-scaling on a VMSS.
- Setup Azure Automation and created a Runbook to automate the resolution of performance issues.
- Created alerts to trigger auto-scaling on an AKS clsuter and trigger a RunBook to execute.

# Graduated December 2020
[Nanodegree Certificate Verification Link](https://graduation.udacity.com/confirm/UHPTK6LA)
![Certificate][Graduation]