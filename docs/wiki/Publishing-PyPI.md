# PyPI Trusted Publishing Standard Operating Procedure (SOP)

This document outlines the standard release procedure for publishing `bhashabid` to the Python Package Index (PyPI) via GitHub Actions Trusted Publishing.

---

## 🔐 1. Prerequisite: Configure Trusted Publisher on PyPI

Bhashabid uses OpenID Connect (OIDC) trusted publishing (`id-token: write`), eliminating the need to store long-lived PyPI API tokens in GitHub Secrets.

Before the first release is triggered:

1. Log in to [pypi.org](https://pypi.org/).
2. Navigate to **Account Settings** -> **Publishing** -> **Add a new publisher**.
3. Fill in the following repository details:
   - **PyPI Project Name**: `bhashabid`
   - **Owner**: `ashik1291`
   - **Repository Name**: `bhashabid`
   - **Workflow name**: `publish_pypi.yml`
   - **Environment name**: *(leave blank or specify `pypi` if using an environment)*
4. Click **Add**.

---

## 🚀 2. Triggering a Release

Once the trusted publisher is registered, triggering a release is fully automated:

### Method A: Automated via GitHub Release Tag
1. Create a release tag on `main`:
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```
2. Navigate to GitHub -> **Releases** -> **Draft a new release**.
3. Select `v1.0.0`, provide the release notes, and click **Publish release**.
4. GitHub Actions will run `.github/workflows/publish_pypi.yml`:
   - Builds binary wheel (`.whl`) and source tarball (`.tar.gz`).
   - Authenticates via OIDC token.
   - Publishes package to PyPI.

### Method B: Manual Workflow Dispatch
1. Go to GitHub -> **Actions** -> **Publish to PyPI**.
2. Click **Run workflow** on the `main` branch.

---

## 📦 3. Verifying the Global Installation

After publication completes:
```bash
pip install --upgrade bhashabid
bhashabid status
bhashabid install-skill
bhashabid install-mcp
```
All packaged assets (`skills/` and `adapters/`) are bundled directly within the distribution wheel (`tools/assets/`), allowing one-command global activation across Cursor, Claude Desktop, and Antigravity.
