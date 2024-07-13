SELECT
	type,
	COUNT(distinct hex)
FROM 
	readsb
GROUP BY
	type