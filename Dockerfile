FROM mariadb/server:latest

ENV MYSQL_ROOT_PASSWORD=root

ADD db.sql /docker-entrypoint-initdb.d

EXPOSE 3306