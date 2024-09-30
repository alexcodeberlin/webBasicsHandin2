# Flask Web Application with 2 dynamic routes

This is a simple web application built with Flask. The project includes dynamic routes for user profiles and posts, with a basic form for navigating to different user pages.

## Features

- Responsive navigation for mobile devices
- Dynamic routing for:
  - User profiles (`/user/<username>`)
  - Posts (`/post/<post_id>`)
- A user overview page where you can type in a username and be redirected to that user's profile.
- Simple CSS styling 


## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. **Install Flask**
    

3. **Run the Flask app**:
    ```bash
    python app.py
    ```

4. Open a browser and navigate to `http://127.0.0.1:5000/`.

## Usage

- **User Overview**: A form where you can enter a username and get redirected to the corresponding user's profile page.
- **Post Page**: Displays the content of a post based on the post ID. You can type in the id in the link and then it changes on the page.


### Dynamic Routing

- **User Profile**: 
  - Navigate to any user profile by accessing `/user/<username>`.
  - The username is dynamic and changes based on the input provided.
- **Post**:
  - Access any post by navigating to `/post/<post_id>`, where `post_id` is a number.



