# MiniPeeks Genomic App
Welcome to the home page of MiniPeeks(no relation to any competitors, what-so-ever), a genetics information company which offers a product which will analyze a variety of genes and diseases from next generation sequencing(NGS) data! At MiniPeeks we are always trying to expand our current offering by including more diseases whenever we have the ability to cover them with sufficient specificity and selectivity. As a result, our genetic counselors have requested the ability to connect our gene and disease information together, and be able to create/edit new gene-disease associations and diseases, without them showing until requested.

The following user story is something that you have been tasked with to enhance our platform, pushing our ability to provide a cutting edge analysis to our patients:

## Setup
1. Clone this git repo locally and setup a Python/Django environment to work with.
2. The provided requirements.txt has all the dependancies you will need.
3. We will be using SQLite as our database as choice here, because its awesome, but mainly because the final database can be zipped up with the rest of your code and sent back to us!
4. Load the provided data in `genomics/fixtures/initial.json` for a set of genes and diseases to test with.
6. Feel free to install additional packages as you see fit to complete the tasks below.

## Background
As a genetic counselor, I would like to be able to view all of our disease information in a similar fashion as the gene pages already created(obviously if you can make it look better, that'd be awesome, but not required). I would also like to be able to make connections between genes and diseases in our platform, where a disease can be associated with **multiple** genes and a gene can be associated with **multiple** diseases. Additionally, I should be able to specify which diseases are **linked** and **active** for a particular gene and which ones are **linked** and **not active**.
Since I don't know how to use databases either, I should be able to view both a list and detail level page for genes and diseases, exposing the above information; more details below in the AC.

## Acceptance Criteria
* Update models to be able to link diseases and genes together, as specified above.
    * A JSON file for the description of the connections we would like to see can be found in `genomics/fixtures/connections.json`, please create all these connections based on how you modeled the data.
* Create a disease list page with the following information displayed for each record:
    *   `Name` - As defined on the model
    *   `Primary Inheritance` - as defined on the model
    *   `Active Genes` - A list of the `gene.ens_gene` for genes with an **active** link for that disease
* Create a disease detail page, displaying all available fields on the model and all genes linked to the specified disease.
    * Each gene record should have a hyperlink to navigate to the associated gene detail page and whether or not it is an **active** link with the specified disease.
* Update `genomics/templates/genomics/gene-list.html` to include the count of **active** diseases associated with the given gene.
* Update `genomics/templates/genomics/gene-detail.html` to include information about all of the diseases linked to the specified gene.
    * Each disease record should have a hyperlink to navigate to the associated disease detail page and whether or not it is an **active** link with the specified gene.

## Bonus Round
* Develop a dashboard landing page, include some interesting data!
* Assume the AC got changed at the last minute, and now we want to be able to record the date and time associated when a disease was made **active** for a particular gene. Write the code necessary to capture this information, then display it in the platform where relevant.

## Tips
1. Data is only as valuable as it is interpretable, the easier it is to read and digest the data you present, the better! Choosing what to display is just as important as choosing what not to display. Many of the AC are purposefully left open ended to see what you can come up with!
2. Prototype for 1x; Build for 10x; Engineer for 100x.