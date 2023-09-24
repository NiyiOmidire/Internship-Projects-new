from selenium.webdriver.common.by import By
from behave import *
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
PRODUCT_NAME = (By.ID, 'productTitle')
COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")


@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    context.driver.wait.until(
        EC.element_to_be_clickable(ADD_TO_CART_BTN),
        message='Add to Cart btn not clickable').click()


@when('Store product name')
def get_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Current product: {context.product_name}')


# @then('Verify user can click through colors')
# def verify_can_click_colors(context):
#     expected_colors = ['Army Green', 'Black', 'Blue', 'Brown'] # 0, 1, 2, 3
#     actual_colors = []
#
#     colors = context.driver.find_elements(*COLOR_OPTIONS)
#
#     for color in colors[:4]:
#         color.click()
#         current_color = context.driver.find_element(*CURRENT_COLOR).text
#
#         actual_colors.append(current_color)
#
#     assert actual_colors == expected_colors, f'Expected {expected_colors} did not match actual {actual_colors}'


# #Homework #5(2a)
# @then('Verify user can click through colors')
# def verify_can_click_colors(context):
#     expected_colors = ['Army Green', 'Black', 'Blue', 'Brown',
#     'Burgundy', 'Caramel', 'Dark Blue', 'Denim Blue', 'Gray',
#     'Green', 'Khaki', 'Light-green', 'Orange', 'Pink', 'Purple',
#     'Red', 'Rose Red', 'Stripe Caramel', 'Stripe Gray',
#     'Stripe Green', 'Stripe Khaki', 'Stripe Red',
#     'Stripe Sapphire Blue', 'White', 'Yellow'] # All colors
#     actual_colors = []
#
#     colors = context.driver.find_elements(*COLOR_OPTIONS)
#
#     for color in colors:
#         color.click()
#         current_color = context.driver.find_element(*CURRENT_COLOR).text
#         # print(current_color)
#         actual_colors.append(current_color)
#
#     # print(actual_colors)
#
#     assert actual_colors == expected_colors, f'Expected {expected_colors} did not match actual {actual_colors}'


#Homework #5(2b)
@then('Verify user can click through colors')
def verify_can_click_colors(context):
    expected_colors = ['Black', 'Blue Over Dye', 'Bright White',
    'Dark Blue Vintage', 'Dark Indigo', 'Dark Khaki Brown',
    'Dark Wash', 'Indigo Wash', 'Light Blue Vintage',
    'Light Khaki Brown', 'Light Wash', 'Medium Blue Vintage',
    'Medium Wash', 'Olive', 'Rinsed', 'Sage Green', 'Vintage Wash',
    'Washed Black', 'Washed Grey'] # All colors
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for color in colors:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        # print(current_color)
        actual_colors.append(current_color)

    print(actual_colors)

    assert actual_colors == expected_colors, f'Expected {expected_colors} did not match actual {actual_colors}'