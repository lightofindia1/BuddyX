# Commands

## Database

### 1. Initialize Alembic (first time)
```sh
cd apps/backend
alembic init alembic
```

### 2. Create a new migration
```sh
alembic revision --autogenerate -m "<migration message>"
```

### 3. Apply all migrations
```sh
alembic upgrade head
```

### 4. Revert last migration in database
```sh
alembic downgrade -1
```

### 5. Reset all migrations (development only)
```sh
cd apps/backend/alembic/versions
rm *  # or del * on Windows
cd ../..
rm buddyx.db  # or del buddyx.db on Windows
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

### 7. Create Default Admin User
```sh
cd apps/backend
PYTHONPATH=.
python app/db/init_db.py
```

---

## Backend

### 1. Setup Virtual Environment
```sh
cd apps/backend
python -m venv venv
```

### 2. Activate Virtual Environment
```sh
# Windows:
venv\Scripts\activate
# Mac/Linux:
# source venv/bin/activate
```

### 3. Install Requirements
```sh
pip install -r requirements.txt
```

### 4. Start Backend APIs
```sh
uvicorn main:app --reload
```

---

## Frontend (Web)

### 1. Install packages
```sh
cd apps/web
npm install
```

### 2. Start Frontend Dev Server
```sh
npm run dev
```

---

## Run Both Frontend and Backend Together

### (Optional) Using concurrently (requires npm install -g concurrently)
```sh
npx concurrently "cd apps/backend && venv\Scripts\activate && uvicorn main:app --reload" "cd apps/web && npm run dev"
```

---

## Notes
- Set `NEXT_PUBLIC_API_URL` in `apps/web/.env.local` to your backend URL (e.g., http://localhost:8000)
- For mobile/desktop, see respective README or scripts.
