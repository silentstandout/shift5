SELECT 
	hex, 
	now, 
	COUNT(*) as dupes 
FROM 
	reads 
GROUP BY
	hex, 
	now 
ORDER BY
	`dupes` desc
