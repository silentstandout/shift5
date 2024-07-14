SELECT
	category,
	MAX(gs) as max_gs,
	DENSE_RANK() OVER (ORDER BY MAX(gs) DESC) as rank
FROM
	readsb
GROUP BY
	category
ORDER BY
	rank;