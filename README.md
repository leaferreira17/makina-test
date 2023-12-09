# makina-test
## To start the app
Make sure to download Pillow first : 
```console

~$ pip install Pillow

```


If still in the `makina-test/` directory, go to `lebonangle/` : 
```console

~$ cd lebonangle

```
Finally, launch app with : 
```console
~$ python manage.py runserver
```
Enjoy !
## Makina Corpus technical test
Create a django-driven website that allows users to list their items for sale to other users.
### Requirements

#### Homepage

- Should show what items are available to buy.
- Viewing the homepage should not require users to login.
- Buying an item would require login, but is outside the scope of this project. For this project, just record somewhere that (non-logged-in-user) has clicked “buy”.

#### Selling Pages

- Logged in sellers should be able to add new items.
- To add an item, seller should give category, description and price. ~~Geolocation assumed from seller details.~~
- Seller should be able to view listed items, sold items, and cancel unsold items.

#### Signup

- User should be able to signup to enable them to list and sell items.
- Site should collect name, address, email and password.

#### Guidance

- This should be roughly a half-day project.
- This is a django project. (Don’t use a different web framework)
- This is a non-CSS project in that it should always be assumed that styling would happen at a later date, probably by someone else.
- While styling is not important, a functional user interface is. Buttons / forms etc must work in a sensible way.



