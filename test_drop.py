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
    
def test_pie_radio(dash_duo):
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
"""

def test_radio_barchart(dash_duo):
    app = import_app(app_file="app_dash")
    dash_duo.start_server(app)
    time.sleep(2)
    
    navlink = WebDriverWait(dash_duo.driver, 20).until(
        EC.visibility_of_element_located((By.ID, "parking"))
    )

    # Click on the navlink
    navlink.click()  
    
    checkbox = dash_duo.driver.find_element(By.ID,"_dbcprivate_radioitems_checklist1_input_2020/21")
    checkbox.click()
    x_axis_labels_elements=dash_duo.driver.find_elements(By.CLASS_NAME,"xaxislayer-above")
    x_axis_label = "The University of Manchester"
    x_axis_label2 = "The University of Reading" #'Bath Spa University'

    x_axis_labels_texts = [label.text for label in x_axis_labels_elements]
    x_axis_labels = [line for label in x_axis_labels_texts for line in label.split('\n')]
    assert x_axis_label not in x_axis_labels, f"Label '{x_axis_label}' not found in x-axis labels"
    assert x_axis_label2 in x_axis_labels #f"Label '{x_axis_label2}' not found in x-axis labels"

    #dash_duo.driver.implicitly_wait(30)
    time.sleep(15)

def test_click_pie(dash_duo):
    app = import_app(app_file="app_dash")
    dash_duo.start_server(app)
    time.sleep(2)  # Delay just so I can visually check the page is loaded, this isn't necessary!

    navlink = WebDriverWait(dash_duo.driver, 2).until(
        EC.visibility_of_element_located((By.ID, "parking"))
    )
    navlink.click()
    checkbox = dash_duo.driver.find_element(By.ID,"_dbcprivate_radioitems_checklist_input_2020/21")
    checkbox.click()
    css_selector = "#pie > div.js-plotly-plot > div > div > svg:nth-child(1) > g.pielayer > g > g.titletext > text"
    
    chart_title = WebDriverWait(dash_duo.driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector))
    )
    assert ("2020/21" in chart_title.text, "'2021' should appear in the chart title")
    time.sleep(5)
    
