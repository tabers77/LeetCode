# Write your MySQL query statement below

select
id, 

#["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"].

# we would need to aggregate 
SUM(case when month = 'Jan' then revenue else null end) as Jan_Revenue,
SUM(case when month = 'Feb' then revenue else null end) as Feb_Revenue,
SUM(case when month = 'Mar' then revenue else null end) as Mar_Revenue,
SUM( case when month = 'Apr' then revenue else null end) as Apr_Revenue,
SUM(case when month = 'May' then revenue else null end) as May_Revenue,
SUM(case when month = 'Jun' then revenue else null end) as Jun_Revenue,
SUM(case when month = 'Jul' then revenue else null end)as Jul_Revenue,
SUM( case when month = 'Aug' then revenue else null end) as Aug_Revenue,
SUM(case when month = 'Sep' then revenue else null end) as Sep_Revenue,
SUM(case when month = 'Oct' then revenue else null end) as Oct_Revenue,
SUM(case when month = 'Nov' then revenue else null end) as Nov_Revenue,
SUM(case when month = 'Dec' then revenue else null end) as Dec_Revenue


from 
Department

group by id