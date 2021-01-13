# Amazon Crawler Backend

A backend that can be queried for products on Amazon and then to fetch the reviews. For educational purposes.


## Installation

Installing is as simple as downloading the project and running the main.py file, the backend will then run of localhost.


## Routes

`/search`

Gets a page based on the search string.

`/search_next`

Gets the next page of products. Should be used on the response of the search, requires the "next" url.

`/fetch_reviews`

Initiates the server to fetch all the reviews of the selected product and stores them as a new-line seperated txt file. Asynchronous.
