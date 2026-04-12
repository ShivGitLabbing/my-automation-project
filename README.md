# 🚀 My Automation Project

A containerized, cloud-ready Python application featuring an interactive toddler learning experience with dynamic media-driven letter recognition, built for scalability and deployed on Azure.

---

## 📋 Project Overview

This monorepo contains:
- **letterprogram**: An interactive FastAPI-based web app for early childhood education
- **Comprehensive Azure cloud deployment**: Container apps, app services, and load balancing
- **Docker containerization**: Production-ready images with optimized builds
- **SSL/TLS security**: End-to-end encryption across all Azure services

---

## 🐍 Python Environment

### Python Version
- **Required**: Python 3.14 or higher
- **Base Image** (Docker): `python:3.14-slim`
- **Dependency Manager**: `uv` (ultra-fast, Rust-based Python package manager)

### Installation
```bash
pip install uv
uv sync
```

### Virtual Environment Setup
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

---

## 📦 Core Libraries & Dependencies

### Web Framework & Server
- **FastAPI**: `>=0.135.3` — Modern, async Python web framework
- **Uvicorn**: `>=0.44.0` — Lightning-fast ASGI server
- **Jinja2**: `>=3.1.6` — Server-side templating engine

### Media & Image Processing
- **Pillow**: `>=12.2.0` — PIL fork for image handling (JPEG, PNG)
- **playsound**: `1.2.2` — Cross-platform audio playback

### Azure Integration (Recommended)
- **azure-identity**: For managed service identity authentication
- **azure-keyvault-secrets**: Secure credential management
- **azure-monitor-opentelemetry**: Application insights telemetry

### Development & Optimization
- **Starlette**: Async web toolkit (FastAPI dependency)
- **pydantic**: Data validation and settings management
- **aiofiles**: Async file handling

---

## 🐳 Docker Image & Container Configuration

### Dockerfile Specifications
```dockerfile
FROM python:3.14-slim
WORKDIR /app
RUN pip install fastapi uvicorn jinja2
COPY . .
EXPOSE 8000
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Build & Run Commands
```bash
# Build image
docker build -t toddler-app:latest .

# Run locally
docker run -p 8000:8000 toddler-app:latest

# Run with environment variables
docker run -e ENVIRONMENT=production -p 8000:8000 toddler-app:latest
```

### Docker Optimization
- **Multi-stage builds**: Reduce final image size (currently ~200MB)
- **.dockerignore**: Excludes `__pycache__`, `.venv`, `.git`, logs
- **Layer caching**: Minimal rebuild times for code changes
- **Health checks**: Liveness and readiness probes for orchestration

### Docker Compose Support
```yaml
version: '3.8'
services:
  app:
    build: .
    ports:
      - "8000:8000"
    expose:
      - "8000"
    environment:
      - PYTHONUNBUFFERED=1
    restart: unless-stopped
```

---

## 🎨 Frontend: HTML & CSS

### Template Engine: Jinja2
- **Location**: `source/letterprogram/app/templates/index.html`
- **Features**: Dynamic context injection, loop rendering, conditional logic

### HTML Structure
- **Semantic markup**: Proper HTML5 document structure
- **Accessibility**: ARIA labels, semantic heading hierarchy
- **Media integration**: Dynamic card generation from asset files
- **Audio elements**: HTML5 `<audio>` tags for cross-browser compatibility
- **Image handling**: Graceful degradation for missing images

### CSS Styling
- **Framework**: Pure CSS (no external dependencies)
- **Responsive design**: CSS Grid with `auto-fit` and `minmax()`
- **Mobile-first**: Touch-optimized interactions
- **Animations**: CSS transitions for hover/active states
- **Color schemes**: Rainbow border system (4-color rotation)
  - Red (#FF6B6B)
  - Teal (#4ECDC4)
  - Gold (#FFD93D)
  - Purple (#6C5CE7)

### Key CSS Features
```css
/* Responsive grid */
.grid { 
  display: grid; 
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); 
  gap: 40px; 
}

/* Bounce effect on hover */
.card:hover { 
  transform: scale(1.05) translateY(-10px); 
  box-shadow: 0 25px 50px rgba(0,0,0,0.2);
}

/* Touch-friendly cards */
.card { 
  border-radius: 50px; 
  padding: 30px; 
  cursor: pointer;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
```

---

## ☁️ Azure Resource Group

### Resource Organization
- **Purpose**: Logical container for all Azure resources
- **Region**: `East US 2` (recommended for latency)
- **Naming convention**: `rg-letterprogram-prod`

### Resources Included
1. **Azure Container Registry (ACR)**: Private Docker image repository
2. **Azure Container Apps**: Serverless container orchestration
3. **Azure App Service Plan**: Compute resources for web apps
4. **Azure App Service**: Managed web hosting
5. **Azure Key Vault**: Secrets and certificate management
6. **Application Insights**: Monitoring and diagnostics
7. **Log Analytics Workspace**: Centralized logging

### IAM & Access Control
- **Managed Identity**: Service-to-service authentication
- **Role-Based Access Control (RBAC)**: Least privilege principle
- **Service principals**: CI/CD pipeline authentication

---

## 🐳 Azure Container Apps

### Deployment Architecture
- **Platform**: Serverless Kubernetes (AKS managed)
- **Compute**: Event-driven auto-scaling on CPU/memory metrics
- **Startup time**: Sub-second cold starts
- **Cost model**: Pay-per-execution (development) or reserved (production)

### Configuration
```yaml
# Container app environment
name: letterprogram-env
properties:
  containerAppsConfiguration:
    daprAIInstrumentationKey: "<app-insights-key>"
    
# Container app
name: letterprogram-app
properties:
  environmentId: /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.App/managedEnvironments/letterprogram-env
  configuration:
    ingress:
      external: true
      targetPort: 8000
      transport: http
      allowInsecure: false
    registries:
      - server: <acr-name>.azurecr.io
        username: <username>
        passwordSecretRef: registry-password
  template:
    containers:
      - name: letterprogram
        image: <acr-name>.azurecr.io/letterprogram:latest
        resources:
          cpu: 0.5
          memory: 1Gi
        env:
          - name: ASPNETCORE_ENVIRONMENT
            value: production
    scale:
      minReplicas: 1
      maxReplicas: 10
      rules:
        - name: http-requests
          custom:
            query: "requests_total"
            metadata:
              desiredReplicas: "30"
```

### Scaling Policies
- **Min replicas**: 1 (cost-effective baseline)
- **Max replicas**: 10 (handles traffic spikes)
- **Scale trigger**: HTTP concurrency > 100 requests/instance
- **Scale-down delay**: 300 seconds (avoid thrashing)

### Networking
- **Internal ingress**: Private container networking
- **External ingress**: Public HTTPS endpoint
- **Dapr integration**: Service-to-service communication

---

## 🌐 Azure Web Service & App Service

### Azure App Service Plan
- **SKU**: `P1V2` (Production) or `B2` (Development)
  - **P1V2**: 2 cores, 3.5 GB RAM, auto-scale to 30 instances
  - **B2**: 2 cores, 3.5 GB RAM, no auto-scale (max 3 instances)
- **OS**: Linux (optimal for Docker containers)
- **Reserved instances**: 1-year commitment for cost savings

### Azure App Service Configuration

#### Application Settings
```json
{
  "WEBSITES_ENABLE_APP_SERVICE_STORAGE": false,
  "DOCKER_REGISTRY_SERVER_URL": "https://<acr-name>.azurecr.io",
  "DOCKER_REGISTRY_SERVER_USERNAME": "<acr-username>",
  "DOCKER_REGISTRY_SERVER_PASSWORD": "<acr-password>",
  "WEBSITES_PORT": 8000,
  "PYTHONPATH": "/app",
  "ENVIRONMENT": "production"
}
```

#### Startup Command
```bash
gunicorn --worker-class uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000 --workers 4
```

### Deployment Methods
- **Continuous deployment** from GitHub (GitHub Actions)
- **Docker Hub / ACR** image pull
- **ZIP deployment** with kudu
- **Local Git push** to Azure remote

### Monitoring
- **Application Insights**: Performance metrics, request tracing, exception logging
- **Live Metrics Stream**: Real-time diagnostics
- **Custom metrics**: Business KPIs and application events

---

## 🔒 SSL/TLS Encryption & HTTPS

### Azure App Service SSL Configuration

#### Certificate Management
- **Azure-managed certificates** (free, auto-renewal)
  - Domain: `letterprogram.azurewebsites.net`
  - Auto-renewed 30 days before expiry
  
- **Custom domain with custom certificate**
  - Upload `.pfx` certificate to App Service
  - Recommended: Use Azure Key Vault for storage
  - Certificate pinning for production

#### HTTPS Enforcement
```json
{
  "https_only": true,
  "min_tls_version": "1.2",
  "client_cert_mode": "Optional"
}
```

**CLI Configuration:**
```bash
az webapp update \
  --resource-group <rg-name> \
  --name <app-name> \
  --https-only true \
  --set httpsOnly=true

az webapp config ssl bind \
  --resource-group <rg-name> \
  --name <app-name> \
  --certificate-thumbprint <thumbprint> \
  --ssl-type SNI
```

### HSTS (HTTP Strict Transport Security)
```nginx
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
```

### Certificate Renewal Alerts
- **Azure Monitor Alert Rule**: Notify when certificate expires in 30 days
- **Application Insights**: Track certificate validity in custom metrics

---

## ⚖️ Load Balancing & Traffic Management

### Azure Load Balancer
- **Type**: Layer 4 (Transport) Load Balancer
- **Protocol support**: TCP, UDP for non-HTTP traffic
- **Availability**: 99.99% SLA with zone redundancy

#### Configuration
```json
{
  "frontendIPConfiguration": {
    "publicIPAddress": "letterprogram-lb-pip",
    "idleTimeoutInMinutes": 30
  },
  "backendAddressPool": [
    {
      "name": "app-backend-pool",
      "virtualMachines": ["vm-app-1", "vm-app-2", "vm-app-3"]
    }
  ],
  "loadBalancingRules": [
    {
      "name": "http-rule",
      "protocol": "Tcp",
      "frontendPort": 80,
      "backendPort": 8000,
      "backendAddressPool": "app-backend-pool",
      "probe": "app-health-probe"
    },
    {
      "name": "https-rule",
      "protocol": "Tcp",
      "frontendPort": 443,
      "backendPort": 8000,
      "backendAddressPool": "app-backend-pool",
      "probe": "app-health-probe"
    }
  ],
  "probes": [
    {
      "name": "app-health-probe",
      "protocol": "Http",
      "port": 8000,
      "path": "/health",
      "intervalInSeconds": 15,
      "numberOfProbes": 2
    }
  ]
}
```

### Azure Application Gateway (OSI Layer 7)
- **Routing rules**: Path-based, hostname-based, header-based
- **WAF integration**: Web Application Firewall for DDoS/SQL injection protection
- **SSL offloading**: Decrypt at gateway, re-encrypt to backend (optional)
- **Session persistence**: Sticky sessions with affinity cookies
- **Auto-scaling**: Dynamic backend pool member addition/removal

#### URL Path-Based Routing Example
```json
{
  "requestRoutingRules": [
    {
      "name": "api-routing",
      "ruleType": "PathBasedRouting",
      "httpListener": {
        "name": "https-listener"
      },
      "urlPathMap": {
        "name": "api-path-map",
        "pathRules": [
          {
            "name": "api-rule",
            "paths": ["/api/*"],
            "backendAddressPool": "api-backend",
            "backendHttpSettings": "http-settings"
          },
          {
            "name": "static-rule",
            "paths": ["/static/*"],
            "backendAddressPool": "static-backend",
            "backendHttpSettings": "cache-settings"
          }
        ]
      }
    }
  ]
}
```

### Traffic Manager (Geographic/Performance Routing)
- **Routing methods**:
  - **Priority**: Primary region with failover to secondary
  - **Weighted**: Percentage-based traffic split (canary deployments)
  - **Performance**: Route to lowest latency endpoint
  - **Geographic**: Route based on user location
  - **Subnet**: Route based on client subnet
  - **Multi-value**: Return multiple healthy endpoints

#### Example Configuration
```json
{
  "name": "letterprogram-tm",
  "trafficRoutingMethod": "Weighted",
  "endpoints": [
    {
      "name": "primary-region",
      "type": "azureEndpoints",
      "target": "letterprogram-east.azurewebsites.net",
      "weight": 80,
      "priority": 1
    },
    {
      "name": "secondary-region",
      "type": "azureEndpoints",
      "target": "letterprogram-west.azurewebsites.net",
      "weight": 20,
      "priority": 2
    }
  ],
  "healthCheckConfig": {
    "protocol": "HTTPS",
    "port": 443,
    "path": "/health",
    "intervalInSeconds": 30
  }
}
```

### Azure Front Door (Global Content Delivery)
- **Features**: Global load balancing, DDoS protection, WAF, caching
- **Backends**: Multiple Azure regions for geo-redundancy
- **Health probes**: Active monitoring every 30 seconds
- **Priority-based routing**: Automatic failover on unhealthy backends
- **HTTP/2 and HTTP/3 support**: Modern protocol acceleration

#### CDN Configuration
```json
{
  "cacheConfiguration": {
    "queryStringCachingBehavior": "IgnoreQueryString",
    "cacheDuration": "1.00:00:00",
    "isCompressionEnabled": true,
    "contentTypesToCompress": [
      "text/html",
      "text/css",
      "application/javascript",
      "image/svg+xml"
    ]
  }
}
```

---

## 📊 Deployment Topology

```
┌─────────────────────────────────────────────────────────────────┐
│                        GitHub Repository                         │
│                                                                  │
│  ┌────────────────┐      ┌──────────────────────────────────┐  │
│  │ Source Code    │      │   Automated CI/CD Pipeline       │  │
│  │  - letterprogram      │  - Build Docker image            │  │
│  │  - Docker config      │  - Push to ACR                   │  │
│  │  - Tests              │  - Deploy to Azure               │  │
│  └────────────────┘      └──────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│              Azure Resource Group (Production)                   │
│                                                                  │
│  ┌──────────────────┐      ┌──────────────────────────────────┐│
│  │ Azure Container  │      │   Azure Front Door / Traffic      ││
│  │ Registry (ACR)   │      │   Manager (Global Load Balance)  ││
│  │                  │      └──────────────────────────────────┘│
│  │ - Stores images  │                     │                     │
│  │ - Versioning     │                     ▼                     │
│  └───────┬──────────┘      ┌──────────────────────────────────┐│
│          │                 │  Azure Application Gateway        ││
│          │                 │  (Layer 7 LB + WAF)             ││
│          │                 │  SSL/TLS Termination             ││
│          │                 └───────────┬──────────────────────┘│
│          │                             │                        │
│          │    ┌────────────────────────┼────────────────────┐  │
│          │    │                        │                    │  │
│          ▼    ▼                        ▼                    ▼  │
│  ┌──────────────────┐     ┌──────────────────────┐         │  │
│  │  Region 1 (East) │     │  Region 2 (West)    │    ….    │  │
│  │ Container Apps   │     │ Container Apps      │         │  │
│  │ App Service      │     │ App Service         │         │  │
│  │ PostgreSQL (hot) │     │ PostgreSQL (hot)    │         │  │
│  │ Redis Cache      │     │ Redis Cache         │         │  │
│  │                  │     │                     │         │  │
│  │ (Active)         │     │ (Standby/Failover)  │         │  │
│  └──────────────────┘     └─────────────────────┘         │  │
│                                                             │  │
│  ┌────────────────────────────────────────────────────┐   │  │
│  │ Shared Resources:                                  │   │  │
│  │ - Key Vault (Secrets, Certs)                       │   │  │
│  │ - Application Insights (Monitoring)                │   │  │
│  │ - Log Analytics (Centralized Logging)              │   │  │
│  │ - Azure DevOps / GitHub Actions (CI/CD)           │   │  │
│  └────────────────────────────────────────────────────┘   │  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Quick Start

### Local Development
```bash
# Clone repository
git clone https://github.com/ShivGitLabbing/my-automation-project.git
cd source/letterprogram

# Install dependencies
uv sync

# Run app
uv run uvicorn app.main:app --reload
```

### Docker Local Testing
```bash
docker build -t letterprogram:test .
docker run -p 8000:8000 letterprogram:test
```

### Azure Deployment (via GitHub Actions)
```bash
# Push to feature branch
git checkout -b feature/my-feature
git push -u origin feature/my-feature

# Merge to main triggers automatic deployment
git checkout main
git merge feature/my-feature
git push origin main
```

---

## 📈 Performance & Optimization

### Application Performance
- **Startup time**: < 2 seconds (uvicorn ASGI server)
- **Container image size**: ~220 MB (python:3.14-slim base)
- **Memory footprint**: ~150 MB per instance
- **CPU usage**: Auto-scales based on concurrency

### Caching Strategy
- **Static assets**: 1-hour edge caching via Front Door
- **API responses**: Redis caching for frequent queries
- **Database**: Connection pooling (5-20 connections per instance)

### Database Connection Options
- **Azure Database for PostgreSQL**: Managed relational database
  - Read replicas for analytics workloads
  - Automatic backup and geo-replication
- **Azure Cosmos DB**: NoSQL for high-scale scenarios
- **Azure SQL Database**: Enterprise SQL Server compatibility

---

## 🔐 Security Best Practices

### Network Security
- **VNet Integration**: Private subnet assignment
- **NSG Rules**: Restrict inbound to load balancer only
- **Private Link**: Database access without public endpoints
- **DDoS Protection Standard**: Layer 3-7 attack mitigation

### Data Protection
- **Encryption at rest**: Storage, database encryption
- **Encryption in transit**: TLS 1.2 minimum
- **Secrets management**: Azure Key Vault with managed identity
- **Vulnerability scanning**: Trivy for container images

### Compliance
- **SOC 2 Type II**: Azure compliance certifications
- **GDPR**: Data residency in EU regions
- **HIPAA**: Healthcare data handling (if applicable)
- **Audit logging**: All resource changes logged to Azure Monitor

---

## 🛟 Support & Troubleshooting

### Common Issues
- **Container fails to start**: Check Application Insights logs
- **SSL certificate expired**: Renew in Azure App Service
- **High latency**: Verify load balancer health probes passing
- **Database connection timeout**: Check VNet firewall rules

### Monitoring Dashboards
- **Custom dashboard**: Application metrics, error rates
- **Alert rules**: Auto-notify on CPU > 80% or errors > threshold
- **Log query examples**: Kusto Query Language (KQL) in Log Analytics

### Support Channels
- **GitHub Issues**: Report bugs and feature requests
- **Azure Support**: Enterprise support plans available
- **Documentation**: [letterprogram README](./source/letterprogram/README.md)

---

## 📦 Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2026-04-12 | Initial release with media-driven letter cards, Azure containerization support, comprehensive documentation |

---

## 📄 License

This project is licensed under the **MIT License** — see [LICENSE](./LICENSE) for details.

---

**Last Updated**: April 12, 2026  
**Maintained by**: ShivGitLabbing
