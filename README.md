# Q-DashMan
Q-DashMan is a web application used to generate dashboards with metrics about a software's project development in an easy way. For that, we use Django (as development's framework of web applications) and GrimoireLab's tools (several tools to collect, analyze and view metrics about software's development).

![SetupGeneral](/templates/static/img/grimoirelab-qdashman.png)

Q-DashMan uses several GrimoireLab’s tools.  Its final goal is to export data from the systems where you develop and analyze the software to produce at the end a dashboard that shows interesting metrics in an interactive way.  Q-DashMan let specifying which ones are those systems for a specific project and manages the whole process till the dashboard is ready to work.

GrimoireLab’s tools used are the following:
* SirMordred: Orchestration.
* Perceval: Data collection.
* Sortinghat: Affiliate identities automatically.
* Sigils: Data Visualization.

Consequently, GrimoireLab gives you the tools you need. However, writing files set forMordred is difficult and boring and it forces you to let the machine access to the place where the analysis is going to happen due to you need to manage the set file and run the tools.

In this part of the process is where Q-DashMan offers an alternative: an app who offers the generation of dashboards as a service. The user interface that it offers is very simple comparted with the files set by SirMordred, you’d only need to complete some files to specify the data source of the project you’re going to analyze.

Set up the projects file
![Projects](/templates/static/img/projects-add.png)
Add data sources
![SetupAddDataSource](/templates/static/img/setup-add.png)
Set up SirMordred file
![SetupGeneral](/templates/static/img/setup-general.png)

All the rest is completely automatic since Q-DashMan produces a dashboard hiding the difficult use of all GrimoireLab’s tools to the user.

We used development web standard technologies to built Q-DashMan based on Django framework.  The tool is written in Python, it uses a database MariaDB and it can be deployed in a simple way by using Docker containers. The tool is easy to deploy and it’s being used as a trial in environments as preproduction to build dashboards in more than 10 different projects.

As a conclusion, Q-DashMan is designed to offer the generation of development software projects dashboards as an automatic service, generated by users with any management.

An example of the dashboard created by Q-DashMan
![Dashboard](/templates/static/img/kibana-git.png)
    
# Requirements
* docker => 18.03.1-ce
* docker-compose => 1.13.0
* beautifulsoup4 => 4.6.3
* bs4 => 0.0.1
* certifi => 2018.11.29
* chardet => 3.0.4
* Django => 2.0.5
* idna => 2.7
* pkg-resources => 0.0.0
* pytz => 2018.7
* PyYAML => 3.13
* requests => 2.18.4
* urllib3 => 1.24.1
* yml => 0.0.1

# Docker containers
You must have an ElasticSearch, Kibana, and MariaDB running in a docker container before installing Q-DashMan.

### ElasticSearch + Kibiter
docker-compose.yml
```
elasticsearch:
  restart: on-failure:5
  image: bitergia/elasticsearch:6.1.0
  command: /elasticsearch/bin/elasticsearch -Enetwork.bind_host=0.0.0.0 -Ehttp.max_content_length=2000mb
  environment:
    - ES_JAVA_OPTS=-Xms2g -Xmx2g
  ulimits:
    nofile:
      soft: 65536
      hard: 65536
  ports:
    - "9200:9200"
  log_driver: "json-file"
  log_opt:
    max-size: "100m"
    max-file: "3"

kibiter:
  restart: on-failure:5
  image: bitergia/kibiter:optimized-v6.1.4-2
  environment:
    - PROJECT_NAME=TEST
    - NODE_OPTIONS=--max-old-space-size=1200
    - ELASTICSEARCH_URL=http://elasticsearch:9200
  links:
    - elasticsearch
  ports:
    - "5601:5601"
  log_driver: "json-file"
  log_opt:
    max-size: "100
```

### MariaDB
docker-compose.yml
```
mariadb:
  restart: on-failure:5
  image: mariadb:10.0
  expose:
    - "3306"
  environment:
    - MYSQL_ROOT_PASSWORD=
    - MYSQL_ALLOW_EMPTY_PASSWORD=yes
  command: --wait_timeout=2592000 --interactive_timeout=2592000 --max_connections=300
  log_driver: "json-file"
  log_opt:
      max-size: "10
```

# Installation

`$ git clone https://github.com/zhquan/Q-DashMan.git`

`$ cd Q-DashMan`

`$ pip install -r requirements.txt`

`$ python3 manage.py migrate --run-syncdb`

`$ python3  manage.py migrate`

`$ python3 manage.py makemigrations`

`$ python3 manage.py runserver`

# Modify `models.py`
When you modify the `module.py` file, you have to delete the old database and create a new one.

`$ python3 rm db.sqlite3`

`$ python3 manage.py migrate --run-syncdb`

`$ python3 manage.py migrate`

`$ python3 manage.py makemigrations`

`$ python3 manage.py createsuperuser`

# License
Licensed under GNU General Public License (GPL), version 3 or later.
