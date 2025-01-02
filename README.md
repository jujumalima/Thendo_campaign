# Django Project

This is a Django-based web application designed to manage donations, newsletters, events, and news. The project includes features for subscribing to newsletters, making donations, registering and logging in users, and displaying the latest news and upcoming events.

## Features

- **Newsletter Subscription**: Users can sign up for a newsletter.
- **Donation Management**: Users can donate and view a thank-you message.
- **User Authentication**: Register, log in, and manage user sessions.
- **Home Page**: Displays the latest news and upcoming events.
- **Thank You Pages**: After donation and newsletter signup, users are redirected to a thank you page.

## Installation

To get started with this project, follow the steps below.

### Requirements

- Python 3.12 or later
- Django 3.x or later


### Setup

1. Clone the repository:
    ```
    git clone https://github.com/jujumalima/Thendo_campaign
    cd Thendo_campaign
    ```

2. Create a virtual environment:
    ```
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Apply database migrations:
    ```
    python manage.py migrate
    ```

5. Run the development server:
    ```
    python manage.py runserver
    ```

6. The application should now be running on `http://127.0.0.1:8000/`.

## Usage

- **Homepage**: Displays the latest news and upcoming events.
- **Register**: Create an account.
- **Login**: Log into your account.
- **Donate**: Make a donation through the donate page.
- **Newsletter Signup**: Subscribe to the newsletter.
- **Thank You Pages**: After donating or subscribing, you'll be redirected to a thank-you page.

.


