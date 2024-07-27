# Pizza Project app using Django
This project was done as a technical test to demonstrate knowledge in Python, k8s, CICD and SDLC best practices. Using Django for the web framework and Kubernetes for orchestration.

## Requirements

**Order Placement Form:** A form that allows users to place orders for pizza. This form should include: 
a. A dropdown menu for selecting the type of pizza (e.g., Margherita, Pepperoni, Vegetarian, etc.). 
b. A text area for comments or special instructions.

**Orders Table:** A page that displays all placed orders in a tabular format. Each row should display the type of pizza ordered and any comments associated with the order.

## Deployment Requirements:
1. Containerization: Containerize the web application using Docker. Provide a Dockerfile in your repository.
2. Kubernetes Deployment: Deploy your application to Kubernetes. Should include the necessary Deployments, Services, and any other resources needed to make the application accessible. **Ensure the application is scalable and can handle multiple instances.**

## Tech Stack

- **[Django](https://www.djangoproject.com/)**  is a Python-based free and open-source web framework,
 which follows the model-view-template architectural pattern. It is maintained by the Django Software. It is used in this project, to handle all routes, rendering pages and managing databases.

- **[Minikube](https://minikube.sigs.k8s.io/docs/start/)**  is local Kubernetes, focusing on making it easy to learn and develop for Kubernetes. All you need is Docker container or a Virtual Machine environment, and Kubernetes is a single command away: `minikube start`

## Deployment Steps

 - **Deploy using Docker**
 The project has a `Dockerfile` with which you can generate a container image. The steps to generate the image are as follows.

    - `cd pizzaproject`
    - `docker build --target=base -t {custom_image_name:custom_tag} .`
    <br>
    The `--target=base` flag is necessary to build only the application docker image, if you avoid this flag the resulting container image will run the tests application in the container, you could use the `--target=test` instead if you want to run the tests in the container.
    <br>
      Then to run the previous created image you will need to set an environment variable
      **SECRET_KEY**, this variable is needed to app run as expected, please refer to the contributors
      of this repo to get the value of the variable. 

	The command should see as follows:
    - `docker run -p 8000:8000 -e SECRET_KEY=$SECRET_KEY {custom_image_name:custom_tag}`
 
 - **Deploy using Helm**
	The project also have a Helm implementation to deploy the application in a target Kubernetes cluster, if you want to deploy the app locally, you can use minikube or similar to test the application with one or more instances, the helm chart permit the customization of different variables like the number of instances for the application, the image container, host path, the environment of the app, etc. 
		
	You will need to set an environment variable *SECRET_KEY*, this variable is needed to app run as expected, please refer to the contributors of this repo to get the value of the variable. 
	
	The steps to deploy the application locally using minikube are described below.
	First make sure you have installed minikube and it's running with the command:
	`minikube start`
	Then in the project folder go the helm folder and run the helm install command:
	- `cd helm`
	- `helm install pizzaproject . --set secret.djangoSecretKey=$SECRET_KEY`
	
	After creating the Release with the previous command you can make changes to the deployment values, which are found in the `values.yaml` file. To apply these changes you can use the helm upgrade command. Below is an example of how the command would look to apply the changes with the Release already created.
	- `helm upgrade --install pizzaproject .`
	
## CICD workflows
This project has workflows created to run as github actions pipelines, below we will describe what each of the files does.

 - **test.yaml:** This workflow will run on all the commits that the developers will do on the repo, it's responsible for running the unit tests created by the developers as well as validating the syntax of the project code (lint). If there is any failure in these validations, the workflow will be marked as failed and the developer should correct the errors indicated in its execution.
 - **deploy.yaml:** This workflow only will run on commit made on the main branch, since this is the production code of the app, it's in charge of build and push the prod base image that will be used in a helm release. The production base image can be found in: https://hub.docker.com/r/trebol256/pizzaproject/
