# NYC Council Dashboard Setup Guide

## Setup Instructions

### Backend Setup (Python 2.x)

1. Navigate to the main directory:

```bash
cd challenge
```

2. Install required Python packages:

```bash
pip install -r requirements.txt
```

3. Run migrations and populate the database:

```bash
python manage.py migrate
python manage.py populate_db
```

4. (Optional) Create a superuser to access the admin panel:

```bash
python manage.py createsuperuser
```

5. Start the Django development server:

```bash
python manage.py runserver
```

### Backend Setup (Python 3.x)

1. Navigate to the main directory:

```bash
cd challenge
```

2. Install required Python packages:

```bash
pip3 install -r requirements.txt
```

3. Run migrations and populate the database:

```bash
python3 manage.py migrate
python3 manage.py populate_db
```

4. (Optional) Create a superuser to access the admin panel:

```bash
python3 manage.py createsuperuser
```

5. Start the Django development server:

```bash
python3 manage.py runserver

### Frontend Setup
1. Navigate to the frontend directory:

```bash
cd challenge/frontend
```

2. Install dependencies:

```bash
npm install
```

3. Set Node options for compatibility with newer Node.js versions:

```bash
# For macOS/Linux
export NODE_OPTIONS=--openssl-legacy-provider

# For Windows Command Prompt
set NODE_OPTIONS=--openssl-legacy-provider

# For Windows PowerShell
$env:NODE_OPTIONS="--openssl-legacy-provider"
```

4. Start the React development server:

```bash
npm start
```

5. The application should now be running at `http://localhost:3000`

## Login Information
* Username: {first_name_initial}{last_name}
* Password: {last_name}-{district_number}

### Example Logins:
* **Margaret Chin (District 1)**
   * Username: `mchin`
   * Password: `chin-1`
* **Fernando Cabrera (District 14)**
   * Username: `fcabrera`
   * Password: `cabrera-14`
* **Inez Barron (District 42)**
   * Username: `ibarron`
   * Password: `barron-42`
* **Justin Brannan (District 43)**
   * Username: `jbrannan`
   * Password: `brannan-43`