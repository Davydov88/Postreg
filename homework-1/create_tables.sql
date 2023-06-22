-- Создание таблицы employees
CREATE TABLE employees (
    employee_id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    title VARCHAR(50),
    birth_date DATE,
    notes TEXT
);

-- Создание таблицы customers
CREATE TABLE customers (
    customer_id VARCHAR(50),
    company_name VARCHAR(100),
    contact_name VARCHAR(100)
);

-- Создание таблицы orders
CREATE TABLE orders (
    order_id INT,
    customer_id VARCHAR(50),
    employee_id INT,
    order_date DATE,
    ship_city VARCHAR(100)
);
