<div align="center">

<h1 align="center">Django4.2 Mini-inventory</h1>

</div>
<p align="center">
<a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
<a href="https://www.djangoproject.com/" target="_blank"> <img src="https://user-images.githubusercontent.com/29748439/177030588-a1916efd-384b-439a-9b30-24dd24dd48b6.png" alt="django" width="60" height="40"/> </a> 
<a href="https://www.docker.com/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a>
<a href="https://www.postgresql.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a>
<a href="https://www.nginx.com" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nginx/nginx-original.svg" alt="nginx" width="40" height="40"/> </a>
<a href="https://git-scm.com/" target="_blank"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a>

</p>

# Django4.2 Mini-inventory

A simple inventory management system built with Django 4.2, Docker, and PostgreSQL.

## Table of Contents
- Goal
- Prerequisites
- Development Usage
  - Clone the Repo
  - Environment Variables
  - Build Everything
  - Check it out in a Browser
- Stage Mode
- License
- Bugs
- Contributing
- Contact

## Goal
The primary objective of this project is to demonstrate a Data Center Infrastructure Management (DCIM) application using Django. This system aims to provide comprehensive management and visualization of data center infrastructure, including sites, data centers, rooms, racks, devices, cooling systems, power sources, and diesel generators.

## Prerequisites
- Docker
- Docker Compose
- Git

## Development Usage
You'll need to have Docker installed. It's available on Windows, macOS, and most distros of Linux. 

If you're using Windows, it will be expected that you're following along inside of WSL or WSL 2. That's because we're going to be running shell commands. You can always modify these commands for PowerShell if you want.

### Clone the Repo
Clone this repo anywhere you want and move into the directory:
```bash
git clone http://10.20.20.20/intern/mini-inventory.git
```


## Environment Variables
Create a .env file in the root directory and add the following variables:

DEBUG=True

SECRET_KEY=your_secret_key

DATABASE_URL=postgres://user:password@db:5432/your_db


## Build everything

*The first time you run this it's going to take 5-10 minutes depending on your
internet connection speed and computer's hardware specs. That's because it's
going to download a few Docker images and build the Python + requirements dependencies.*

```bash
docker compose up --build
```
Now that everything is built and running we can treat it like any other Django
app.

## Project Model Schema:
<p align="center">
<img src="https://github.com/user-attachments/assets/8249ef4e-8e97-4cba-b4d9-b272c3ee22b5" alt="database schema" width="560"/>
</p>

## Note

If you receive an error about a port being in use? Chances are it's because
something on your machine is already running on port 8000. then you have to change the docker-compose.yml file according to your needs.
## Check it out in a browser

Visit <http://localhost:8000> in your favorite browser.

## Stage Mode

To run the application in stage mode, use the following command:
```bash
docker-compose -f docker-compose.stage.yml up --build
```
## License

This project is licensed under the MIT License.

## Bugs

If you find any bugs, please report them by creating an issue.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Contact

For any questions or suggestions, feel free to contact me at mahdighadiriafzal@gmail.com