# Detailed Setup Guide

## Prerequisites
- Python 3.9 installed
- Git installed
- GitHub account
- Render account

## Local Development Setup

### 1. Environment Setup
```bash
# Clone the repository
git clone https://github.com/jyyoungg/devops-cicd-week1.git
cd devops-cicd-week1

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration
The application uses environment variables for configuration:
- `FLASK_ENV`: Set to 'development' for local development
- `PORT`: Default is 5000

Create a `.env` file in the root directory:
```
FLASK_ENV=development
PORT=5000
```

### 3. Running Tests
```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=app tests/
```

## CI/CD Pipeline Setup

### 1. GitHub Actions Configuration
The workflow in `.github/workflows/ci-cd.yml` handles:
- Automated testing on push/PR to main branch
- Deployment to Render on successful merge to main

### 2. Render Setup
1. Create a new Web Service in Render
2. Connect your GitHub repository
3. Configure the following:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Environment Variables:
     - `PYTHON_VERSION`: 3.9.0
     - `FLASK_ENV`: production

### 3. Environment Variables
Required secrets in GitHub repository:
- `RENDER_API_KEY`: Your Render API key for automated deployments

## Application Structure

### Main Components
1. `app.py`: Flask application with route definitions
2. `render.yaml`: Render deployment configuration
3. `requirements.txt`: Python dependencies
4. `tests/`: Test files
5. `.github/workflows/`: CI/CD configuration

### Routes
- `/`: Home page displaying environment information

## Best Practices
1. Always work in a virtual environment
2. Run tests before committing changes
3. Follow Git commit message conventions
4. Keep dependencies updated
5. Monitor deployment logs in Render dashboard

## Troubleshooting
Common issues and solutions:

1. **Tests failing locally**
   - Ensure virtual environment is activated
   - Verify all dependencies are installed
   - Check Python version matches project requirements

2. **Deployment failures**
   - Verify Render configuration
   - Check application logs in Render dashboard
   - Ensure all environment variables are set correctly

3. **GitHub Actions issues**
   - Verify workflow file syntax
   - Check repository secrets are configured
   - Review Action logs for detailed error messages