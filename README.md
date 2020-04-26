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
