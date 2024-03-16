FROM python:3.10

# Set environment variables
ENV PYTHONBUFFERED 1
ENV PYTHONWRITEBODYCODE 1
ENV DEBUG=True

# Set working direcotry in container
WORKDIR /app

# copy dependencies file in working directory
COPY requirements.txt /app/

# insatll dependencies
RUN pip install -r requirements.txt

# copy entire project in working directory
COPY . /app/

COPY .env /app/

#set port
EXPOSE 8000

#command to run application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]