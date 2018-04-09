To solve this problem, we will use multiple pass map reduce jobs.
The map reduce jobs will be chained/cascaded together to get the final answer.
Initially we will have our data points.
The first mapper will get the id as key and score and device type as values.
It will return the count of each id as 1.
The first reducer will get these key value pairs with 1 count and reduce them
for each unique id type and avg the score values.
The 2nd mapper will get these transformed values and then for each device type it will assign it as poor or not.
The 2nd reducer will reduce these pairs to all those who are poor for each device type.