FROM python:3 
WORKDIR /usr/src/app

## Install packages 
COPY requirements.txt ./ 
RUN pip install -r requirements.txt
COPY sso .
EXPOSE 8000

# CMD ["python", "./setup.py", "runserver", "--host=0.0.0.0", "-p 8080"] 
CMD ["gunicorn", "--workers=3" ,"--bind", "0.0.0.0:8000", "sso.wsgi:application"]