# UT Arlington Library Chatbot

The chatbot is being created to assist students and guests visiting the website of library at the University of Texas at Arlington.

Here, the [Rasa](https://rasa.com/docs/rasa/) framework is used to create a chatbot. For the project, conda is used as a package manager, and Rasa is installed inside a conda environment. 

> **Instructions to install Rasa:**
> - Create a separate conda environment. If you need instructions to create a conda environment, please follow the link [here](https://docs.conda.io/projects/conda/en/latest/user-guide/overview.html).
> - Activate your conda environment
> - Install Rasa framework via **$pip install rasa**
> - Check the version of rasa installed with the command **$rasa --version**

Once you are able to see the version number with the command **$rasa --version**, then you are ready to start a rasa project.

> **Starting a Rasa project:**
> - Create a rasa project with the command **$rasa init --no-prompt**
> - The command will create the following files: __init__.py, actions.py, config.yml, credentials.yml, domain.yml, and endpoints.yml, and the following folders: data and models.

The training data for the chatbot will be provided inside **data > nlu.md**, and sample paths of conversations will be saved inside **data > stories.md**. Additionally the trained models will be stored in the **models** directory.

**How to Use this repository to run in your local machine**
> Once you clone this repository, please follow this procedure:
> - Open widget_test.html in Safari, Google Chrome, or Firefox
> - Open two terminal windows and activate your rasa environment in both terminal windows
> - In one terminal, run the command **rasa run -m models --enable-api --log-file log.out --endpoints endpoints.yml --credentials credentials.yml**
> - In the next terminal, run the command **rasa run actions**
> - Go to your browser with the tab widget_test.html, and click on the blue chat icon on the bottom-left corner.
> Follow the prompt or type your questions.
