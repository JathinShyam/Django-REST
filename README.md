# Django-REST

## Overview
Django-REST is a comprehensive tutorial and example project for building RESTful APIs using Django and the Django REST framework. This repository provides a step-by-step guide and code samples to help you understand and implement RESTful APIs in your Django projects.


## Key Features


1. **Django REST Framework Setup:** Learn how to set up Django REST framework to enable API development in your Django project.

2. **API View Decorators:** Explore various API view decorators that can be used to enhance your API views.

3. **HTTP Methods (GET, POST, PUT):** Understand how to create API endpoints that support common HTTP methods like GET, POST, and PUT.

4. **Creating Models:** Learn how to define models to represent your data in the database.

5. **Writing Serializers:** Discover the process of creating serializers to transform complex data types (such as Django models) into native Python data types.

6. **CRUD Operations with Serializers:** Implement Create, Read, Update, and Delete (CRUD) operations using serializers.

7. **Validation in Serializers:** Explore how to add validation to ensure data integrity and consistency.

8. **Serializing Foreign Keys:** Learn how to serialize and work with relationships, including foreign keys in Django REST framework.

9. **More About Serializers in DRF:** Dive deeper into serializers, their functionality, and advanced use cases.

10. **APIView Class in DRF:** Understand how to use the APIView class to create custom API views with complete control over the logic.

11. **ModelViewSet in DRF:** Discover the power of ModelViewSet for simplified CRUD operations with minimal code.

12. **Status Codes in DRF:** Explore the various HTTP status codes used in Django REST framework and their meanings.

13. **Token Authentication in DRF:** Learn how to implement token-based authentication for secure API access.

14. **Permissions in DRF:** Explore different permission classes and how to control access to your API endpoints.

15. **Pagination in DRF:** Understand how to implement pagination to handle large datasets efficiently.

16. **Actions in Django Rest Framework:** Learn how to create custom actions in your views for more complex functionality.


## Installation and Usage

1. Clone the repository:
   ```shell
   git clone https://github.com/JathinShyam/Django-REST.git

2. Install dependencies:
   ```shell
   pip install -r requirements.txt

3. Apply database migrations:
   ```shell
   python manage.py migrate

4. Create a superuser for initial login:
   ```shell
   python manage.py createsuperuser

5. Start the development server:
   ```shell
   python manage.py runserver

6. Access the Django-REST via your web browser: http://localhost:8000/

7. Log in using your superuser credentials to access the admin panel.

## Postman Installation

[Postman](https://www.postman.com/) is a valuable tool for testing and documenting RESTful APIs. Follow these steps to install Postman and get started with API testing:

### 1. Download Postman

- Visit the [Postman download page](https://www.postman.com/downloads/) and select the version that matches your operating system (Windows, macOS, or Linux).

### 2. Install Postman

- **Windows:**
  - Once the download is complete, run the installer.
  - Follow the on-screen instructions to complete the installation.

- **macOS:**
  - Open the downloaded DMG file.
  - Drag the Postman app into your Applications folder.

- **Linux:**
  - Depending on your Linux distribution, the installation process may vary. Consult the installation instructions provided on the Postman website for specific Linux distributions.

### 3. Launch Postman

- After installation, you can launch Postman by opening the application from your system's applications or applications menu.

### 4. Sign In or Create an Account

- You will be prompted to sign in or create a Postman account. While you can use Postman without an account, having an account enables you to sync your work and access additional features.

### 5. Get Started

- Postman is now installed and ready to use. You can create collections, define requests, and start testing APIs. To learn more about using Postman, refer to the [official Postman documentation](https://learning.postman.com/docs/getting-started/introduction/).

Now that you have Postman installed, you can use it to interact with the APIs you develop in this project, test endpoints, and make API development even more efficient.

## Credits

We would like to express our gratitude to [Scalar Academy](https://www.scalaracademy.com/) for their valuable contributions to this project. Scalar Academy offers comprehensive courses and resources on web development and programming, and their guidance has been instrumental in the development of this repository.

We also want to thank the open-source community and the contributors who have made this project possible through their suggestions, bug reports, and code contributions. Your support and collaboration are greatly appreciated.

- [Scalar Academy](https://www.scalaracademy.com/): For providing educational content and resources related to web development and programming.

- Open Source Contributors: A big shout-out to all the developers who have helped make this project better through their contributions.

If you have contributed to this project and your name is not listed, please let us know, and we'll be happy to include your name in the credits.


## Contributions
We welcome contributions! To contribute to this project, please follow our Contributing Guidelines. You can report issues, suggest improvements, and submit pull requests.

