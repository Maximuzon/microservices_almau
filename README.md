# microservices_almau

Quick idea for managing vape shop storage. 
Table consist of few paramaters: 

1. flavour 

2. retail_price

3. base_price

4. quantity

5. volume_ml

6. status

7. buying_method


There is 4 services. 

***Service 1***

Creates a table if one not found. 
Fills in every column based on choices given. 
Writes 1 row every second. 
<img src="https://user-images.githubusercontent.com/80852667/220141787-341d7d26-7d96-451c-822b-4afc810674e8.png" width="500" height="150">
<img src="https://user-images.githubusercontent.com/80852667/220142290-e130bd75-27c6-4348-b0a6-45d6bdafb3e6.png" width="500" height="150">


***Service 2***

Checks for amount of specified liquid in storage based on status. 
0 - in storage
1 - sold.
![image](https://user-images.githubusercontent.com/80852667/220142598-6d1e0bdf-f921-44e0-8291-1782a5dd8f69.png)

***Service 3***

Counts expected total earning based on amount of bought liquids and calculating based on their base and retail price.
![image](https://user-images.githubusercontent.com/80852667/220142993-2d012dde-6dec-45fd-aed2-2e32cca981ee.png)

***Service 4***

Give detailed statistics about chosen flavour.
![image](https://user-images.githubusercontent.com/80852667/220143832-62512625-4ea1-408d-be0d-e080fafe89b2.png)
