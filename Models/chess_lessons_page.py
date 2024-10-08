from playwright.sync_api import expect
import re

class ChessLessons:
  def __init__(self, page):
    self.page = page

    ###Selectors###
    """
    Lessons Page > New To Chess Section
    """
    #Header for new to chess
    self.new_to_chess_section = page.locator("div.level-component:nth-child(1)")
    self.new_to_chess_header = page.locator("div.level-component:nth-child(1) .level-title")

    #How to move block
    self.how_to_move_pieces_link = page.locator("div.level-component:nth-child(1) .course-component:nth-child(1) a")
    self.how_to_move_pieces_header = page.locator("div.level-component:nth-child(1) .course-component:nth-child(1) .course-content h3")
    self.how_to_move_pieces_description = page.locator("div.level-component:nth-child(1) .course-component:nth-child(1) .course-content .course-desc")
    self.how_to_move_pieces_author = page.locator("div.level-component:nth-child(1) .course-component:nth-child(1) .course-content .course-author")

    #Playing the game block
    self.playing_game_link = page.locator("div.level-component:nth-child(1) .course-component:nth-child(2) a")
    self.playing_game_header = page.locator("div.level-component:nth-child(1) .course-component:nth-child(2) .course-content h3")
    self.playing_game_description = page.locator("")
    self.playing_game_author = page.locator("")

  def verify_course_block(self, block_name):

    match block_name:
      case "how-to-move":
        expect(self.how_to_move_pieces_link).to_have_attribute("href", "https://www.chess.com/lessons/how-to-move-the-pieces")
        expect(self.how_to_move_pieces_header).to_have_text("How to Move the Pieces")
        expect(self.how_to_move_pieces_description).to_have_text("Get to know the chess pieces and how to set up the board.")
        expect(self.how_to_move_pieces_author).to_have_text(re.compile(r"Chess\.com"))
      case "playing-the-game":
        return 0



