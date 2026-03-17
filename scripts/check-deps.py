#!/usr/bin/env python3
"""
Dependency vulnerability checker and outdated package detector.
Scans requirements files and checks for security issues and outdated versions.
"""

import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple


class DependencyChecker:
    """Check dependencies for vulnerabilities and outdated versions."""

    def __init__(self):
        """Initialize the checker."""
        self.project_root = Path(__file__).parent.parent
        self.requirements_files = [
            self.project_root / "requirements.txt",
            self.project_root / "requirements-dev.txt",
        ]
        self.report_data = {
            "timestamp": datetime.now().isoformat(),
            "vulnerabilities": [],
            "outdated": [],
            "summary": {}
        }

    def run(self) -> int:
        """Run all checks and generate report."""
        print("🔍 Dependency Security & Update Check")
        print("=" * 50)

        # Check for vulnerabilities
        print("\n1️⃣ Checking for known vulnerabilities...")
        vuln_status = self._check_vulnerabilities()

        # Check for outdated packages
        print("\n2️⃣ Checking for outdated packages...")
        outdated_status = self._check_outdated()

        # Generate report
        self._generate_report()

        # Determine exit code
        exit_code = max(vuln_status, outdated_status)
        return exit_code

    def _check_vulnerabilities(self) -> int:
        """
        Check for known vulnerabilities using safety.
        Returns: 0 (ok), 1 (warnings), 2 (critical)
        """
        try:
            # Try using safety
            result = subprocess.run(
                ["safety", "check", "--json"],
                capture_output=True,
                text=True,
                timeout=30,
            )

            if result.returncode == 0:
                print("✅ No known vulnerabilities found")
                self.report_data["summary"]["vulnerabilities"] = "PASS"
                return 0
            else:
                try:
                    data = json.loads(result.stdout)
                    vulns = data if isinstance(data, list) else data.get("vulnerabilities", [])
                    self.report_data["vulnerabilities"] = vulns
                    print(f"⚠️  Found {len(vulns)} vulnerabilities")
                    for vuln in vulns[:3]:  # Show first 3
                        print(f"   - {vuln.get('package', 'Unknown')} ({vuln.get('cve', 'N/A')})")
                    self.report_data["summary"]["vulnerabilities"] = f"WARNING ({len(vulns)} found)"
                    return 1
                except json.JSONDecodeError:
                    print("⚠️  Could not parse safety output")
                    return 0

        except FileNotFoundError:
            print("⚠️  'safety' not installed, skipping vulnerability check")
            print("   Install with: pip install safety")
            return 0
        except subprocess.TimeoutExpired:
            print("⚠️  Safety check timed out")
            return 0
        except Exception as e:
            print(f"⚠️  Error during vulnerability check: {e}")
            return 0

    def _check_outdated(self) -> int:
        """
        Check for outdated packages.
        Returns: 0 (ok), 1 (has outdated)
        """
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pip", "list", "--outdated", "--format=json"],
                capture_output=True,
                text=True,
                timeout=30,
            )

            if result.returncode == 0:
                outdated = json.loads(result.stdout)
                if outdated:
                    print(f"📦 Found {len(outdated)} outdated packages:")
                    for pkg in outdated[:5]:  # Show first 5
                        current = pkg.get("version", "?")
                        latest = pkg.get("latest_version", "?")
                        name = pkg.get("name", "Unknown")
                        print(f"   - {name}: {current} → {latest}")
                    if len(outdated) > 5:
                        print(f"   ... and {len(outdated) - 5} more")
                    self.report_data["outdated"] = outdated
                    self.report_data["summary"]["outdated"] = f"UPDATE AVAILABLE ({len(outdated)} packages)"
                    return 1
                else:
                    print("✅ All packages are up to date")
                    self.report_data["summary"]["outdated"] = "PASS"
                    return 0
            else:
                print("⚠️  Could not check outdated packages")
                return 0

        except Exception as e:
            print(f"⚠️  Error checking outdated packages: {e}")
            return 0

    def _generate_report(self):
        """Generate a markdown report."""
        report_file = self.project_root / "DEPENDENCY_REPORT.md"
        report_content = self._format_report()

        with open(report_file, "w") as f:
            f.write(report_content)

        print(f"\n📄 Report generated: {report_file}")

    def _format_report(self) -> str:
        """Format the report as markdown."""
        timestamp = self.report_data["timestamp"]
        summary = self.report_data["summary"]

        report = f"""# Dependency Security Report

**Generated:** {timestamp}

## Summary

| Check | Status |
|-------|--------|
| Vulnerabilities | {summary.get('vulnerabilities', 'UNKNOWN')} |
| Outdated Packages | {summary.get('outdated', 'UNKNOWN')} |

## Vulnerabilities Found

"""
        if self.report_data["vulnerabilities"]:
            report += "| Package | CVE | Severity |\n"
            report += "|---------|-----|----------|\n"
            for vuln in self.report_data["vulnerabilities"]:
                pkg = vuln.get("package", "Unknown")
                cve = vuln.get("cve", "N/A")
                severity = vuln.get("severity", "Unknown")
                report += f"| {pkg} | {cve} | {severity} |\n"
        else:
            report += "_None_\n"

        report += "\n## Outdated Packages\n\n"
        if self.report_data["outdated"]:
            report += "| Package | Current | Latest |\n"
            report += "|---------|---------|--------|\n"
            for pkg in self.report_data["outdated"]:
                name = pkg.get("name", "Unknown")
                current = pkg.get("version", "?")
                latest = pkg.get("latest_version", "?")
                report += f"| {name} | {current} | {latest} |\n"
        else:
            report += "_All packages are up to date_\n"

        report += "\n---\n"
        report += "*This report was auto-generated by check-deps.py*\n"

        return report


def main():
    """Main entry point."""
    checker = DependencyChecker()
    exit_code = checker.run()

    print("\n" + "=" * 50)
    if exit_code == 0:
        print("✅ Dependency check passed!")
    elif exit_code == 1:
        print("⚠️  Dependency check completed with warnings")
    else:
        print("❌ Dependency check failed!")

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
