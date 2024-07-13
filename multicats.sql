SELECT
	hex
FROM
	(SELECT 
		hex, 
		COUNT(distinct category) as 'catct' 
	FROM 
		readsb 
	WHERE
		category is not null
	GROUP BY 
		hex) c
WHERE
	catct='2'