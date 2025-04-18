This project consists of two web applications built using Flask and Django, containerized with Docker and orchestrated using Docker Compose.

The Flask application provides a simple interface with two routes: the homepage displays a "Hello, World!" message, and a second route contains a form that takes the user’s name and age, returning a personalized greeting. Basic error handling is implemented to catch missing or invalid inputs.

The Django application is a vehicle inventory system that allows users to view a list of cars and bikes on the homepage and submit new entries through a form. Additionally, Django’s built-in admin panel is enabled and configured, allowing admins to easily manage the database entries via a web interface.
You can log into the admin panel using the superuser credentials:

Username: admin

Password: admin

Both applications are containerized using individual Dockerfiles and managed with a single docker-compose.yml file. When docker-compose up is run, it spins up both services simultaneously, making the Flask app available at http://localhost:5000 and the Django app at http://localhost:8000. The Django admin panel is accessible at http://localhost:8000/admin.

This setup provides a clean, reproducible development environment—perfect for learning and deploying multi-service web applications.

