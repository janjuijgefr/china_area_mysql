# main - Dockerfile for china_area_mysql
FROM node:18-alpine AS builder

WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM node:18-alpine AS runtime
WORKDIR /app

COPY --from=builder /app/node_modules ./node_modules
COPY . .

RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001

USER nextjs

EXPOSE 3000
ENV PORT 3000
ENV NODE_ENV production

CMD ["node", "index.js"]

# PR Merge: 2025-10-20 - enhancement/merge-5179

# PR Merge: 2025-10-20 - refactor/merge-4091

# PR Merge: 2025-10-20 - feature/merge-5710

# PR Update: 2025-10-20 - feature/update-5120
