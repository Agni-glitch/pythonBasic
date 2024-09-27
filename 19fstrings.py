letter="Hey my namein {} and I am from {}"
country="India"
name ="Agni Roybar"
print(letter.format(name,country))
print(f"Hey my namein {name} and I am from {country}")
print(f"Hey my namein {{name}} and I am from {{country}}")

txt="For only {price:.2f} dollers"
print(txt.format(price=49.999))
# Hey my namein Agni Roybar and I am from India
# Hey my namein Agni Roybar and I am from India
# Hey my namein {name} and I am from {country}
# For only 50.00 dollers