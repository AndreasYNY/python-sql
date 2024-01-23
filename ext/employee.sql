CREATE TABLE
  `Employees` (
    `Name` varchar(100) DEFAULT NULL,
    `Age` int DEFAULT NULL,
    `Address` varchar(100) DEFAULT NULL,
    `Gender` varchar(100) DEFAULT NULL,
    `DOB` date DEFAULT NULL,
    `Email` varchar(100) DEFAULT NULL,
    `Role` varchar(100) DEFAULT NULL,
    `id` int unsigned NOT NULL AUTO_INCREMENT,
    `pet_owned` int DEFAULT NULL,
    `Country` varchar(100) DEFAULT NULL,
    PRIMARY KEY (`id`)
  ) ENGINE = InnoDB AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci