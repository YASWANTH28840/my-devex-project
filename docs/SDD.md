# System Design Document (SDD)
## devex-sample

**Generated:** 2026-03-17T16:15:02.383062
**Status:** Mock Generation (ANTHROPIC_API_KEY not provided)

### Overview

This document describes the architecture and design of the **devex-sample** Flask REST service.

### Service Information

- **Name:** devex-sample
- **Type:** REST API (Flask)
- **Python Version:** 3.11+
- **Port:** 5000

### Endpoints

#### 1. GET `/`

**Purpose:** Health check endpoint

**Response:**
```json
{
  "service": "devex-sample",
  "status": "ok"
}
```

**Status Code:** 200 OK

---

#### 2. GET `/products`

**Purpose:** Fetch products from external API (dummyjson.com)

**Response (Success):**
```json
{
  "products": [
    {
      "id": 1,
      "title": "Essence Mascara Lash Parlour",
      "price": 9.99,
      ...
    }
  ],
  "total": 100,
  "skip": 0,
  "limit": 100
}
```

**Status Codes:**
- 200 OK - Successfully fetched products
- 502 Bad Gateway - Failed to fetch from external API

**Error Response (502):**
```json
{
  "error": "Failed to fetch products",
  "details": "Connection timeout"
}
```

---

### Architecture

```
┌─────────────┐
│   Client    │
└──────┬──────┘
       │ HTTP
       ▼
┌────────────────────┐
│  Flask REST API    │
│  (Port 5000)       │
├────────────────────┤
│  GET /             │  Health check
│  GET /products     │  Proxies to external API
└────────────────────┘
       │
       │ HTTPS (timeout: 10s)
       ▼
┌──────────────────────┐
│ dummyjson.com/api    │
│ (External Service)   │
└──────────────────────┘
```

### Dependencies

**Production:**
- `flask==3.0.0` - Web framework
- `requests==2.31.0` - HTTP client library

**Development:**
- `pytest==7.4.3` - Testing framework
- `black==23.12.1` - Code formatter
- `flake8==6.1.0` - Linter
- `isort==5.13.2` - Import sorting
- `safety==2.3.5` - Vulnerability scanner
- `anthropic==0.7.6` - Claude API client

### Error Handling

The application implements error handling for:

1. **External API Failures**
   - Timeouts (10 second limit)
   - HTTP errors
   - Connection errors
   - All return 502 Bad Gateway with error details

2. **Request Validation**
   - Invalid routes return 404 Not Found
   - Unsupported methods return 405 Method Not Allowed

### Security Considerations

✅ **Implemented:**
- Non-root Docker user
- Health checks with timeout
- Request timeout on external calls (10s)
- Error details sanitized
- No sensitive data logging

⚠️ **Recommendations:**
- Add rate limiting
- Implement authentication/authorization
- Add input validation for query parameters
- Use HTTPS in production
- Implement proper logging with structured output
- Add CORS policy if needed

### Deployment

The service is containerized with:
- **Multi-stage Docker build** for optimized image size
- **Health checks** for container orchestration
- **Non-root user** for security
- **Environment variables** for configuration

### Testing

Run tests with:
```bash
make test
```

Current test coverage:
- Health check endpoint
- Products endpoint (success and error cases)
- Error handling for timeouts and connection errors
- API contract validation

### Code Quality

Automated checks:
```bash
make lint      # Run black, flake8, isort
make format    # Auto-format code
```

### Development Workflow

```bash
make install   # Install dependencies
make dev       # Start service (Docker)
make test      # Run tests
make lint      # Check code quality
make clean     # Clean up
```

---

**Note:** This is a mock SDD generated in absence of Claude API key. For full AI-assisted generation, set `ANTHROPIC_API_KEY` environment variable.

*Last Updated: 2026-03-17T16:15:02.383062*
