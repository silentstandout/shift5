SELECT
	category,
	COUNT(distinct hex)
FROM 
	readsb
GROUP BY
	category