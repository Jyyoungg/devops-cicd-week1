# DevOps CI/CD Project - Week 1

This project demonstrates a basic CI/CD pipeline using GitHub Actions and Heroku deployment.

## Project Overview
- Simple Python Flask web application
- Continuous Integration with GitHub Actions
- Continuous Deployment to Heroku
- Automated testing and deployment pipeline

## Tech Stack
- Python 3.x
- Flask
- GitHub Actions
- Heroku

## Local Development
1. Clone the repository:
```bash
git clone https://github.com/Jyyoungg/devops-cicd-week1.git
cd devops-cicd-week1
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

## CI/CD Pipeline
This project uses GitHub Actions for CI/CD. The pipeline:
1. Triggers on push to main branch
2. Runs tests
3. Deploys to Heroku if tests pass

## Project Structure
```
├── .github/
│   └── workflows/
│       └── deploy.yml
├── app.py
├── requirements.txt
├── tests/
│   └── test_app.py
└── README.md
```

## Progress Tracking
- [x] Set up GitHub repository
- [x] Create basic Flask application
- [x] Set up local development environment
- [ ] Configure GitHub Actions
- [ ] Deploy to Heroku
- [ ] Complete CI/CD pipeline

## Documentation
Detailed documentation of the setup process and learning outcomes will be maintained in the [docs](./docs) directory.