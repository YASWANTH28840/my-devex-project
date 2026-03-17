#!/usr/bin/env python3
"""
AI-based documentation generator using Claude API.
Generates/updates System Design Document (SDD.md) based on code analysis.
"""

import os
import sys
from pathlib import Path
from datetime import datetime


def get_api_key() -> str | None:
    """Get API key from environment."""
    return os.getenv("ANTHROPIC_API_KEY")


def read_app_code() -> str:
    """Read the application code."""
    app_file = Path(__file__).parent.parent / "app.py"
    return app_file.read_text()


def read_existing_sdd() -> str | None:
    """Read existing SDD if it exists."""
    sdd_file = Path(__file__).parent.parent / "docs" / "SDD.md"
    if sdd_file.exists():
        return sdd_file.read_text()
    return None


def generate_mock_sdd() -> str:
    """Generate mock SDD when API key is not available."""
    app_code = read_app_code()
    return f"""# System Design Document (SDD)
## devex-sample

**Generated:** {datetime.now().isoformat()}
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
{{
  "service": "devex-sample",
  "status": "ok"
}}
```

**Status Code:** 200 OK

---

#### 2. GET `/products`

**Purpose:** Fetch products from external API (dummyjson.com)

**Response (Success):**
```json
{{
  "products": [
    {{
      "id": 1,
      "title": "Essence Mascara Lash Parlour",
      "price": 9.99,
      ...
    }}
  ],
  "total": 100,
  "skip": 0,
  "limit": 100
}}
```

**Status Codes:**
- 200 OK - Successfully fetched products
- 502 Bad Gateway - Failed to fetch from external API

**Error Response (502):**
```json
{{
  "error": "Failed to fetch products",
  "details": "Connection timeout"
}}
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

*Last Updated: {datetime.now().isoformat()}*
"""


def generate_sdd_with_ai(api_key: str, app_code: str, existing_sdd: str | None) -> str:
    """Generate SDD using Claude API."""
    try:
        from anthropic import Anthropic
    except ImportError:
        print("❌ anthropic library not found. Install with: pip install anthropic")
        return generate_mock_sdd()

    try:
        client = Anthropic()

        # Prepare the prompt
        context = f"""You are a technical documentation expert.

I need you to generate or update a System Design Document (SDD) for a Flask REST service.

## Current Application Code:

```python
{app_code}
```

{"## Existing SDD (update if needed):" + existing_sdd if existing_sdd else ""}

## Requirements for the SDD:

1. **Overview**: Brief description of the service
2. **Endpoints**: Document all API endpoints with:
   - HTTP method and path
   - Purpose
   - Request/response examples
   - Status codes
   - Error handling

3. **Architecture**: ASCII diagram showing service components and dependencies
4. **Dependencies**: List all external services and libraries
5. **Error Handling**: How errors are handled
6. **Security Considerations**: Security features and recommendations
7. **Deployment**: How to deploy the service
8. **Testing**: Testing approach and coverage
9. **Development Workflow**: How to work with the code

## Output Format:

Generate the response as valid Markdown that can be used as a .md file.
Include the current timestamp at the top.
Use clear headings and sections.
Include code examples where relevant.
"""

        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=4096,
            messages=[
                {
                    "role": "user",
                    "content": context
                }
            ]
        )

        sdd_content = message.content[0].text
        return sdd_content

    except Exception as e:
        print(f"⚠️  Error calling Claude API: {e}")
        print("Falling back to mock SDD generation...")
        return generate_mock_sdd()


def save_sdd(content: str) -> Path:
    """Save SDD to file."""
    docs_dir = Path(__file__).parent.parent / "docs"
    docs_dir.mkdir(exist_ok=True)

    sdd_file = docs_dir / "SDD.md"
    sdd_file.write_text(content, encoding="utf-8")

    return sdd_file


def main():
    """Main entry point."""
    print("📝 Generating System Design Document...")
    print("=" * 50)

    api_key = get_api_key()

    if not api_key:
        print("⚠️  ANTHROPIC_API_KEY not set")
        print("   Generating mock SDD (no AI enhancement)")
        sdd_content = generate_mock_sdd()
    else:
        print("✅ API key found, generating with Claude...")
        app_code = read_app_code()
        existing_sdd = read_existing_sdd()
        sdd_content = generate_sdd_with_ai(api_key, app_code, existing_sdd)

    # Save the SDD
    sdd_file = save_sdd(sdd_content)

    print(f"\n✅ SDD generated successfully!")
    print(f"   Location: {sdd_file}")
    print(f"   Size: {len(sdd_content)} characters")

    return 0


if __name__ == "__main__":
    sys.exit(main())
