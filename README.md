<h3 align="center">🛠️ thai-sso</h3>

<div align="center">
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=flat&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
  [![Python](https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
  [![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/axentx/thai-sso)
</div>

---

# 🚀 thai-sso  
**Power Thai organizations with compliant, self-hosted single sign-on.** A PDPA-by-design authentication solution that ensures data sovereignty while providing seamless user access.

## Why thai-sso?
- **PDPA Compliant**: Built-in consent management, data minimization, and audit logs for Thai Personal Data Protection Act compliance
- **Data Sovereign**: Self-hosted deployment options for on-premise or private cloud to keep sensitive authentication data within your control
- **Zero Data Exfiltration**: All authentication data remains within your infrastructure, satisfying strict data residency requirements
- **Enterprise Ready**: Built for organizations handling sensitive user information in regulated industries
- **Easy Integration**: Simple API for connecting with existing Thai enterprise applications and services
- **Audit Trail**: Comprehensive logging of all authentication events for compliance and security monitoring

## Feature Overview
| Feature | Description |
|---------|-------------|
| PDPA Authentication | Pre-built consent mechanisms and data minimization practices compliant with Thai regulations |
| Self-Hosting Options | Deploy on-premise or in private cloud with no data leaving your infrastructure |
| Audit Logging | Automatic recording of all authentication events and data access |
| Data Subject Requests | Built-in tools for handling user data access and deletion requests |
| Multi-Protocol Support | Supports SAML, OAuth 2.0, and OpenID Connect for various integration scenarios |
| Session Management | Secure session handling with configurable timeouts and refresh mechanisms |

## Tech Stack
- Node.js (JavaScript runtime)
- Python (backend services)
- Express.js (web framework)
- Flask (Python web framework)
- PostgreSQL (database)
- Redis (session storage)
- JWT (authentication tokens)
- Docker (containerization)

## Project Structure
```
thai-sso/
├── business/          # Business logic and domain models
├── src/              # Source code for core functionality
├── tests/            # Test suites for all components
├── thai_sso/         # Main application package
├── README.md         # Project documentation
├── auth.js           # JavaScript authentication module
├── auth.py           # Python authentication module
├── config.js         # JavaScript configuration
├── config.py         # Python configuration
├── main.py           # Python application entry point
├── models.py         # Database models
├── package.json      # Node.js dependencies and scripts
├── pyproject.toml    # Python project configuration
├── requirements.txt  # Python dependencies
└── session_manager.py # Session management logic
```

## Getting Started
```bash
# Install Node.js dependencies
npm install

# Install Python dependencies
pip install -r requirements.txt

# Run the application
npm run start  # For Node.js components
python main.py  # For Python components

# Run tests
npm test
python -m pytest tests/
```

## Deploy
```bash
# Build Docker containers
docker build -t thai-sso .

# Run with Docker Compose
docker-compose up -d

# Deploy to Kubernetes
kubectl apply -f k8s/
```

## Status
Active development with recent focus on PDPA compliance features. Last commit: axentx-dev-bot: docs cycle 20260611-171748-thai-sso

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.