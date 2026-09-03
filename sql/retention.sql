-- Retention по месячным когортам
with first_order as (
    select customer_id,
           date_trunc('month', min(order_date)) as cohort_month
    from orders
    group by 1
)
select cohort_month, count(distinct customer_id) as customers
from first_order
group by 1
order by 1;
checking
DOG
