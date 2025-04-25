# DevOps CI/CD Project - Week 1

This project demonstrates a basic CI/CD pipeline using GitHub Actions and Render deployment.

## Project Overview
- Simple Python Flask web application
- Continuous Integration with GitHub Actions
- Continuous Deployment to Render
- Automated testing and deployment pipeline

## Quick Start
1. Clone and setup:
```bash
git clone https://github.com/Jyyoungg/devops-cicd-week1.git
cd devops-cicd-week1
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. Run locally:
```bash
python app.py
```

Visit `http://localhost:5000` to view the application.

## Tech Stack
- Python 3.9
- Flask 3.0.2
- pytest 8.0.2
- GitHub Actions
- Render (for deployment)
- Gunicorn 21.2.0 (production server)

## Documentation
- [Complete Setup Guide](docs/setup-guide.md)
- [Local Development Guide](docs/setup-guide.md#local-development-setup)
- [CI/CD Pipeline Setup](docs/setup-guide.md#ci-cd-pipeline-setup)
- [Troubleshooting Guide](docs/setup-guide.md#troubleshooting)

## Project Structure
```
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # CI/CD workflow configuration
├── docs/
│   └── setup-guide.md        # Detailed documentation
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── render.yaml              # Render deployment configuration
├── tests/
│   └── test_app.py          # Application tests
└── README.md                # Project overview
```

## Features
- Responsive web interface
- Environment-aware configuration
- Automated testing
- Continuous deployment
- Production-ready setup

## Progress Tracking
- [x] Set up GitHub repository
- [x] Create basic Flask application
- [x] Set up local development environment
- [x] Configure GitHub Actions
- [x] Add comprehensive documentation
- [x] Deploy to Render
- [x] Complete CI/CD pipeline
- [x] Add testing suite

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments
- Flask documentation
- GitHub Actions documentation
- Render deployment guides
- Python testing best practices