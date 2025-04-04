

 Markdown
 Flask CI/CD App with Docker, PostgreSQL, and Render Deployment

This project is a simple Flask application demonstrating CI/CD, Dockerization, and cloud deployment using Render. It connects to a PostgreSQL database, adds and retrieves users, and automates deployment with GitHub Actions.



 Tech Stack

- Flask (Python Web Framework)
- PostgreSQL (Cloud-hosted on Render)
- Docker (for containerizing the app)
- GitHub Actions (for CI/CD pipeline)
- Render.com (for hosting the Flask app)



 Project Structure


├── app.py              # Flask app with routes
├── Dockerfile          # Docker instructions
├── requirements.txt    # Python dependencies
├── .github/workflows
│   └── main.yml        # GitHub Actions workflow
└── README.md           # Project documentation


 Features

- Add a user (`/add-user`)
- View all users (`/users`)
- Dockerized for easy deployment
- CI/CD pipeline with GitHub Actions
- Automatically deployed to Render on each push to `main`

🐳 Docker Instructions

 Build the Docker Image
bash
docker build -t my-python-app .


 Run the App Locally
bash
docker run -p 5000:5000 \
  -e DATABASE_URL="postgresql://flask_db_l8ys_user:3S02PJf9cSaburqEyYIFj8dTicQ4F85w@dpg-cvnsuk15pdvs73fs853g-a.oregon-postgres.render.com/flask_db_l8ys" talha777/my-python-app


🌐 Render Deployment

- App URL: [https://ci-cd-docker-0fst.onrender.com](https://ci-cd-docker-0fst.onrender.com/?_sm_au_=iVVN0QnJfv36qNqrML8tvK34L00HF)
- Database is provisioned on Render and connected via `DATABASE_URL` environment variable.

🔄 CI/CD Pipeline (GitHub Actions)

 On every push to `main`:
  - The Docker image is built
  - Image is pushed to Docker Hub
  - Render automatically redeploys the latest image

 GitHub Actions Workflow (`.github/workflows/main.yml`)

yaml
name: CI/CD Pipeline

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v2

      - name: Set up Docker
        uses: docker/setup-buildx-action@v1

      - name: Log in to Docker Hub
        uses: docker/login-action@v1
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      - name: Build and Push Docker Image
        run: |
          docker build -t ${{ secrets.DOCKER_USERNAME }}/my-python-app .
          docker push ${{ secrets.DOCKER_USERNAME }}/my-python-app

 Testing the App
- Visit `/add-user` to add a user
- Visit `/users` to view the user list

 Common Issues & Troubleshooting

- 500 Internal Server Error: Likely due to incorrect `DATABASE_URL` or DB table not initialized.
- "relation 'user' does not exist": Run a DB migration or create tables using SQLAlchemy before first use.
- Connection refused: Make sure PostgreSQL credentials are correct and accessible from Render.


 What I Learned

- How to build and containerize a Flask app
- Automate deployments using GitHub Actions
- Deploy full-stack app to Render
- Connect Flask to PostgreSQL in a production-ready way
- Troubleshooting real-world DevOps issues (dependency errors, networking, env variables)

 Screenshot

![image](https://github.com/user-attachments/assets/a9bdb2dd-8dc4-48d8-a094-ea325c2aba83)
![image](https://github.com/user-attachments/assets/faf55b64-51d7-41f4-bca9-f25e0d15adcd)
![image](https://github.com/user-attachments/assets/ca8c70a8-1afb-4747-a0e0-c95813575540)


 Contact

Made with ❤️ by Talha  
Reach out via [https://www.linkedin.com/in/talha-bin-fawad-5a31a3205/]) or open an issue in this repo.

