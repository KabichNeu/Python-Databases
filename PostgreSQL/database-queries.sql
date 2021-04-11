create database red30;
\c red30;
\dt;

SELECT * FROM sales;
\d sales;
\copy sales FROM '<PATH OF CSV FILE>' WITH DELIMITER ',' CSV HEADER;
