# WANDERLUST 
 
### Top 5 Must-Visit Destinations To Zanzibar

![Wanderlust](documentation/images/)

Portfolio 4 Projects for Code Institute's Diploma in Full Stack Software Development.
___

Zanzibar Wanderlust is a travel blog dedicated to showcasing the top 5 destinations in Zanzibar. While our primary focus is on highlighting these must-visit spots, we also provide a platform for users to engage with our content and share their own travel experiences.

This full-stack blog site offers users the opportunity to explore detailed blog posts about each destination, create an account to personalize their experience, and leave comments to share their thoughts or ask questions. Join us as we take you on a virtual journey to the breathtaking sights and cultural wonders of Zanzibar, and become a part of our vibrant travel community.

Link to live site - [/](/)

## CONTENTS

- [Wanderlust](#wanderlust)
    - [Top 5 Must-Visit Destinations To Zanzibar](#Top-5-Must-Visit-Destinations-To-Zanzibar)
  - [CONTENTS](#contents)
  - [Site Objectives](#site-objectives)
- [User Experience/UX](#user-experienceux)
  - [Target Audience](#target-audience)
  - [User Stories](#user-stories)
    - [New Visitor Goals](#new-visitor-goals)
    - [Existing Visitor Goals](#existing-visitor-goals)
- [Design Choices](#design-choices)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Logo and Favicon](#logo-and-favicon)
  - [Wireframes](#wireframes)
  - [Flow Diagram](#flow-diagram)
  - [Database Plan](#database-plan)
- [Features](#features)
  - [Registration](#registration)
  - [Future Features](#future-features)
  - [Features Not Included](#features-not-included)
- [Technologies Used](#technologies-used)
- [Programming Languages, Frameworks and Libraries Used](#programming-languages-frameworks-and-libraries-used)
- [Agile](#agile)
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [User](#user)
  - [Bugs](#bugs)
  - [Lighthouse](#lighthouse)
  - [Validation Testing](#validation-testing)
    - [HTML \& CSS](#html--css)
  - [Python Testing](#python-testing)
  - [Deployment](#deployment)
    - [Github Deployment](#github-deployment)
    - [Creating a Fork or Copying](#creating-a-fork-or-copying)
    - [Clone](#clone)
    - [Repository deployment via Heroku](#repository-deployment-via-heroku)
    - [Deployment of the app](#deployment-of-the-app)
  - [Credits](#credits)
  - [Media](#media)
  - [Acknowledgments and Thanks](#acknowledgments-and-thanks)

___

## Site Objectives

The main objective of this project was to design and create a blog site that showcases my growing understanding of the libraries and frameworks available to developers. Specifically, the three main objectives were:

- ### Create a responsive, readable,  and clean  front end

I aimed to develop a front end that is readable, clean, and responsive. My goal was to ensure the site is easily accessible and intuitively navigable for users. To achieve this, I utilized Django and Bootstrap to design and style the front end.

- ### Utilize the existing backend functionality

Leverage the functionality provided by the backend framework, enabling users to create profiles, comment on any blog posts within the site, and delete their own comments if desired.

- ### Store project data on an external cloud database

Store project data on an external cloud database. I utilized ElephantSQL to host the PostgreSQL database for this project.

___

# User Experience/UX

## Target Audience

- Travelers who are interested in traveling, especially to the best places in African countries.

## User Stories

### New Visitor Goals

- To comprehend the purpose and content of the site.
- To learn how to navigate the site.
- To establish an account and interact with the site, as well as with other users and the site owner.

### Existing Visitor Goals

- Sign in and sign out of their account.
- Review blog posts and comments on each post.
- Contribute their own comments on blog posts on the site to interact with the site owner and other users.

___

# Design Choices

## Colour Scheme

The project's color scheme was derived from the colors featured in Code Institute's 'I think therefore I blog' walkthrough module. However, I have made numerous adjustments and enhancements to the styling and colors to align with my objectives. The scheme leans towards neutrality, with brighter colors reserved for actionable elements like buttons and links to facilitate navigation and site interaction.

## Typography

## Logo and Favicon

The logo was crafted utilizing an online logo creator - []()

## Wireframes

- Mobile Homepage Wireframe

![Mobile Homepage Wireframe](documentation/wireframes/mobile_homepage_wireframe.png)

- Mobile Post Detail Wireframe

![Mobile Post Detail Wireframe](documentation/wireframes/mobile_post_detail_wireframe.png)

- Desktop Homepage Wireframe

![Desktop Homepage Wireframe](documentation/wireframes/desktop_homepage_wireframe.png)

- Desktop Post Detail Wireframe

![Desktop Post Detail Wireframe](documentation/wireframes/desktop_postdetail_wireframe.png)

## Flow Diagram

Here is a diagram illustrating the potential flow through the site. It comprises two sections: on the left, it depicts the Admin, and on the right, it represents a site user.

![Site Flow Diagram](documentation/diagrams/site_flow_diagram.png)

## Database Plan

The database plan is relatively straightforward, outlining the stored information, data types, and identifying primary or foreign keys where relevant.

![Database plan](documentation/diagrams/database_plan.png)

# Features

## Registration

The user can create an account

![Create an Account](documentation/images/create_account.png)

View Blog Posts on Home Page

![View Blog Posts on Home Page](documentation/images/home.png)

Browse by Post Category

![Browse by Post Category](documentation/images/browse_by_category.png)

Comment on Blog Posts.

*Also depicted here is the trashcan icon, which enables users to delete their own comments if they choose to do so.*

![Comment on Blog Posts](documentation/images/commenting.png)

## Future Features

- Incorporating an option for users to edit their comments.
- Implementing a profile page for users to upload profile pictures and edit personal information.

## Features Not Included

Including an option for users to upload photos within comments.


___

# Technologies Used

Here are the technologies used to build this project:

- [Gitpod](https://gitpod.io/) To develop and construct this project.
- [Github](https://github.com) To host and manage the data storage for the site.
- [Gitpod](https://www.codeanywhere.com) The Integrated Development Environment (IDE) used for building the site.
- [PEP8 Validator](https://pep8ci.herokuapp.com/) A tool utilized to check Python code for errors.
- [ElephandSQL](https://www.elephantsql.com/) A platform employed to store a PostgreSQL database.
- [Cloudinary](https://cloudinary.com/) Utilized as cloud storage for images uploaded as part of the blog posts.
- [Heroku](https://id.heroku.com/) Deployed the project.

# Programming Languages, Frameworks and Libraries Used

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)

# Agile

The project was designed using Agile methodology, leveraging the Project Board and Issues sections in GitHub.


- [Project Board](https://github.com/users/markdaniel1982/projects/4/views/1)

# Testing

During the project, I conducted testing for functionality and styling issues after building each section or Function/Model. Corrections or fixes were made before proceeding. Additionally, I enlisted friends to test the site by signing up, adding, and deleting comments using various devices and platforms (IOS, Android, Mobile, Tablet, etc.), and they reported any encountered issues with functionality or styling.

## Manual Testing

*For any failures, a more detailed description is provided below the table*












