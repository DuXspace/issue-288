from selenium.webdriver.common.by import By
from toolium.pageobjects.page_object import PageObject
from toolium.pageelements.page_element import PageElement


class BasicSite(PageObject):
    base_url = "https://www.basicwebsiteexample.com/"
    basic_site_logo = PageElement(By.ID, "page-zones__template-widgets__companyname-companyname")


def test_sample(driver_wrapper):
    driver_wrapper.driver.get(BasicSite.base_url)
    BasicSite().basic_site_logo.assert_screenshot("page_logo")