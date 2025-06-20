CREATE TABLE customers (
customer_id INT PRIMARY KEY,
customer_name VARCHAR(100),
registration_date DATE
);
CREATE TABLE products (
product_id INT PRIMARY KEY,
product_name VARCHAR(100),
category VARCHAR(50),
price DECIMAL(10, 2)
);
CREATE TABLE orders (
order_id INT PRIMARY KEY,
customer_id INT,
order_date DATE,
total_amount DECIMAL(10, 2),
FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
CREATE TABLE order_items (
order_item_id INT PRIMARY KEY,
order_id INT,
product_id INT,
quantity INT,
unit_price DECIMAL(10, 2),
FOREIGN KEY (order_id) REFERENCES orders(order_id),
FOREIGN KEY (product_id) REFERENCES products(product_id)
);
INSERT INTO customers (customer_id, customer_name, registration_date) VALUES
(1, 'Иван Иванов', '2023-01-15'),
(2, 'Мария Смирнова', '2023-03-22'),
(3, 'Алексей Петров', '2022-11-05'),
(4, 'Ольга Кузнецова', '2024-06-10'),
(5, 'Дмитрий Орлов', '2022-12-01'),
(6, 'Владимир Иванов', '2021-11-01'),
(7, 'Ирина Сергеевна', '2020-07-11');
INSERT INTO products (product_id, product_name, category, price) VALUES
(101, 'Ноутбук Lenovo', 'Электроника', 75000.00),
(102, 'Смартфон Samsung', 'Электроника', 55000.00),
(103, 'Кофеварка Bosch', 'Бытовая техника', 8500.00),
(104, 'Фен Philips', 'Бытовая техника', 3000.00),
(105, 'Монитор LG', 'Электроника', 23000.00);
INSERT INTO orders (order_id, customer_id, order_date, total_amount) VALUES
(201, 1, '2024-01-10', 75000.00),
(202, 2, '2024-02-05', 8500.00),
(203, 1, '2024-03-15', 55000.00),
(204, 3, '2023-12-20', 11500.00),
(205, 2, '2025-01-25', 3000.00),
(206, 4, '2025-05-15', 23000.00);
INSERT INTO order_items (order_item_id, order_id, product_id, quantity,unit_price) VALUES
(301, 201, 101, 1, 75000.00),
(302, 202, 103, 1, 8500.00),
(303, 203, 102, 1, 55000.00),
(304, 204, 103, 1, 8500.00),
(305, 204, 104, 1, 3000.00),
(306, 205, 104, 1, 3000.00),
(307, 206, 105, 1, 23000.00);