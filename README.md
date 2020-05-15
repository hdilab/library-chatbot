# UT Arlington Library Chatbot

The chatbot is being created to assist students and guests visiting the website of library at the University of Texas at Arlington.

Here, the [Rasa](https://rasa.com/docs/rasa/) framework is used to create a chatbot. For the project, conda is used as a package manager, and Rasa is installed inside a conda environment. 

> **Rasa**
> - We use conda to manage our python dependencies.
> - Create a separate conda environment. For more details on creating a conda environment, please follow the link [here](https://docs.conda.io/projects/conda/en/latest/user-guide/overview.html).
> - Activate your conda environment
> - Install Rasa framework via **$pip install rasa**
> - Check the version of rasa installed with the command **$rasa --version**

> **PostGres**
> - Postgres database is used to track conversations as well as store feedback of conversations.
> - Instructions to install it can be found at [https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04)
> - Change the default password by referring to [https://docs.bitnami.com/aws/infrastructure/postgresql/administration/change-reset-password/](https://docs.bitnami.com/aws/infrastructure/postgresql/administration/change-reset-password/)
> - Update the user and password in the files
>> - endpoints.yml (Under tracker_store)
>> - api.py

> **Google Maps**
> - The google maps API is integrated to display directions to various UTA buildings.
> - Details on the Map API can be found at [https://cloud.google.com/maps-platform](https://cloud.google.com/maps-platform)
> - The API key can be requested using the datacave@uta.edu account and updated in the file actions.py

> **Apache**
> - To setup apache follow the link at [https://ubuntu.com/tutorials/install-and-configure-apache#1-overview](https://ubuntu.com/tutorials/install-and-configure-apache#1-overview)
> - Edit the server files # TODO

> **File Contents**
> - nlu.md
>> - This file contains possible user intents. 
>> - The rasa models learns from the sentences defined in this file and associates user messages to these intents.
> - stories.md
>> - This file contains the sequence of events that a chat can follow.
>> - Here we can define what responses to take when a user enters a specific intent.
> - endpoints.yml
>> - This file is used to define different endpoints.
>> - We specify the actions endpoint as well as the tracker store details here. 
> - actions.py
>> - This file is used to define custom actions based on some user inputs.
> - database_script.py
>> - This file is used to create the initial table for feedback.
>> - The other tables required by rasa to track conversations are automatically generated.
> - widget
>> - This folder contains all the files for the UI interface.
>> - The index.html is the entry point.

> **Configuring for Testing**
> - Create Conda Environment 
>> - conda create --name chatbot python=3.6
>> - conda activate chatbot
>> - pip install rasa
>> - pip install psycopg2
> - Train Rasa model
>> - rasa train
>> - rasa run -m models --enable-api --log-file log.out --endpoints endpoints.yml --credentials credentials.yml --cors "*"
> - In a separate terminal Start the Action server
>> - rasa run actions
> - In a separate terminal Start the API server
>> - python api.py
> - We can then point the widget/index.html file to the test server by updating the socketUrl.
> - Next open the file in a browser to interact with the chatbot. 

> **Configuring on Server**
> - Additional to the steps listed above, we also need to configure an Apache server.
> - The Apache server is used to host the UI file listed under widget.
> - Copy the files from the widget folder to /var/www/html
> - We also need to configure the apache server to route all the requests to the correct port.
> - The reason for this is so that we do not need to open all the ports to the public.
> - This means that on the Chat server we will open only the 443 port. Internally the Apache server can be configured to route the other traffic to ports internally.
> - Configure the chat.ssl.conf file under /etc/apache2/sites-available route traffic to the internal ports. For Example for the feedback api path we can add
``` 
ProxyPass  /feedback http://localhost:5000/feedback nocanon
ProxyPassReverse  /feedback http://localhost:5000/feedback 
<Location http://localhost:5000/*>
    Order deny,allow
    Allow from all
</Location>
```
> - Restart Apache
>> - sudo systemctl restart apache2
