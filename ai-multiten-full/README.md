# AI Multitenant Fullstack Demo

This workspace contains a scaffold for a multi-tenant AI platform with Angular Nx monorepo and a FastAPI backend.

Quickstart (Windows PowerShell):

```powershell
cd <repo-root>\backend
.\setup_venv.ps1
& .\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --port 8000
```

Docker quickstart:

```powershell
docker-compose up --build
```

Frontend (Nx + Angular) quickstart (run from repository root):

```powershell
# install node deps (already done if you followed earlier steps)
npm install --legacy-peer-deps

# serve the shell (host) on http://localhost:4200
npx nx serve shell --configuration=development

# serve the chat remote on http://localhost:4201
npx nx serve chat --configuration=development
```
