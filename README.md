# How to run

- To run this project, you will have to run the flask backend to send the data to the endpoint created (actually --> http://localhost:3000)
- To run the backend, first download the requirements (creating a venv is recommended)
  ```cmd
  pip install -r requirements.txt
  ```
- After that, run:
  ```python
  python3 app.py
  ```

- Now, run the Vue frontend (actually --> http://localhost:5173/). To run, first install de npm modules:
  ```cmd
  cd frontend
  npm install primeicons primevue @primevue/themes
  npm run dev
  ```

- Now the application must works