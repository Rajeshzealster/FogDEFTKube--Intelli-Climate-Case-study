#!/bin/bash

# Set the K3s namespace and context
NAMESPACE=default
CONTEXT=default

# Loop through all deployments in the namespace
for DEPLOYMENT in $(kubectl get deployments -n $NAMESPACE -o jsonpath='{range .items[*].metadata.name}{@}{"\n"}{end}' --context $CONTEXT); do
    # Get the image name of the running deployment
    IMAGE=$(kubectl get deployment $DEPLOYMENT -n $NAMESPACE -o jsonpath="{.spec.template.spec.containers[*].image}" --context $CONTEXT)
    #echo "$IMAGE"

    # Get the latest image ID from Docker Hub
    LATEST_IMAGE_ID=$(curl -s "https://registry.hub.docker.com/v2/repositories/$IMAGE/tags/latest" | jq -r '.images[0].digest')

    # Get the ID of the running image
    RUNNING_IMAGE_ID=$(docker inspect --format='{{.Id}}' $IMAGE)
    
    #echo " Running image id: $RUNNING_IMAGE_ID , latestimage id: $LATEST_IMAGE_ID"

    # Compare the image IDs
    if [ $RUNNING_IMAGE_ID != $LATEST_IMAGE_ID ]; then
        echo "Deployment $DEPLOYMENT is not using the latest image"
        echo "Current image id: ${RUNNING_IMAGE_ID}"
    	echo "Latest image id: ${LATEST_IMAGE_ID}"
    	#echo $DEPLOYMENT
    	
    	# Trigger a rolling update of the deployment with the latest image
    	kubectl rollout restart deployment "${DEPLOYMENT}" -n "${NAMESPACE}"
    else
  	echo "Deployment $DEPLOYMENT is using the latest image"
    fi
done

