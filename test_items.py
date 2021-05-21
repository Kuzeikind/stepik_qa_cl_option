import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import NoSuchElementException


def wait_for_element(browser, locator, locator_method=By.CSS_SELECTOR):
	'''
	Convenience function for locating alements with WebDriverWait.
	The functions is supposed to be run from a scope where a browser
	object is difined.
	'''
	element = None
	try:
		element = WebDriverWait(browser, 10).until(
				EC.presence_of_element_located(
					(locator_method, locator)
					)
				)
	except NoSuchElementException:
		element = None
	except Exception as e:
		print(e)

	return element



books = [
	'hacking-exposed-wireless_208',
	'reversing_202',
	'coders-at-work_207',
	'applied-cryptography_200',
	'we-are-anonymous_192'
]


class TestCart:
	def test_add_button_present(self, browser, language):
		base_url = f'http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/'
		browser.get(base_url)

		# Find the add-to-cart button.
		add_button_selector = 'button.btn-add-to-basket'
		add_button = wait_for_element(browser, add_button_selector)
		time.sleep(15)

		assert add_button is not None, '\nAdd to cart button not present on the page'



	@pytest.mark.skip
	@pytest.mark.parametrize('item', books)
	def test_add_to_cart_button(self, browser, language, item):
		item_url = f'http://selenium1py.pythonanywhere.com/{language}/catalogue/{item}/'
		browser.get(item_url)
		time.sleep(1)

		# Find the add-to-cart button and click it.
		add_button_selector = 'button.btn-add-to-basket'
		add_button = wait_for_element(browser, add_button_selector)
		add_button.click()

		# See an alert to check that the item was successfully added.
		alert_success_selector = '.alert-success'
		alert_success = wait_for_element(browser, alert_success_selector)
		assert alert_success is not None

	@pytest.mark.skip
	@pytest.mark.parametrize('item', books)
	def test_item_in_cart(self, browser, language, item):
		cart_url = f'http://selenium1py.pythonanywhere.com/{language}/basket/'
		browser.get(cart_url)
		time.sleep(1)

		# Find all items added to cart.
		cart_items_selector = '.basket_summary > .basket-items h3 > a'
		cart_items = browser.find_elements(
			By.CSS_SELECTOR,
			cart_items_selector
			)

		assert len(cart_items) > 0, '\ncart is empty'

		# See if the item is present in cart.
		found = any(
			[item in el.get_attribute('href') for el in cart_items]
			)


		assert found, f'{item} not found in cart'























