base_url = 'https://chess.com'

def goToURL(page, url):
  page.goto(url)

def close_generic_modal(page):
  page.locator('#first-time-modal .modal-first-time-modal button[aria-label="Close"]').click()