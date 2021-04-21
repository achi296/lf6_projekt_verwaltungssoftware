#!/bin/bash
# The parameter for this file is the password of the root user
# $1 = root password for MySQL instance

# create the new database "verwaltung"
echo -e "Creating the new database verwaltung\n"
mysql -h localhost -u root -p $1 < database/create_database.sql
# create a new user "pyuser" and set the permissions
echo -e "Creating a new user pyuser\n"
mysql -h localhost -u root -p $1 < database/setup_permissions.sql
# create the tables
declare -i I=1
MAX=$(ls "database/ddl/" | wc -l)
for SCRIPT in database/ddl/*.sql
do
  echo -e "Executing script (${I}/${MAX}): ${SCRIPT}\n"
  mysql -h localhost -u root -p $1 < $SCRIPT
  I=$I+1
done