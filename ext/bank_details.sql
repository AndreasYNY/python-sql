CREATE TABLE
  `bank_details` (
    `id` int unsigned NOT NULL AUTO_INCREMENT,
    `Bank_country` varchar(100) DEFAULT NULL,
    `Bank_Number` int DEFAULT NULL,
    `employee_id` int unsigned DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `employee_id` (`employee_id`),
    CONSTRAINT `bank_details_ibfk_2` FOREIGN KEY (`employee_id`) REFERENCES `Employees` (`id`) ON DELETE CASCADE
  ) ENGINE = InnoDB AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci