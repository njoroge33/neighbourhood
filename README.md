# Neighborhood

A web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.

## As users you can :
* Sign in to the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.

### Usage example

1. signup then login.
2. Open the website and browse the images.
3. If you see the post and business from other users around your neighborhood.***


## Development setup

- To access the Code behind this site, you will need to:

1. Clone this repo:
  ```bash
  git clone https://github.com/njoroge33/neighborhood
  ```
2. Move to the folder and install requirements
  ```bash
  cd neighborhood
  pip install -r requirements.txt
  ```
3. Create database on psql shell
  ```SQL
  psql
  CREATE DATABASE neighbor;
  ```
4. Migrate the database and run the application
  ```bash
  python manage.py migrate
  python manage.py runserver
  ```

## Technologies Used
- Python3.6
- Django

## License
MIT &copy;2020 [John Gichuhi](https://github.com/njoroge33/neighbourhood/blob/master/LICENSE)
Neighborhood

