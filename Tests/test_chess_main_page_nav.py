from playwright.sync_api import Page, Browser, BrowserContext
from Models.chess_main_page import ChessHomePage
from Utilities.generic_functions import goToURL

def test_verify_nav_elements(page):
  chessPage = ChessHomePage(page)

  #Key : data-nav-link, value = href
  navElements = {
    "home": "https://www.chess.com/",
    "play": "https://www.chess.com/play",
    "puzzles": "https://www.chess.com/puzzles/rated",
    "learn": "https://www.chess.com/learn"
  }

  goToURL(page, "https://www.chess.com")
  chessPage.check_primary_nav_list(navElements)

def test_testing_nav_script(page):
  chessPage = ChessHomePage(page)
  """
  pass in data-nav-link and text of the child span if needed
  """
  goToURL(page, "https://www.chess.com/")
  chessPage.click_primary_nav_item("learn", None, None)

  goToURL(page, "https://www.chess.com/")
  chessPage.click_primary_nav_item("play", "Play Bots", None)

