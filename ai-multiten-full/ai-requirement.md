Build a full-stack, multi-tenant AI platform using **Angular 19 + Nx monorepo** with Micro Frontends (Module Federation), **FastAPI + MongoDB** backend, and complete DevOps setup (Docker, Minikube, Helm charts).


**No external AI services, no Azure, no OpenAI-compatible APIs mentioned.** 
The chat endpoint will be a **stub/placeholder** that streams mock responses (text + fake chart data) for demo purposes. Real LLM integration will be added later.


### Two Applications (Angular 19 + Nx)
Create a proper folder structure and then start creating files and coding
1. **Dashboard / Use-Case Portal (MFE Shell / Host)**
  - Nx-hosted Angular 19 standalone app using `@angular-architects/module-federation`
  - Multi-tenant: tenant resolved from subdomain (e.g., `tenant1.app.local`) or JWT claim
  - Clean card/grid UI showing available use-cases
  - Clicking a card navigates to the Chat app with context (tenant_id, use_case_id, user_id, optional preset prompt) passed securely


2. *** Chat Application (MFE Remote + Standalone)**
  - Independent Angular 19 app (Nx)
  - Modern ChatGPT-style interface with rich message rendering:
    - Markdown text, tables, code blocks (syntax highlighting)
    - Dynamic charts/graphs (line, bar, pie, area) using **Chart.js**
  - Works as:
    - Dynamically loaded remote inside the shell
    - Standalone route (`/chat` or `chat.app.local`)
  - Fully multi-tenant: chat history, rate limits, theming isolated per tenant
  - Chat app will get the data from mongodb database


### Tech Stack (100% local/self-hosted)


- **Frontend**: Angular 19 + Nx + Standalone Components + Signals + SCSS + Module Federation
- **Backend**: Python 3.12 + FastAPI + Motor (async MongoDB) + Pydantic v2
- **Database**: MongoDB (single DB with `tenant_id` field + strict middleware + indexes)
- **Auth**: JWT (RS256 preferred), `tenant_id` in claims
- **DevOps**:
 - Python virtual environment (venv) + setup script
 - Multi-stage Dockerfiles
 - `docker-compose.yml` (FastAPI + MongoDB + shell + remote)
 - Helm charts + Minikube-ready manifests
 - Ingress with subdomain routing


### Deliverables (step-by-step)


1. Complete Nx monorepo folder structure (`apps/`, `libs/`, `tools/`)
2. Python virtual environment setup script + `requirements.txt`
3. FastAPI backend with:
  - Tenant middleware (subdomain + JWT validation)
  - **Mock streaming chat endpoint** (`/chat/stream`) that returns realistic fake responses including:
    - Text chunks
    - Chart data (JSON payload for Chart.js)
    - Markdown tables/code
  - Chat history CRUD scoped by `tenant_id` + `user_id` in MongoDB
  - Health & OpenAPI endpoints
4. MongoDB collection schemas + indexes (`tenants`, `users`, `chat_sessions`, `messages`, `use_cases`)
5. Module Federation configs:
  - Shell host `webpack.config.js`
  - Chat remote `webpack.config.js` (exposes chat module)
  - Dynamic loading with fallback
6. Dockerfiles + `docker-compose.yml` for local dev
7. Helm charts (backend Deployment, MongoDB StatefulSet, shell, remote, Ingress)
8. Secure context passing (signed JWT in query param or secure cookie)
9. Optional: Redis for per-tenant rate limiting


### Start by generating:


1. Full Nx monorepo folder structure (Angular 19 + Module Federation ready)
2. Python virtual environment setup script + `requirements.txt`
3. Complete FastAPI project structure with tenant middleware, MongoDB integration, and mock streaming chat endpoint


Use latest best practices, clean architecture, type safety, and production-ready patterns.
