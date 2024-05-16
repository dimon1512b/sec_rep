"""
coalesce - функція яка може замінити нулл на щось інше

select c.name, coalesce(sum(p.price), 0) from customer
left join cart on cart.customer_id = c.id
left join cart_product on cart_product.cart_id = cart.id
left join product on cart_product.product_id = product.id
group by c.name;

"""