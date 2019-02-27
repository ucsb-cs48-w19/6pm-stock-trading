# 6pm-stock-trading

Travis-CI status on Master Branch: <a href="https://travis-ci.org/ucsb-cs48-w19/6pm-stock-trading">
<img src="https://travis-ci.org/ucsb-cs48-w19/6pm-stock-trading.svg?branch=master" alt="Build Status">
</a>

## Project summary

### One-sentence description of the project

Mock environment for managaed account investment structure.

### Additional information about the project

This app will be completely hands off to the user. Users' accounts will be managed day to day by an automated trading algorithm powered by live stock price data. Users will be able to personalize the investment strategy choosen during initial setup to help them reach their financial goals. 


## Installation

### Prerequisites

1. Install Python 3.7
2. pip install flask
3. Install PostgreSQL
4. pip install -r requirements.txt or pip3 install -r requirements.txt
[Bootstrap 3 Reference](https://getbootstrap.com/docs/3.3/components/ "Bootstrap 3 Reference")
https://getbootstrap.com/docs/3.3/components/



### Installation Steps
1. `export APP_SETTINGS="config.DevelopmentConfig"`
2. `export DATABASE_URL="[name of your postgres database]"`
3. `python manage.py db init`
4. `python manage.py db migrate`
5. `python manage.py db upgrade`
6. `python app.py`


### Issues
1. `rm -r migrations/`
2. Delete database tables in psql with 
      `drop table alembic_version;`
      `drop table users;`
3. Redo Installation Steps 3 - 6    

## Functionality

https://stock-6pm-final.herokuapp.com 


## Known Problems

1. The Python script has to manually run right now, we need to find a way to run the script automatically everyday in the background.
   Solution: Using Heroku add-on tool - Heroku Scheduler to deploy and run the script on heroku.
>>>>>>> b4bd40333a7f226157592d3c5ee8b0bea98c74bd

## Contributing


1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## License

If you haven't already, add a file called `LICENSE.txt` with the text of the appropriate license.
We recommend using the MIT license: <https://choosealicense.com/licenses/mit/>
