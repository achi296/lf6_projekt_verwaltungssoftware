#!/bin/bash
# The parameter for this file is the password of the root user
# $1 = root password for MySQL instance
# Warnings will be suppressed (2>/dev/null)
RED='\033[0;31m'
NC='\033[0m'
YELLOW='\033[0;33m'
if [[ $1 == "" ]]
then
  printf "${RED}ERROR: Please provide a password as a parameter${NC}\n"
  echo -e "${YELLOW}INFO: ${NC}<scriptname> <password>\m"
  exit 1
fi

# create the new database "verwaltung"
echo -e "${YELLOW}INFO: ${NC}Creating the new database verwaltung\n"
mysql --user=root --password=$1 < database/ddl/create_database.sql 2>/dev/null
# create a new user "pyuser" and set the permissions
echo -e "${YELLOW}INFO: ${NC}Creating a new user pyuser\n"
mysql --user=root --password=$1 < database/setup_permissions.sql 2>/dev/null
# create the tables
declare -i I=1
MAX=$(ls "database/ddl/" | wc -l)
for SCRIPT in database/ddl/*.sql
do
  echo -e "${YELLOW}INFO: ${NC}Executing script (${I}/${MAX}): ${SCRIPT}\n"
  mysql --user=root --password=$1 < $SCRIPT 2>/dev/null
  I=$I+1
done