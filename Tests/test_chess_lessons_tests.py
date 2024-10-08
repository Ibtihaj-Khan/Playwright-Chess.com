from playwright.sync_api import Page, Browser, BrowserContext
from Models.chess_lessons_page import ChessLessons
from Models.chess_main_page import ChessHomePage
from Utilities.generic_functions import goToURL, base_url as chess_url, close_generic_modal

def test_verify_new_to_chess(page):
  home_page = ChessHomePage(page)
  lessons_page = ChessLessons(page)

  goToURL(page, chess_url)

  home_page.click_primary_nav_item("learn", "Lessons", "https://www.chess.com/lessons")
  close_generic_modal(page)
  lessons_page.verify_course_block("how-to-move")
  lessons_page.verify_course_block("playing-the-game")


