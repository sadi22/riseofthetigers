# Rise of the Tigers

This is a django based cricket news blog .It offers:

  - Live Cricket Score
  - Scorecard
  - A simple Poll
  
## Version
1.0.0

# Requirements
- python 2.7
- django == 1.9
- django-autoslug
- django-contrib-comments
- datetime
- django-stdimage
- beautifulsoup4
- django-taggit
- flask

## Installation

### 1. git Clone
```sh
$ cd /path/to/your/workspace
$ git clone https://github.com/sadi22/riseofthetigers.git
```
### 2. virtualenv

```sh
$ cd riseofthetigers
$ virtualenv myENV
```
Activate the virual environment
### 3. requirements

```sh
$ pip install -r requirements.txt
```

### 4. Initialize the database
```sh
$ python manage.py makemigrations
$ python manage.py migrate
```
## Ready? Go!
```sh
$ python manage.py runserver
```
Want to contribute? Great!

