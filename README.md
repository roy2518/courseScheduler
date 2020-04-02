# 316project

This is the 316 Project


We hosted the database on a heroku server. On mac, run this to drop all the tables in the database: 
`heroku pg:psql -a testproject316 <drop.sql`

Run this to create the tables:
`heroku pg:psql -a testproject316 <create.sql`

Run this to load the data:
`heroku pg:psql -a testproject316 <load.sql`



To create the tables on a personal server, run the following commands:

Run this to drop all the tables in the database: 
`psql <drop.sql`

Run this to create the tables:
`psql <create.sql`

Run this to load the data:
`psql <load.sql`


Additionally, our test-sample.sql includes all the load statements in load.sql.


Production Server:

We are hosting the site and data on heroku at https://class-stage.herokuapp.com/ and https://class-pro.herokuapp.com/

To create the production schema, you can run create_production.sql:
'heroku pg:psql class-stage <create_proudction.sql'

You can find the load sql files in the data file folder and additionaly coreq.sql in the main. 
To load the datam