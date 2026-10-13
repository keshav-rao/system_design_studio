Run cmd

docker compose up -d --build


Frontend UI: http://localhost:3000
Backend API & Swagger Docs: http://localhost:8000/docs
Qdrant Vector DB Dashboard: http://localhost:6333/dashboard
PostgreSQL: localhost:5432

# Run backend
docker run -d --name sd-backend -p 8000:8000 system-design-backend:latest
# Run frontend
docker run -d --name sd-frontend -p 3000:80 system-design-frontend:latest
