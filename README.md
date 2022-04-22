# Cocktail Exercise

# Introduction 

The Cocktail DB is a public database of cocktails and drinks from around the world https://www.thecocktaildb.com/. 
The Cocktail DB has a public API to retrieve data about ingredients and drinks. See the documentation here https://www.thecocktaildb.com/api.php.

We have proposed some requirements for the cocktail API (this list is not exhaustive!).

# Your task is to:
1.	Write a minimum set of test cases to test the requirements below
2.	Write two additional test cases that are not covered by the requirements below.
3.	Automate the test cases using a language/framework of your choice.
4.	Suggest two non-functional tests that you would design
5.	Suggest a framework that could be used to automate the non-functional test above.
6.	Send your tests with instructions on how to execute the automated tests within 3 days.
7.	Always explain yourself clearly and let us know if any assumptions were made.


# Functional Requirements
Search Ingredients By Name: www.thecocktaildb.com/api/json/v1/1/search.php?i=vodka

* The system shall include a method to search by ingredient name and return the following fields: 
- Ingredient ID (string),
- Ingredient (string), 
- Description (string),
- Type (string), 
- Alcohol (string) and 
- ABV (string). 
* If an ingredient is non-alcoholic, Alcohol is null and ABV is null
* If an ingredient is alcoholic, Alcohol is yes and ABV is not null. 

Search Cocktails By Name: www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita

*	The system shall include a method to search by cocktail name. 
*	If the cocktail does not exist in the cocktail DB, the API shall return drinks as null. 
*	Searching for a cocktail by name is case-insensitive
* API response must contain the following Schema properties:

|Element Name|Type|Required|
|drinks|array|yes|


3. drinks	array	yes
4. strDrink	string / null	yes
5. strDrinkAlternative	string / null	no
6. strTags	string / null	yes
7. strVideo	string / null	no
8. strCategory	string / null	yes
9. strIBA	string / null	no
10. strAlcoholic	string / null	yes
11. strGlass	string / null	yes
12. strInstructions (ES/DE/FR/IT/ZH-HANS/ZH-HANT)	string / null	only strInstructions
13. strDrinkThumb	string / null	no
14. strIngredient1-15	string / null	only strIngredient1
15. strMeasure1-15	string / null	only strMeasure1
16. strImageSource	string / null	no
17. strImageAttribution	string / null	no
18. strCreativeCommonsConfirmed	string / null	yes
19. dateModified	string / null	yes
