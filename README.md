# EKS pulumi (Python+Scrapy+celary)
### Utilising Pulumi to create a EKS insfra structure in a minute and deploy a scraping project that uses distributed message queue.

#### Library/Technology

| Library/Technology | Purpose |
|--------------------|---------|
| Pulumi             | Infrastructure as code tool for defining, deploying, and managing cloud infrastructure using familiar programming languages. |
| pulumi-awsx        | Higher-level abstraction for working with AWS infrastructure resources in Pulumi, simplifying the process of defining and managing AWS resources. |
| pulumi-eks         | Abstractions for working with Amazon EKS clusters in Pulumi, simplifying the deployment and management of Kubernetes clusters on AWS. |
| Celery             | Managing concurrent requests efficiently for web scraping. |
| Docker             | Containerization of the Scrapy project for portability and ease of deployment. |
| Kubernetes         | Orchestration platform for deploying and managing containerized applications. |
| psycopg2-binary    | Optional: PostgreSQL adapter for interacting with PostgreSQL databases if storing scraped data. |
| python-dotenv      | Loading environment variables for managing configuration settings securely. |
| Scrapy             | Web scraping framework for extracting data from IMDb's Top 50 movies list. |
| SQLAlchemy         | Optional: ORM library for interacting with relational databases if storing scraped data. |
| AWS EKS            | Kubernetes service on AWS for deploying the Dockerized Scrapy scraper with scalability and reliability. |
| AWS Secrets Manager| Securely handling sensitive configurations like API keys or database credentials. |
| Github Actions     | Manage CI CD and automatic deployment on main branch |

<br/>
<br/>

### Instructions 

#### 1. Setup Infrastucture
**1.1 pulumi setup**
```bash
cd resources/iaac 
```


*if venv is not yet generated*

```bash
python -m venv venv
```


*Active venv*

```bash
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

<br/>

**1.2 Setup aws**

Get you secret acesss key from  AWS IAM. then setup you creds into cli. CLI setup [instruction](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

```
aws configure
```


<br />
**1.3 Spin up pulumi*

```
pulumi up
```

<br />

**1.4 Spin down**
```
pulumi down
```


## 2. Scraper Project instruction 

**Pre requsite:** Postgres, redis. 

**Setup**

```
cd /scaper
```

```
python -m venv venv
```

```
source venv/bin/active
```


**2.1 Scraper Project**

Crawls through imdb top 250 website visit each pages and sends datas to queue.

```
scrapy crawl imdb
```

**2.2 Worker Project**

Recieved datas from the scraper and upset them into database.

```
celery -A scraper worker --loglevel=info
```



