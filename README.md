# Project4: Network

### Social Network

In this project, our aim is to develop a social networking website similar to Twitter, where users can create posts and engage with content by liking it

#### Description

Using Python, JavaScript, HTML, and CSS, we have to complete the implementation of a social network that allows users to make posts, follow other users, and "like" posts. we must comply with the following requirements:

#### Specifications

- **New Post**: Logged-in users should be able to write a new text-based post by filling out a text area and then clicking a button to submit the post.

The screenshot at the top of this specification shows the "New Post" box at the top of the "All Posts" page. You can choose to do the same, or you can make the "New Post" feature a separate page.

- **All Posts**: The "All Posts" link in the navigation bar should take the user to a page where they can view all posts from all users, with the most recent posts first.

Each post should include the author's username, the content of the post itself, the date and time the post was made, and the number of "likes" the post has (this will be 0 for all posts until you implement the ability to "like" a post later).

- **Profile Page**:  Clicking on a username should load that user's profile page. This page should:

Display the number of followers the user has, as well as the number of people the user is following.

Show all posts by that user, in reverse chronological order.

For any other logged-in user, this page should also display a "Follow" or "Unfollow" button that allows the current user to toggle whether they are following this user's posts or not. Note that this only applies to any other user: a user should not be able to follow themselves.

- **Following**: The "Following" link in the navigation bar should take the user to a page where they see all posts made by users they are currently following.

This page should behave the same way as the "All Posts" page but with a more limited set of posts.

This page should only be available to logged-in users.

- **Pagination**: On any page displaying posts, only 10 should be shown on one page. If there are more than ten posts, a "Next" button should appear to take the user to the next page of posts (which should be older than the current page of posts). If not on the first page, a "Previous" button should also appear to take the user to the previous page of posts.

- **Edit Post**:Users should be able to click on an "Edit" button or link on any of their own posts to edit that post.

When a user clicks "Edit" for one of their own posts, the content of their post should be replaced with a text area where the user can edit the content of their post.

Then, the user should be able to "Save" the edited post. Using JavaScript, you should be able to achieve this without requiring a full page reload.

For security, ensure that your application is designed in such a way that it is not possible for a user, through any means, to edit another user's posts.


- **"Like" and "Unlike"**:Users should be able to click on a button or link on any post to toggle whether they "like" that post or not.

Using JavaScript, you should asynchronously inform the server to update the "like" count (such as through a fetch call) and then update the like count of the post displayed on the page, without requiring a full page reload.

## Developed Using:

- Django
- Python
- HTML
- CSS
- Jinja
- SQL
- Bootstrap
- JavaScript
- Mail API

## Run Locally

### Clone the project

```bash
git clone https://github.com/Alex000127/cs50w-project4.git
```

### Navigate to the project directory

```bash
cd cs50w-project4
```
### Set up the virtual environment (optional)

```bash
pip install virtualenv
```

```bash
python -m venv env
```
### or
```bash
virtualenv env
```
### activate the virtual environment
```bash
.\env\Scripts\activate
```



### Install dependencies

```bash
python -m pip install -r requirements.txt
```


### Apply migrations

```bash
python manage.py migrate
```

### Start the server

```bash
python manage.py runserver
```

## Author

- [Alexandra Salazar](https://github.com/Alex000127)
