# Wanderlust - Testing


![Wanderlust shown on a variety of screen sizes](documention/images/Wanderlust_blog_site.png)

Visit the deployed site: [wandrelust Site](https://django-wanderlust-96b58b7e2665.herokuapp.com/)

___

# Testing

During the project, I conducted testing for functionality and styling issues after building each section or Function/Model. Corrections or fixes were made before proceeding. 
Throughout development, I utilized Google developer tools to verify proper functionality and to aid in diagnosing unexpected issues.
I thoroughly inspected each page using Google Chrome developer tools and the Firefox inspector tool to ensure responsiveness across various screen sizes and devices. Additionally, I enlisted friends to test the site by signing up, adding, and deleting comments using various devices and platforms (IOS, Android, Mobile, Tablet, etc.), and they reported any encountered issues with functionality or styling.


## CONTENTS

- [AUTOMATED TESTING](#automated-testing)
  - [Manual Testing](#manual-testing)
  - [User](#user)
  - [Bugs](#bugs)
  - [Lighthouse](#lighthouse)
  - [Validation Testing](#validation-testing)
    - [HTML \& CSS](#html--css)
  - [Python Testing](#python-testing)
  

## Manual Testing

*For any failures, a more detailed description is provided below the table.*

ADMIN
| TEST | OUTCOME | PASS/FAIL|
|:---:|:---:|:---:|
| Create Blog Post | The post has been successfully created and is now visible | Pass |
| Edit Blog Post | Post content and category have been successfully updated | Pass |
| Delete User Comments | Comment successfully deleted | Pass |
| Delete Blog Post | Post deleted successfully | Pass |
| Create test posts to verify pagination | Next/Previous Page appears at the bottom of the screen | Pass |
| Like and Unlike a blog post | The admin can not like or unlike a post that they posted | Pass |
| Edit Blog post | updated successfully | pass 
| logout | Logout Successful | Pass |

(*) - While testing the ability to like posts (Hidden from Admin not to be able to like the post that is created by the admin ), I had a problem when editing the title and slug of the post. This was due to the URL not being able to find the original slug of the post (because it had been changed during the edit) to route it after the editing was complete. At this stage, I felt the easiest fix was to remove the ability to edit the post title and slug in the browser, but this functionality is still available via the django admin panel.

## User

| TEST | OUTCOME | PASS/FAIL|
|:---:|:---:|:---:|
| Create Account | successfully created | Pass |
| Login | Login Successful | Pass |
| Logout | Logout Successful | Pass |
| Read Full Blog Post | PostDetail page loaded successfully | Pass |
| Leave a comment below the blog post | Comment Successfully Added| Pass |
| Edit a comment below the blog post | update successfully Added | Pass |
| Delete Comment | Comment Deleted | Pass |
| Filter Posts by category | Posts marked as selected category displayed successfully | Pass |
| Add a blog post | Post a blog succssfully | Pass |
| Like and Unlike a blog post that you did not create | Successfully | Pass |

(*) See Bugs below

## Bugs

## Lighthouse

The performance scores appear to be low, and I attribute this to the images uploaded for each blog post being hosted on a third-party cloud-based platform.

Mobile

![Lighthouse Mobile Score](documentation/images/lighthouse_mobile.png)

Desktop

![Lighthouse Desktop Score](documentation/images/lighthouse_desktop.png)
## Validation Testing

### HTML & CSS

HTML & CSS testing, I used [W3 Validator](https://validator.w3.org/)



![HTML Validation - Descendant Error](documentation/testing_documentation/validation/base.html_button_descendant.png)

Fixed:

## Python Testing

Python pep8 validation was done via [Code Institute's Python Linter](https://pep8ci.herokuapp.com/)

The only issues encountered here were with indentations and the fact that certain lines of text exceeded the 79-character limit, but these have now been resolved.

Python Files Tested:

- models
- forms
- views
- urls

___

### Full Testing

Full testing was performed on the following devices:

* Laptop:
  * Macbook Pro 2021 14 inch screen
* Mobile Devices:
  * iPhone 13 pro.
  * iPhone 11 pro.
  * Phone X.

  

