# Contributing to devex-sample

Thank you for your interest in contributing! This document explains how to contribute to the project.

## Getting Started

1. **Fork** the repository
2. **Clone** your fork: `git clone https://github.com/YOUR_USERNAME/devex-sample.git`
3. **Create** a feature branch: `git checkout -b feature/your-feature-name`

## Development Setup

```bash
# Install dependencies
make install

# Start the service
make dev

# Run tests
make test

# Check code quality
make lint
```

## Making Changes

1. **Write clear commit messages** following conventional commits:
   ```
   feat: add new endpoint
   fix: resolve timeout issue
   docs: update README
   test: add edge case tests
   ```

2. **Ensure code quality:**
   ```bash
   make format    # Auto-format code
   make lint      # Check for issues
   ```

3. **Write tests** for new features:
   - Add tests to `tests/test_app.py`
   - Aim for >85% coverage
   - Test happy paths and error cases

4. **Test everything locally:**
   ```bash
   make ci-check  # Run all checks
   ```

## Submitting Changes

1. **Push** your branch: `git push origin feature/your-feature-name`
2. **Create** a Pull Request with a clear description
3. **Link** related issues: `Fixes #123`
4. **Wait** for CI checks to pass
5. **Respond** to review feedback

## Code Standards

### Python Style

- **Line length**: Max 120 characters
- **Formatter**: Black
- **Linter**: Flake8
- **Import sorting**: isort (black profile)

### Testing

- **Framework**: pytest
- **Coverage**: Aim for >85%
- **Location**: `tests/` directory
- **Pattern**: `test_*.py` or `*_test.py`

Example:
```python
def test_endpoint_returns_200(client):
    """Test that endpoint returns 200 status."""
    response = client.get('/')
    assert response.status_code == 200
```

### Documentation

- **Docstrings**: Module, function, and class docstrings required
- **Comments**: Explain "why", not "what"
- **README**: Update if adding features

## Review Process

1. **Automated Checks**
   - Linting (black, flake8, isort)
   - Unit tests
   - Coverage reports
   - Security scanning (bandit, safety)

2. **Code Review**
   - At least one approval required
   - Maintainers may suggest improvements
   - CI must pass before merge

3. **Merge**
   - Squash commits (recommended)
   - Delete feature branch
   - Auto-generate docs (on main)

## Reporting Issues

### Bug Report

Include:
- ✅ What did you do?
- ✅ What did you expect?
- ✅ What actually happened?
- ✅ Steps to reproduce
- ✅ Environment (OS, Python version, Docker?)

### Feature Request

Include:
- ✅ Motivation/use case
- ✅ Proposed solution
- ✅ Alternative approaches considered

## Running Checks Locally

```bash
# All CI checks
make ci-check

# Individual checks
make lint          # Code quality
make test          # Unit tests
make check-deps    # Vulnerabilities
make docs          # Generate documentation
```

## Useful Commands

```bash
make help          # Show all commands
make dev           # Start service
make test          # Run tests
make format        # Auto-fix code
make clean         # Clean up
docker compose ps  # Show containers
make logs          # View service logs
```

## Documentation

- **API Docs**: See `docs/SDD.md`
- **Setup**: See `README.md`
- **Architecture**: See `README.md` → Architecture section

## Questions?

- Open an issue for questions
- Check existing issues first
- Include context and examples

---

## Development Workflow Example

```bash
# 1. Create feature branch
git checkout -b feature/add-timeout-config

# 2. Make changes
# ... edit files ...

# 3. Format code
make format

# 4. Run tests
make test

# 5. Check quality
make lint

# 6. Run all CI checks
make ci-check

# 7. Commit
git commit -m "feat: make external API timeout configurable"

# 8. Push
git push origin feature/add-timeout-config

# 9. Create PR on GitHub
# ... fill in description ...
# ... wait for reviews ...

# 10. After approval, merge via GitHub UI
```

## Thank You!

Your contributions help make this project better. We appreciate your effort! 🎉

---

For more info, see [README.md](README.md)
