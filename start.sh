cd frontend
npm install  
npm run dev


cd ..
pip install -r requirements.txt
gunicorn backend.app:app