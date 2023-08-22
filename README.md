![Bleach Banner](banner.png "Banner")

# Bleach API

This api is the live adaption of the Bleach Database.

## Base URL
Thanks to render for their generous free tier which helped me host the api.
```
https://bleach-api-8v2r.onrender.com/
```

## URL endpoints
List of all available endpoints:

1. `/`
	The root endpoint which generally returns some basic info about the API.
	```json
	{
    	"name": "Bleach API",
    	"description": "This is the API for Bleach Anime.",
    	"supports": ["shinigami", "humans", "quincy", "arrancar"],
    	"author": "AshishK1331",
    	"contact": "https://twitter.com/AshishK1331"
    }
	```

2. `/characters`
	The route returns all the available character types:
	```json
	{
		"types": [
			"shinigami",
			"humans",
			"quincy",
			"arrancar"
		]
	}
	```

3. `/characters/{type_id}`
	This route returns the list of all characters that belong to the given `type_id`, which can either be `shinigami`, `humans`, `quincy` or `arrancar`.
	```json
	{
		"shinigami": [
			"Niko Kuna",
			"Ikkaku Madarame",
			"Sajin Komamura",
			...
		]
	}
	```

4. `/characters/{type_id}/{name}`
	This route returns all the characters in the specified class with their respective data. You can chose any name by first bringing up entire list from the previous route.
	```json
	{
		"results": [
			{
				"id": "renji_abarai",
				"name": {
					"english": "Renji Abarai",
					"kanji": "阿散井 恋次",
					"romaji": "Abarai Renji"
				},
				"description": "Renji Abarai (阿散井 恋次, Abarai Renji) is the lieutenant of the 6th Division under Captain Byakuya Kuchiki and is married to Rukia Kuchiki. He formerly served as the 6th Seat of the 11th Division under Kenpachi Zaraki. Renji has brown eyes and long crimson hair, which is usually kept in a high ponytail. As a child, Renji's hairline was leveled. Later, he styled it in a large widow's-peak.",
				...
			}
		]
	}
	```