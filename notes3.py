#####################################
##########  F  L  A  S  K  ##########
#####################################

# Virtual Env
# We use virtual env, so we can have own env with the required version of library that we need, and it doesn't have to interact with other env.

# Anaconda comes with its own environment manager.

# To create an env:
# -> conda create --name myenv

# To create an env with speific package included:
# -> conda create -n myenv numpy     # Over where numpy is the package name and myenv is the environment name

# To create an environment with a specific version of python
# -> conda create --name myenv python=3.5

# To create an env with specific package version included:
# -> conda create -n myenv numpy=1.4

#To list out all the environments
# -> conda env list

# for docs, check below:
# https://docs.conda.io/projects/conda/en/latest/

# Click on User guide and select tasks and then on Managing environments.
# It talks about all the different environments and how to manage it.

# For Flask, we will perform: 
# conda create -n myflaskenv flask
# 
# To activate env:
# conda activate myflaskenv
#
# To deactivate end:
# conda deactivate
#
