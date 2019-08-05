# UT Arlington Library Chatbot


In this project, the [Rasa](https://rasa.com/docs/rasa/) framework is used to create a chatbot. For the project, Rasa is installed inside a conda environment. 

> **Instructions to install Rasa:**
> - Create a separate conda environment. If you need instructions to create a conda environment, please follow the link [here](https://docs.conda.io/projects/conda/en/latest/user-guide/overview.html).
> - Activate your conda environment
> - Install Rasa framework via **$pip install rasa**
> - Check the version of rasa installed with the command **$rasa --version**

Once you are able to see the version number with the command **$rasa --version**, then you are ready to start a rasa project.

> **Starting a Rasa project:**
> - Create a rasa project with the command **$rasa init --no-prompt**
> - The command will create the folowing files: __init__.py, __pycache__, actions.py, config.yml, credentials.yml, domain.yml, and endpoints.yml, and the following folders: data and models.

The training data for the chatbot will be provided inside **data > nlu.md**, and sample paths of conversations will be saved inside **data > stories.md**. Additionally the trained models will be stored in the **models** directory.
