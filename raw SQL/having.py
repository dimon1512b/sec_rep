"""
having - працює як і where тільки він працює лише з групами. Тобто з такими
штуками як sum, count і іншими функціями агругації. І пишеться майже вкінці

select c.name, coalesce(sum(p.price), 0) from customer
left join cart on cart.customer_id = c.id
left join cart_product on cart_product.cart_id = cart.id
left join product on cart_product.product_id = product.id
group by c.name
having sum(p.price) > 0;
"""