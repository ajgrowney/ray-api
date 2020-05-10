
# Ray's API Docs
## Top Level Endpoints
1) clothing
2) echo
3) food
4) todo


### Clothing (/clothing)
#### Resources
-  /outfit
    - GET: Check Current Time
    - /accepted
        - POST: Specified outfit was accepted
    - /rejected
        - POST: Specified outfit was rejected 
- /laundry
    - GET: Check current status of laundry basket


### Echo (/echo)
#### Resources
-  /time 
    - GET: Check Current Time
- /hello
    - GET: Greeting (based on time of day)


### Food (/food)
#### Resources
-  /recipes
    - GET: List the recipes 
- /groceries
    - GET: Get the current grocery list
    - PUT: Update the current grocery list
    - DELETE: Clear the current grocery list

### Todo (/todo)
#### Resources
-  /calendar
    - GET: 
    - /today
        - GET: Get list of events today
    - /reminders
        - GET: Get list of active reminders 


### Django Terminology
- admin -> configuration file for django admin app
- apps -> configuration file for app itself
- migrations/ -> track changes to models.py file so database and models.py stay in sync
- models -> define database models which Django translates into DB tables
- view -> handle request/response logic
