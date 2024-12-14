# Django Blog Application
This is a simple Django blog application that allows users to view, create, update, and delete blog posts. The application uses both function-based views (FBV) and class-based views (CBV) for different actions. The application includes templates for listing, viewing, creating, updating, and deleting blog posts.

## Features
    - List Blog: Display a list of all blog posts.
    - Detail Blog: View the details of a specific blog post.
    - Add Blog: Create a new blog post.
    - Update Blog: Edit an existing blog post.
    - Delete Blog: Delete a blog post.


## Views

### Function-Based Views (FBV)
The project contains the following function-based views:
   - list_blog: Displays all blog posts.
   - detail_blog: Displays the details of a single blog post.
   -  add_blog: Allows users to create a new blog post.
   - update_blog: Allows users to edit an existing blog post.
   - delete_blog: Allows users to delete a blog post.

### Class-Based Views (CBV)
The project also uses class-based views for the following actions:
   -  ListViewBlog: Displays all blog posts (replaces list_blog FBV).
   -  DetailViewBlog: Displays the details of a single blog post (replaces detail_blog FBV).
   -  UpdateViewBlog: Allows users to edit an existing blog post (replaces update_blog FBV).
   -  CreateViewBlog: Allows users to create a new blog post (replaces add_blog FBV).
   -  DeleteViewBlog: Allows users to delete a blog post (replaces delete_blog FBV).