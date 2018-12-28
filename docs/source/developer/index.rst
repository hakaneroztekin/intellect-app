Developer Guide
===============

Database Design
---------------

**explain the database design of your project**

**include the E/R diagram(s)**

Code
----

The code can be explained in three parts.

- HTML/CSS
- Python
- Database

**1- HTML/CSS**
There are a differentiated HTML code for each page. Though, they all share the common one,
layout.html. Let's start with it.

Let's start with CSS part of the layout.html.

::

   .. code-block:: python

           <style>
        html, body, h1, h2, h3, h4, h5, h6 {
        font-family: 'Hammersmith One', serif;
        }

The code part above, font is determined. Then the rest of the code layouts the general style.

   .. code-block:: python

        * {
      box-sizing: border-box;
    }

    /* Create two equal columns that floats next to each other */
    .column {
      float: left;
      padding: 10px;
      padding-right: 15px;
    }

    .left {
      width: 85%;
    }

    .right {
      width: 15%
    }

    {# responsive to screen size #}
    @media screen and (max-width: 600px) {
      .column {
        width: 100%;
      }
    }

    /* Clear floats after the columns */
    .row:after {
      content: "";
      display: table;
      clear: both;
    }
    </style>

Below you can see the jquery and Bootstrap scripts initializations.
.. code-block:: python
   <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
   <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

Now we create "title" block which will be different for each page.
.. code-block:: python
   <title>{% block title %}{% endblock %}</title>

After, we create our menu. It is designed as two lines. The first one consists of
couple links for necessary redirections. Because it's same for all the pages, it is not
labeled as block, as in the second menu bar. Second menu bar includes links to the community lists.
It also has a welcome message with included username. Because it's only necessary for mylists page
it is labeled as secondmenubar.

.. code-block:: python

    <div class="w3-bar w3-text-yellow w3-large">
        <h5>
            <a href="/mylists"><button class="w3-bar-item w3-button w3-right"><b>Your Lists</b></button></a>
            <a href="/signup"><button class="w3-bar-item w3-button w3-right"><b>Sign up</b></button></a>
            <a href="/signin"><button class="w3-bar-item w3-button w3-right"><b>Sign in</b></button></a>
            <a href="/"><button class="w3-bar-item w3-button w3-left"><b>Intellect</b></button></a>
        </h5>
    </div>

    {% block secondmenubar %}
    <div class="w3-bar w3-text-brown w3-large w3-border-top w3-border-bottom">
        <h5>
            <a href="/mylists"><button class="w3-bar-item w3-button w3-left"><b>My Lists</b></button></a>
            <a href="/mylists/movies"><button class="w3-bar-item w3-button w3-left"><b>Community Movies</b></button></a>
            <a href="/mylists/musics"><button class="w3-bar-item w3-button w3-left"><b>Community Musics</b></button></a>
            <button class="w3-bar-item w3-button w3-right"><b>Welcome {{ current_user[2] }}!</b></button>
        </h5>
    </div>
    {% endblock %}

Then create a block for body. It's empty for the homepage.

.. code-block:: python

    <body>
        {% block content %}{%  endblock %}
    </body>

Create the footer;

.. code-block:: python

    {   % block footer %}
    <footer class="w3-bottom w3-container w3-text-gray">
        <p>Developed by Hakan Eroztekin</p>
    </footer>
    {% endblock %}

Block for additional styles;

.. code-block:: python

    {% block additional_styles %}
    <style>
       body {
        padding-left: 10px;
       }
    </style>
    {% endblock %}

That's it for layout.html. All the other pages are derived from this page. While it is common, they differ in contents in the blocks.
There are 12 more html pages.

- **User Authentication:** signup.html, signin.html
- **Homepage:** homepage.html
- **User Lists:** mylists.html
- **Community Lists for Movies:** movies.html, add_movies.html, update_movies.html, delete_movies.html
- **Community Lists for Musics:** musics.html, add_musics.html, update_musics.html, delete_musics.html

Almost all the pages are created to work with forms. The forms has fields according to the related database tables.

**User Authentication** *signup.html*
The technical part of the page can be seen below:

.. code-block:: python

    {% block content %}
            <h1>Sign-up to Intellect</h1>
        <form method=post>
      <dl>
        {{ render_field(form.username) }}
        {{ render_field(form.email) }}
        {{ render_field(form.name) }}
        {{ render_field(form.surname) }}
        {{ render_field(form.age) }}
        {{ render_field(form.gender) }}
        {{ render_field(form.password) }}
        {{ render_field(form.confirm) }}
      </dl>
      <p><input type=submit value=Register>

    {% endblock %}


.. code-block:: python



.. toctree::

   Hakan Eröztekin
