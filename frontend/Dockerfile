# Stage 1: Build React frontend
FROM node:20-alpine AS builder

WORKDIR /app

# Copy dependency specifications first for better layer caching
COPY package.json package-lock.json ./

# Install dependencies cleanly
RUN npm ci --prefer-offline --no-audit

# Copy source code and build
COPY . .
RUN npm run build

# Stage 2: Serve with Nginx Alpine
FROM nginx:1.27-alpine

# Copy custom nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy build artifacts from builder stage
COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD wget --quiet --tries=1 --spider http://localhost:80/index.html || exit 1

CMD ["nginx", "-g", "daemon off;"]
