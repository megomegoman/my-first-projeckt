from pages.produkt_page import ProduktPage

def test_guest_can_add_produkt_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    prod_page = ProduktPage(browser, link)
    prod_page.open()
    prod_page.add_to_bascet()
    prod_page.solve_quiz_and_get_code()
    prod_page.finding_a_product_in_the_basket()
