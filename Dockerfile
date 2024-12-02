# Step 1: Use an official Python runtime as a base image
FROM python:3.10-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements.txt inside the container
COPY requirements.txt /app/

# Step 4: Install the Python dependencies
RUN pip install -r requirements.txt

# Step 5: Copy the rest of the Django project files into the container
COPY . /app/

# Step 6: Expose the port that Django will run on (default is 8000)
EXPOSE 8000

# Step 7: Run the Django development server (use "python manage.py runserver")
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]