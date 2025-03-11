## Task 1. Checking the uniqueness of passwords using a Bloom filter

>   Create function to check the uniqueness of passwords using a Bloom filter. This function should determine whether a password has been used before without having to store the passwords themselves.

#### Specifications:

- Implement the BloomFilter class, which provides adding elements to the filter and checking if the element is in the filter.

- Implement a check_password_uniqueness function that uses an instance of BloomFilter and checks the list of new passwords for uniqueness. It should return the result of the check for each password.

- Ensure that all data types are processed correctly. Passwords should be processed simply as strings, without hashing. Empty or invalid values should also be taken into account and handled properly.

- The function and class should work with large data sets using a minimum of memory.

## Task 2. Comparing the performance of HyperLogLog with exact unique element counting

> Create a script to compare the exact count of unique elements and the count using HyperLogLog.

#### Specifications:

-   Download the dataset from the [real log file lms-stage-access.log](https://drive.google.com/file/d/13NUCSG7l_z2B7gYuQubYIpIjJTnwOAOb/view?usp=sharing), which contains information about IP addresses.
-   Implement a method to accurately count unique IP addresses using a set structure.
-   Implement a method to approximate the count of unique IP addresses using HyperLogLog.
-   Compare the methods by execution time.
