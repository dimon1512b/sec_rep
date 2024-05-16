"""
select c.name, SUM(p.price) from customer
join cart on cart.customer_id = c.id
join cart_product on cart_product.cart_id = cart.id
join product on cart_product.product_id = product.id
group by c.name;

коли ми робимо групування по колонці то виключаємо дублікати, а замість
дублікатів робимо об"єднання цих рядків, але в такому разі треба вказати
що робити із іншими колонками, наприклад у цьому випадку ми примінили функцію
сумування для другої колонки із двох, а перша попала під групування


"""