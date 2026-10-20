Run cmd

docker compose up -d --build

npm --prefix frontend run dev -- --host 0.0.0.0


Frontend UI: http://localhost:3000
Backend API & Swagger Docs: http://localhost:8000/docs
Qdrant Vector DB Dashboard: http://localhost:6333/dashboard
PostgreSQL: localhost:5432

# Run backend
docker run -d --name sd-backend -p 8000:8000 system-design-backend:latest
# Run frontend
docker run -d --name sd-frontend -p 3000:80 system-design-frontend:latest


Running Services Status
Service	Container Name	Health / Status	Port / URL
Frontend UI	system_design_frontend	Up (Healthy)	http://localhost:3000
Backend API & Swagger	system_design_backend	Up (Healthy)	http://localhost:8000/docs
PostgreSQL 16	system_design_postgres	Up (Healthy)	localhost:5432
Qdrant Vector DB	system_design_qdrant	Up (Running)	http://localhost:6333/dashboard