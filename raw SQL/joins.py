"""

select * from product_photo pp
left join product p on p.id = pp.product_id;

Цей запит поєднує дві таблиці
Лефт означає, що перша таблиця це pp і вона головна
Отже ми вибираємо select * from pp, а потім до кожного рядка прикручуємо
другу таблицю яку ми заджоінили

Якщо в правій таблиці не знаходиться підходячих записів тоді в колонки
підставляється нулл

left/right outer joins it is same as just left/right joins

right join ідентично працює як і лівий тільки головна таблиця права
inner join поверне тільки рядки де виконується умова по якій відбувається join

select c.name, SUM(p.price) from customer
join cart on cart.customer_id = c.id
join cart_product on cart_product.cart_id = cart.id
join product on cart_product.product_id = product.id
group by c.name;

"""