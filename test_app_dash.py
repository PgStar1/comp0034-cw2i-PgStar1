from asyncio import wait_for
import requests
import time
from dash.testing.application_runners import import_app
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

def test_server_live(dash_duo):
    """
    GIVEN a dash_duo fixture instance of the server with the app
    WHEN a HTTP request to the home page is made
    THEN the HTTP response status code should be 200
    """

    # Create the app
    app = import_app(app_file="app_dash")
    # Start the server with the app using the dash_duo fixture
    dash_duo.start_server(app)

    # Delay to wait 2 seconds for the page to load
    dash_duo.driver.implicitly_wait(2)

    # Get the url for the web app root
    # You can print this to see what it is e.g. print(f'The server url is {url}')
    url = dash_duo.driver.current_url

    # Make a HTTP request to the server. This uses the Python requests library.
    response = requests.get(url)

    # Finally, use the pytest assertion to check that the status code in the HTTP response is 200
    assert response.status_code == 200


def test_home_h1textequals(dash_duo):
    """

    NOTE: dash_duo has a scope of fixture, so you have to start the server each time. There is no stop_server function,
    the dash_duo fixture handles this

    GIVEN the app is running
    WHEN the home page is available
    THEN the H1 heading text should be "Paralympics Dashboard"
    """
    app = import_app(app_file="app_dash")
    dash_duo.start_server(app)

    # Wait for the H1 heading to be visible, timeout if this does not happen within 4 seconds
    dash_duo.wait_for_element("h1", timeout=4)

    # Find the text content of the H1 heading element
    h1_text = dash_duo.find_element("h1").text

    # Check the heading has the text we expect
    assert h1_text == "TRANSPORT AND ENVIRONMENT METRICS AT VARIOUS HIGHER EDUCATION PROVIDERS"
 
def test_nav_link_charts(dash_duo):
    """
    Check the nav link works and leads to the charts page.
    """
    app = import_app(app_file="app_dash")
    dash_duo.start_server(app)
    # Delay just so I can visually check the page is loaded, this isn't necessary!
    time.sleep(2)

    # Wait for the navlink to be visible
    """dash_duo.wait_for_element("parking", timeout=4)

    # Click on the navlink
    dash_duo.driver.find_element(By.ID, "parking").click()"""
    
    navlink = WebDriverWait(dash_duo.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "parking"))
    )

    # Click on the navlink
    navlink.click()

    # Delay just so I can visually check the page is loaded, this isn't necessary!
    time.sleep(2)

    # Check the page url includes "charts"
    #dash_duo.wait_for_element("parking", timeout=4)
    assert "/spaces" in dash_duo.driver.current_url
    
def test_nav_link_energy(dash_duo):
    """
    Check the nav link works and leads to the charts page.
    """
    app = import_app(app_file="app_dash")
    dash_duo.start_server(app)
    # Delay just so I can visually check the page is loaded, this isn't necessary!
    time.sleep(2)

    # Wait for the navlink to be visible
    """dash_duo.wait_for_element("parking", timeout=4)

    # Click on the navlink
    dash_duo.driver.find_element(By.ID, "parking").click()"""
    
    navlink = WebDriverWait(dash_duo.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "energy"))
    )

    # Click on the navlink
    navlink.click()

    # Delay just so I can visually check the page is loaded, this isn't necessary!
    time.sleep(2)
    
    dash_duo.wait_for_element("h1", timeout=4)

    # Find the text content of the H1 heading element
    h1_text = dash_duo.find_element("h1").text

    # Check the page url includes "charts"
    #dash_duo.wait_for_element("parking", timeout=4)
    assert "/energy" in dash_duo.driver.current_url
    assert h1_text == "Renewable Energy Page"
    
"""def test_line_dropdown(dash_duo):
    app = import_app(app_file="app_dash")
    dash_duo.start_server(app)
    time.sleep(2)  # Delay just so I can visually check the page is loaded, this isn't necessary!

    navlink = WebDriverWait(dash_duo.driver, 20).until(
        EC.visibility_of_element_located((By.ID, "energy"))
    )
    navlink.click()  
    selected_item_text = "Aston University"

    # Click on the dropdown to open it
    dropdown = WebDriverWait(dash_duo.driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'Select-value-label'))
    )
    dropdown.click()

    # Find the option and click on it
    #options = WebDriverWait(dash_duo.driver, 20).until(
    #    EC.element_to_be_clickable((By.CLASS_NAME, 'VirtualizedSelectOption'))
    #)
    options = WebDriverWait(dash_duo.driver, 20).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, 'VirtualizedSelectOption')))
    #option_text = option.text
    #option.click()
    option = options[7]
    option_text = option.text
    option.click()

    # Wait for the legend item to appear
    chart_selector = "#line > div.js-plotly-plot > div > div > svg:nth-child(3) > g.infolayer > g.legend > g > g > g:nth-child(2) > text"
    legend_item = WebDriverWait(dash_duo.driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, chart_selector))
    )

    # Assertions
    assert option_text == legend_item.text, f"Expected legend item text: {option_text}, Actual: {legend_item.text}"
    #assert selected_item_text in options, f"Dropdown should contain '{selected_item_text}'"
"""   
def test_piechart_dropdown(dash_duo):
    
    """
    Check the nav link works and leads to the charts page.
    """
    app = import_app(app_file="app_dash")
    dash_duo.start_server(app)
    # Delay just so I can visually check the page is loaded, this isn't necessary!
    time.sleep(2)

    # Wait for the navlink to be visible
    """dash_duo.wait_for_element("parking", timeout=4)

    # Click on the navlink
    dash_duo.driver.find_element(By.ID, "parking").click()"""
    
    navlink = WebDriverWait(dash_duo.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "parking"))
    )

    # Click on the navlink
    navlink.click()
    
    # Wait for the dropdown element to be visible
    
    dropdown_input = WebDriverWait(dash_duo.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "dropdown"))
    )
    
    dash_duo.wait_for_element_to_be_clickable("dropdown", timeout=2)
    
    dropdown_input.click()
    #dash_duo.wait_for_element("#dropdown", timeout=12)

    # Click on the dropdown (optional, if needed to trigger selection)
    #dropdown_input = dash_duo.find_element("#dropdown")
    #dropdown_input.click()

    # Select the desired item using keyboard interaction (assuming keyboard support)
    selected_item_text = "The University of Aberdeen"  # Replace with your desired item text
    keys_to_press = [Keys.ARROW_DOWN] * 2 + [Keys.ENTER]  # Simulate down arrow x2 then Enter
    for key in keys_to_press:
        dropdown_input.send_keys(key)

    # Wait for the dropdown to contain the selected item text
    dash_duo.wait_for_element_to_contain_text("#dropdown", selected_item_text, timeout=2)

    # Assertion: Verify the selected item text is present
    assert selected_item_text in dash_duo.find_element("#dropdown").text, f"Dropdown should contain '{selected_item_text}'"

def test_piechar_dropdown(dash_duo):
    
    app = import_app(app_file="app_dash")
    dash_duo.start_server(app)
    # Delay just so I can visually check the page is loaded, this isn't necessary!
    time.sleep(2)
    
    navlink = WebDriverWait(dash_duo.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "parking"))
    )

    # Click on the navlink
    navlink.click()
    
    selected_item_text = "2015/16"
    
    dropdown_input = WebDriverWait(dash_duo.driver, 10).until(
        EC.presence_of_element_located((By.ID, "checklist1"))
    )
    
    #dash_duo.wait_for_element_to_be_clickable("dropdown", timeout=2)
    
    dropdown_input.click()
    #dash_duo.wait_for_element("#provider",timeout =30)
    #dash_duo.driver.find_element(By.ID,"provider").click()
    assert selected_item_text in dash_duo.find_element("#checklist1").text, f"Dropdown should contain '{selected_item_text}'"
