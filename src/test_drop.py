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

"""def test_line_dropdown(dash_duo):
    
    app = import_app(app_file="app_dash")
    dash_duo.start_server(app)
    # Delay just so I can visually check the page is loaded, this isn't necessary!
    time.sleep(2)
    
    navlink = WebDriverWait(dash_duo.driver, 20).until(
        EC.visibility_of_element_located((By.ID, "energy"))
    )
    # Click on the navlink
    navlink.click()  
    selected_item_text = "Aston University"
    uni = dash_duo.driver.find_element(By.CLASS_NAME,'Select-value-label')
    uni.click()
    
    options = dash_duo.driver.find_elements(By.CLASS_NAME,'VirtualizedSelectOption')
    option = options[7]
    option.click()
    dash_duo.driver.implicitly_wait(30)
    time.sleep(15)
    chart_selector = "#line > div.js-plotly-plot > div > div > svg:nth-child(3) > g.infolayer > g.legend > g > g > g:nth-child(2) > text"
    legend_item = WebDriverWait(dash_duo.driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,chart_selector ))
    )
    #dash_duo.driver.implicitly_wait(30)
    #time.sleep(15)
    
    #legend_item = dash_duo.driver.find_elements(By.CSS_SELECTOR,chart_selector )
    assert option.text() == legend_item.text()
    #assert len(checkbox) == 2
    assert selected_item_text in options.text, f"Dropdown should contain '{selected_item_text}'" 
    #assert selected_item_text1 in checkboxes.text    
    dash_duo.driver.implicitly_wait(30)
    time.sleep(15)
 """   
def test_radio(dash_duo):
    app = import_app(app_file="app_dash")
    dash_duo.start_server(app)
    # Delay just so I can visually check the page is loaded, this isn't necessary!
    time.sleep(2)
    
    navlink = WebDriverWait(dash_duo.driver, 20).until(
        EC.visibility_of_element_located((By.ID, "parking"))
    )

    # Click on the navlink
    navlink.click()  
    
    checkbox = dash_duo.driver.find_element(By.ID,"_dbcprivate_radioitems_checklist1_input_2020/21")
    checkbox.click()
    dash_duo.driver.implicitly_wait(30)
    time.sleep(15)
    
"""def test_pie_radio(dash_duo):
    app = import_app(app_file="app_dash")
    dash_duo.start_server(app)
    # Delay just so I can visually check the page is loaded, this isn't necessary!
    time.sleep(2)
    
    navlink = WebDriverWait(dash_duo.driver, 20).until(
        EC.visibility_of_element_located((By.ID, "parking"))
    )

    # Click on the navlink
    navlink.click()  
    
    #checkbox = dash_duo.driver.find_element(By.CLASS_NAME,"Select-input")
    checkbox = dash_duo.driver.find_element(By.ID,"dropdown")
    checkbox.click()
    unis = dash_duo.driver.find_element(By.CLASS_NAME,'Select-value')
    uni = unis[2]
    uni.click()
    dash_duo.driver.implicitly_wait(30)
    time.sleep(15)
  """  

def test_url(dash_duo):

    app = import_app(app_file="app_dash")
    dash_duo.start_server(app)
    time.sleep(2)  # Delay just so I can visually check the page is loaded, this isn't necessary!

    navlink = WebDriverWait(dash_duo.driver, 20).until(
        EC.visibility_of_element_located((By.ID, "energy"))
    )
    navlink.click()  

    # Perform actions to navigate to another URL
    # Example: Clicking a link
    link_element = dash_duo.driver.find_element_by_link_text("Go to home page")
    link_element.click()

    # Wait for a brief moment to ensure the page navigation is complete
    time.sleep(2)

    # Get the current URL
    current_url = dash_duo.driver.current_url

    # Assert if the current URL matches the expected URL
    expected_url = "/home"
    assert expected_url in current_url, f"URL mismatch. Expected: {expected_url}, Actual: {current_url}"

def test_line_chart_selection(dash_duo):
    
    """GIVEN the app is running
    WHEN the dropdown for the line chart is changed to
    THEN the H1 heading text should be "Paralympics Dashboard"
    """
    
    app = import_app(app_file="app_dash")
    dash_duo.start_server(app)
    
    navlink = WebDriverWait(dash_duo.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "energy"))
    )

    # Click on the navlink
    navlink.click()

    # Delay just so I can visually check the page is loaded, this isn't necessary!
    time.sleep(2)
    dash_duo.driver.implicitly_wait(2)
    css_selector = "#line > div.js-plotly-plot > div > div > svg:nth-child(3) > g.infolayer > g.g-gtitle > text"
    #chart_title = dash_duo.find_element(css_selector)
    chart_title = WebDriverWait(dash_duo.driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector))
    )
    assert ("Energy" in chart_title.text, "'Energy' should appear in the chart title")
    