# 316project

This is the 316 Project


We hosted the database on a heroku server. On mac, run this to drop all the tables in the database: 
`heroku pg:psql -a class-stage <drop.sql`

Run this to create the tables:
`heroku pg:psql -a class-stage <create.sql`

Run this to load the data:
`heroku pg:psql -a class-stage <load.sql`

To create the tables on a personal server, run the following commands:
The sql files are contained in the directory 'final sql files':
Run this to drop all the tables in the database: 
`psql <drop.sql`

Run this to create the tables:
`psql <create.sql`

Run this to load the data:
`psql <load.sql`

To deploy locally, you can run 'python app.py'

To deploy to heroku: you must have cli for heroku installed and then you can push to heroku using 'git push stage master'


Flask App:

We have a model.py file that describes the database structure to sqlalchemy. Then we also have an app.py file that manages the backend. We have two paths,
/courseoff and /schedule. From /courseoff, you can add filters such as 'courseoff/?subject=COMPSCI' and it will return JSON text containing the course information.
From schedule, you can access the saved schedules and also post schedules to /schedule.

Link to Course Scheduler: https://nervous-williams-350285.netlify.app/
Backend: http://class-pro.herokuapp.com/
API: https://docs.google.com/document/d/1RbDtwdIZP0dK5ewpGbcaiGVpDOG7IvGwDW4ienBmVd0/edit
GitLab: https://coursework.cs.duke.edu/bowen.jiang/316project/