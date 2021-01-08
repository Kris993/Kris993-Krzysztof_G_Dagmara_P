## General:

### **Clone this repository for your computer**

#### Project has 3 chapters:
* chapter I
* chapter II
* chapter III
  
## Prerequisites:
- docker (install instruction: https://docs.docker.com/engine/install/ubuntu/)
- docker-compose (install instruction: https://docs.docker.com/compose/install/)
  * after install docker and docker-compose create the docker group 
        (https://docs.docker.com/engine/install/linux-postinstall/)
    
- psycopg2-binary
```bash
pip install -r requirements.txt
```

## Instructions
After the installation: docker, docker-compose, requirements.txt and creating the docker group:

* Chapter I
  * Chapter I is done in Chapter_I.py
  

* Chapter II
  * To add a task:  
    `python Chapter_II.py add --name "some name" --deadline "2020-1-8" --description "some description"`
    (deadline and description is not required)
    
  * To update a task:  
    `python Chapter_II.py update --name "new name" --deadline "2020-1-8" --description "new description" TASK_HASH`
    (you can update one or more arguments. TASK_HASH is required)
    
  * To remove a task:  
    `python Chapter_II.py remove TASK_HASH`
    
  * To list tasks:  
  `python Chapter_II.py list --all` to list all tasks  
  `python Chapter_II.py list --today` to list tasks for today
    

* Chapter III
  * Run `python Chapter_III.py`
  