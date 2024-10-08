from playwright.sync_api import expect
from Utilities.generic_functions import close_generic_modal

class ChessHomePage:
  def __init__(self, page):
    self.page = page

    #Define Page selectors
    #Nav Bar
    self.primary_nav_elements = page.locator(".nav-component a.nav-link-component")
    self.nav_bar_more_button = page.locator('.nav-component button[aria-label="More"]')

  """
  Script is used to verify the primary nav elements on the home page.
  : -> elements is passed as a dict of the nav data value + href value.
  Checks iteratively because we want the order to be correct as well.
  """
  def check_primary_nav_list(self, elements):
    
    counter = 0

    for data_value, href in elements.items():
      #First we will verify the data-value and the href on the DOM.
      expect(self.primary_nav_elements.nth(counter), f"data-nav-link was not {data_value}.").to_have_attribute("data-nav-link", data_value)
      expect(self.primary_nav_elements.nth(counter), f"Href for {data_value} was not {href}.").to_have_attribute("href", href)

      #Visit the link 
      self.primary_nav_elements.nth(counter).click()
      expect(self.page, f"Page redirected to was not {href}.").to_have_url(href)

      #Short wait for redirection
      self.page.wait_for_timeout(1200)
      #Puzzles causes a browser popup, close it
      if data_value == "puzzles":
        close_generic_modal(self.page)

      counter += 1

  """
  This script is used to visit a specific nav item, which we can do before doing other pages.
  We will use dynamic selectors so we can pass in exactly where we want to navigate.
  """
  def click_primary_nav_item(self, nav_item, child_nav_item, expect_url):
    #Gonna use dynamic selectors
    if child_nav_item is None and nav_item != "more":
      self.page.locator(f"//a[@data-nav-link='{nav_item}']").click()
    elif nav_item == "more":
      self.nav_bar_more_button.hover()
      self.page.locator(f"//div[@data-nav-panel='{nav_item}']//span[text() = '{child_nav_item}']/..").click()
    else:
      self.page.locator(f"//a[@data-nav-link='{nav_item}']").hover()
      self.page.locator(f"//div[@data-nav-panel='{nav_item}']//span[text() = '{child_nav_item}']/..").click()

    if child_nav_item == "ChessKid":
      self.page.wait_for_timeout(3000)
      new_tab = self.page.context.pages[1]

      expect(new_tab).to_have_url("https://www.chesskid.com/")

      new_tab.locator('//span[contains(text(), "Play Now")]/..').click()
      self.page.wait_for_timeout(3000)
    elif expect_url is not None:
      expect(self.page, f"Expected url to be {expect_url}.").to_have_url(expect_url)